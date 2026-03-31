from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from config import Config

def create_app():
    frontend_dir = Config.FRONTEND_DIR
    app = Flask(__name__, static_folder=frontend_dir, static_url_path="")
    app.config.from_object(Config)
    CORS(app)

    from app.routes.scanner import scanner_bp
    app.register_blueprint(scanner_bp)

    @app.get('/')
    def index():
        return send_from_directory(frontend_dir, 'index.html')

    @app.get('/health')
    def health():
        return jsonify({"status": "ok", "project": "mifos-gazelle-iac-cli-prototype"})

    return app