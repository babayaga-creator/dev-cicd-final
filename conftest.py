import mysql.connector
import os
import pytest
from shop_app import create_app


def ready(config):
    try:
        conn = mysql.connector.connect(**config)
        return conn.is_connected()
    except Exception:
        return False


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join(str(pytestconfig.rootdir), "tests", "integration", "docker-compose.yml")


@pytest.fixture(scope="session")
def database_config(docker_ip, docker_services):
    """Ensure that HTTP service is up and responsive."""

    docker_port = docker_services.port_for("db", 3306)
    config = {
        "host": docker_ip,
        "user": "username",
        "password": "password",
        "database": "example",
    }

    docker_services.wait_until_responsive(timeout=60.0, pause=0.5, check=lambda: ready(config))
    return config


@pytest.fixture()
def test_client():
    app = create_app()
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client


@pytest.fixture()
def modify_db_config(mocker, database_config):
    yield mocker.patch("shop_app.db.get_db_config", return_value=database_config)
