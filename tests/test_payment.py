from pay.order import Order, LineItem, OrderStatus
from pay.payment import pay_order
import pytest
from pay.creditcard import CreditCard
from datetime import date

class PaymentProcessorMock:
    def charge(self, card: CreditCard, amount: int) -> None:
        print(f"Charging the card with the amount ${amount/100:.2f}.")


@pytest.fixture
def card() -> CreditCard:
    year = date.today().year + 2
    return CreditCard('4111111111111111', 12, year)

def test_pay_order(card: CreditCard) -> None:
    o = Order()
    o.line_items.append(LineItem(name="Test", price=100))
    pay_order(o, card, PaymentProcessorMock())
    assert o.status == OrderStatus.PAID


def test_pay_order_invalid(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        o = Order()
        pay_order(o, card, PaymentProcessorMock())
