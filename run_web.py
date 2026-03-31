import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
WEBAPP_DIR = os.path.join(BASE_DIR, "webapp")
if WEBAPP_DIR not in sys.path:
    sys.path.insert(0, WEBAPP_DIR)

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
