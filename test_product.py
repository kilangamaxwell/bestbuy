import pytest
from products import Product


def test_product_creation():
    """Test that creating a normal product works."""
    product = Product("Test Product", 1150, 100)
    assert product.name == "Test Product"
    assert product.price == 1150
    assert product.quantity == 100
    assert product.is_active() is True


def test_invalid_product_creation():
    """Test that creating a product with invalid details 
    (empty name, negative price) invokes an exception."""
    with pytest.raises(Exception):
        Product("", -1050, 100)


def test_zero_quantity():
    """Test that when a product reaches 0 quantity, 
    it becames inactive."""
    product = Product("Test Product", 1150, 0)
    assert product.is_active() is False


def test_quantity_after_purchase():
    """Test that product purchase modifies the 
    quantity and returns th right output."""
    product = Product("Test Product", 1150, 200)
    purchase_price = product.buy(50)
    assert product.quantity == 150
    assert purchase_price == 1150 * 50


def test_notify_insufficient_quantity():
    """Test that buying a larger quantity than 
    exists invokes exception."""
    with pytest.raises(Exception):
        Product("Test Product", 1150, 100).buy(200)


pytest.main()
