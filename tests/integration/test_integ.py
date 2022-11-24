from shop_app import db


def test_get_db(test_client, modify_db_config):
    connection = db.get_db()
    assert connection.is_connected()


def test_get_db_reconnects_disconnected_connection(test_client, modify_db_config):
    connection = db.get_db()
    connection.disconnect()

    assert not connection.is_connected()
    assert db.get_db().is_connected()
