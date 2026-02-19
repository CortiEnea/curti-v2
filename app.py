import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask

from db import init_db, seed_defaults
from routes.admin import admin
from routes.site import site
from site_data import COMPANY, USFA

load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "change-me-in-production")

    app.register_blueprint(site)
    app.register_blueprint(admin)

    init_db()
    seed_defaults()

    @app.context_processor
    def inject_globals():
        return {"company": COMPANY, "year": datetime.now().year, "usfa": USFA}

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5001)
