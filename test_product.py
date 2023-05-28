import pytest
import products


def test_right_product():
    assert products.Product("An Item", price=1450, quantity=100)


def test_wrong_product_name():
    with pytest.raises(TypeError):
        products.Product("", price=1450, quantity=100)


def test_wrong_quantity():
    with pytest.raises(TypeError):
        products.Product("good name", price=500, quantity=-100)


def test_wrong_price():
    with pytest.raises(TypeError):
        products.Product("good name", price=-500, quantity=-100)


def test_is_inactive():
    a_product = products.Product("PC", price=500, quantity=300)
    a_product.set_quantity(300)
    assert not a_product.is_active()


def test_changes_to_quantity():
    a_product = products.Product("PC", price=500, quantity=300)
    a_product.set_quantity(100)
    assert a_product.get_quantity() == 200


def test_buy_larger_quantity_then_exists():
    a_product = products.Product("PC", price=500, quantity=300)
    assert a_product.buy(400) == 0


def test_no_stock_needed_product():
    assert products.NonStockedProduct("An Item", price=1450)


def test_no_stock_needed_product_buy():
    a_product = products.NonStockedProduct("IBM", price=1500)
    assert a_product.buy(500)


def test_limited_product():
    a_product = products.LimitedProduct("Nvidia", price=1500, quantity=500, maximum=1)
    with pytest.raises(Exception):
        a_product.buy(20)
