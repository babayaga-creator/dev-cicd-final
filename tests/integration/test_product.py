from flask import (
    Blueprint, jsonify, request
)
import json


def test_index(test_client, modify_db_config):
    response = test_client.get("/product")
    assert "Nail" in response.data.decode()


def test_create_product(test_client, modify_db_config):

    data = {"name": "CIVI", "price": 100}
    url = "/product"

    response = test_client.post(url, json=data)
    assert "ok" in response.data.decode()
