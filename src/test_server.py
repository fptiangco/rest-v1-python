from server import app


def test_v1():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.data == b"v1"
