from flask import render_template


def test_main_route(test_client, modify_db_config):
    response = test_client.get("/")
    assert response.data.decode() == render_template('profile.html')
