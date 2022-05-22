# @pytest.fixture(scope="session")
# def client():
#     app = create_app(testing=True)
#     with app.test_client() as client:
#         with app.app_context():
#             yield client 
from api.app import create_app
import pytest

@pytest.fixture
def app():
    app = create_app()
    return app