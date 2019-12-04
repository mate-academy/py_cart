"""
docstring
"""
import cart


def test_product():
    """

    :return:
    """
    c = cart.Cart("products.csv")
    p = c.get_product(0)
    assert isinstance(p, cart.Product)
    assert p.name == "Apples"
    assert p.price == 2.3
    assert p.qty == 5


def test_cart():
    """

    :return:
    """
    c = cart.Cart("products.csv")
    assert c.calc_total() == 74.3
