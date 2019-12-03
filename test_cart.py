import cart


def test_product():
    c = cart.Cart("products.csv")
    p = c.get_product(0)
    assert isinstance(p, cart.Product)
    assert p.name() == "Apples"
    assert p.price() == 2.3
    assert p.qty() == 5


def test_cart():
    c = cart.Cart("products.csv")
    assert c.calc_total() == 74.3
