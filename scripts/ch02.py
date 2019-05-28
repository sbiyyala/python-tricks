from typing import Any


def apply_discount(product: Any, discount: float) -> float:
    """

    :param discount: float
    :type product: {"price": float}
    """
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price
