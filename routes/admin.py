from __future__ import annotations

import json
import os
import uuid
from functools import wraps

from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

import db

admin = Blueprint("admin", __name__, url_prefix="/admin")

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "uploads")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}


def _allowed(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def _save_upload(file) -> str:
    """Save an uploaded file and return its path relative to static/."""
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    ext = file.filename.rsplit(".", 1)[1].lower()
    name = f"{uuid.uuid4().hex}.{ext}"
    file.save(os.path.join(UPLOAD_FOLDER, name))
    return f"uploads/{name}"


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("is_admin"):
            return redirect(url_for("admin.login"))
        return f(*args, **kwargs)
    return decorated


# ── Auth ──────────────────────────────────────────────────────────────────────

@admin.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password", "")
        admin_hash = os.getenv("ADMIN_PASSWORD_HASH", "")

        if not admin_hash:
            flash("Nessuna password admin configurata.", "error")
            return redirect(url_for("admin.login"))

        if check_password_hash(admin_hash, password):
            session["is_admin"] = True
            flash("Accesso effettuato.", "success")
            return redirect(url_for("admin.panel"))
        else:
            flash("Password errata.", "error")
            return redirect(url_for("admin.login"))

    return render_template("admin_login.html")


@admin.route("/logout")
def logout():
    session.pop("is_admin", None)
    flash("Logout effettuato.", "success")
    return redirect(url_for("admin.login"))


# ── Panel ─────────────────────────────────────────────────────────────────────

@admin.route("/")
@login_required
def panel():
    projects = db.get_projects()
    listings = db.get_listings()
    return render_template("admin_panel.html", projects=projects, listings=listings)


# ── Projects CRUD ─────────────────────────────────────────────────────────────

@admin.route("/projects/add", methods=["POST"])
@login_required
def project_add():
    title = (request.form.get("title") or "").strip()
    location = (request.form.get("location") or "").strip()
    goal = (request.form.get("goal") or "").strip()
    solution = (request.form.get("solution") or "").strip()
    materials = (request.form.get("materials") or "").strip()

    image = ""
    file = request.files.get("image")
    if file and file.filename and _allowed(file.filename):
        image = _save_upload(file)

    image_url = (request.form.get("image_url") or "").strip()
    if not image and image_url:
        image = image_url

    if not all([title, location, goal, solution, materials]):
        flash("Compila tutti i campi obbligatori.", "error")
        return redirect(url_for("admin.panel") + "#progetti")

    db.create_project(title, location, goal, solution, materials, image)
    flash("Progetto aggiunto.", "success")
    return redirect(url_for("admin.panel") + "#progetti")


@admin.route("/projects/<int:project_id>/edit", methods=["POST"])
@login_required
def project_edit(project_id: int):
    project = db.get_project(project_id)
    if not project:
        flash("Progetto non trovato.", "error")
        return redirect(url_for("admin.panel") + "#progetti")

    title = (request.form.get("title") or "").strip()
    location = (request.form.get("location") or "").strip()
    goal = (request.form.get("goal") or "").strip()
    solution = (request.form.get("solution") or "").strip()
    materials = (request.form.get("materials") or "").strip()

    image = project["image"]
    file = request.files.get("image")
    if file and file.filename and _allowed(file.filename):
        image = _save_upload(file)

    image_url = (request.form.get("image_url") or "").strip()
    if image_url:
        image = image_url

    if not all([title, location, goal, solution, materials]):
        flash("Compila tutti i campi obbligatori.", "error")
        return redirect(url_for("admin.panel") + "#progetti")

    db.update_project(project_id, title, location, goal, solution, materials, image)
    flash("Progetto aggiornato.", "success")
    return redirect(url_for("admin.panel") + "#progetti")


@admin.route("/projects/<int:project_id>/delete", methods=["POST"])
@login_required
def project_delete(project_id: int):
    db.delete_project(project_id)
    flash("Progetto eliminato.", "success")
    return redirect(url_for("admin.panel") + "#progetti")


# ── Real Estate CRUD ──────────────────────────────────────────────────────────

@admin.route("/listings/add", methods=["POST"])
@login_required
def listing_add():
    listing_type = (request.form.get("listing_type") or "").strip()
    place = (request.form.get("place") or "").strip()
    title = (request.form.get("title") or "").strip()
    rooms = (request.form.get("rooms") or "").strip()
    floor = (request.form.get("floor") or "").strip()
    price_chf = request.form.get("price_chf", "0").strip()
    price_label = (request.form.get("price_label") or "").strip()
    description = (request.form.get("description") or "").strip()
    bullets_raw = (request.form.get("bullets") or "").strip()

    if not all([listing_type, place, title, rooms, floor, description]):
        flash("Compila tutti i campi obbligatori.", "error")
        return redirect(url_for("admin.panel") + "#immobili")

    try:
        price_chf = int(price_chf)
    except ValueError:
        flash("Prezzo non valido.", "error")
        return redirect(url_for("admin.panel") + "#immobili")

    bullets = [b.strip() for b in bullets_raw.split("\n") if b.strip()]

    images = []
    files = request.files.getlist("images")
    for f in files:
        if f and f.filename and _allowed(f.filename):
            images.append(url_for("static", filename=_save_upload(f)))

    image_urls = (request.form.get("image_urls") or "").strip()
    if image_urls:
        images.extend([u.strip() for u in image_urls.split("\n") if u.strip()])

    db.create_listing(listing_type, place, title, rooms, floor, price_chf, price_label, description, bullets, images)
    flash("Immobile aggiunto.", "success")
    return redirect(url_for("admin.panel") + "#immobili")


@admin.route("/listings/<int:listing_id>/edit", methods=["POST"])
@login_required
def listing_edit(listing_id: int):
    listing = db.get_listing(listing_id)
    if not listing:
        flash("Immobile non trovato.", "error")
        return redirect(url_for("admin.panel") + "#immobili")

    listing_type = (request.form.get("listing_type") or "").strip()
    place = (request.form.get("place") or "").strip()
    title = (request.form.get("title") or "").strip()
    rooms = (request.form.get("rooms") or "").strip()
    floor = (request.form.get("floor") or "").strip()
    price_chf = request.form.get("price_chf", "0").strip()
    price_label = (request.form.get("price_label") or "").strip()
    description = (request.form.get("description") or "").strip()
    bullets_raw = (request.form.get("bullets") or "").strip()

    if not all([listing_type, place, title, rooms, floor, description]):
        flash("Compila tutti i campi obbligatori.", "error")
        return redirect(url_for("admin.panel") + "#immobili")

    try:
        price_chf = int(price_chf)
    except ValueError:
        flash("Prezzo non valido.", "error")
        return redirect(url_for("admin.panel") + "#immobili")

    bullets = [b.strip() for b in bullets_raw.split("\n") if b.strip()]

    images = list(listing["images"])

    files = request.files.getlist("images")
    new_uploads = False
    for f in files:
        if f and f.filename and _allowed(f.filename):
            images.append(url_for("static", filename=_save_upload(f)))
            new_uploads = True

    image_urls = (request.form.get("image_urls") or "").strip()
    if image_urls:
        images.extend([u.strip() for u in image_urls.split("\n") if u.strip()])

    remove_images = request.form.getlist("remove_images")
    if remove_images:
        images = [img for img in images if img not in remove_images]

    db.update_listing(listing_id, listing_type, place, title, rooms, floor, price_chf, price_label, description, bullets, images)
    flash("Immobile aggiornato.", "success")
    return redirect(url_for("admin.panel") + "#immobili")


@admin.route("/listings/<int:listing_id>/delete", methods=["POST"])
@login_required
def listing_delete(listing_id: int):
    db.delete_listing(listing_id)
    flash("Immobile eliminato.", "success")
    return redirect(url_for("admin.panel") + "#immobili")
