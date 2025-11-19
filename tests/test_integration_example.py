import importlib.util
import os

# Trouver le chemin absolu vers app.py
app_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "app.py")

spec = importlib.util.spec_from_file_location("app", app_path)
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


def test_homepage():
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
