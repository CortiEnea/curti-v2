from datetime import datetime

from flask import Flask
from routes.site import site
from site_data import COMPANY, USFA


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(site)

    @app.context_processor
    def inject_globals():
        return {"company": COMPANY, "year": datetime.now().year, "usfa": USFA}

    return app


if __name__ == "__main__":
    create_app().run(debug=True, port=5001)
