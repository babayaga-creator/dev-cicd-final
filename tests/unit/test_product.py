from shop_app import product


def test_get_section_message():

    assert product.get_section_message() == "Here is all the registered names!"
