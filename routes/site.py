from flask import Blueprint, render_template, request

import db
from site_data import ABOUT, PRODUCTS, SERVICES, COMPANY, IMAGES

site = Blueprint("site", __name__)


@site.get("/")
def home():
    projects = db.get_projects()[:3]
    return render_template("index.html", services=SERVICES[:3], projects=projects, images=IMAGES)


@site.get("/about")
def about():
    return render_template("about.html", about=ABOUT)


@site.get("/projects")
def projects():
    project_list = db.get_projects()
    return render_template("projects.html", projects=project_list, images=IMAGES)


@site.get("/products")
def products():
    return render_template("products.html", products=PRODUCTS, images=IMAGES)


@site.get("/real-estate")
def real_estate():
    listings = db.get_listings()
    return render_template("real_estate.html", listings=listings)


@site.route("/contact", methods=["GET", "POST"])
def contact():
    success = False
    data = {"name": "", "email": "", "phone": "", "message": ""}

    if request.method == "POST":
        data = {
            "name": (request.form.get("name") or "").strip(),
            "email": (request.form.get("email") or "").strip(),
            "phone": (request.form.get("phone") or "").strip(),
            "message": (request.form.get("message") or "").strip(),
        }

        if data["name"] and data["email"] and data["message"]:
            success = True
            print("[contact_form]", data)

    return render_template("contact.html", success=success, form=data)
