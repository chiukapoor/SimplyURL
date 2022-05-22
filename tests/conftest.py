try:
    from api.app import create_app
    import pytest
except Exception as e:
    print("Error: {} ".format(e))


@pytest.fixture
def app():
    app = create_app()
    return app
