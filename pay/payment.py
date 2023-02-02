from typing import Protocol
from pay.creditcard import CreditCard
from pay.order import Order

class PaymentProcessor(Protocol):
    def charge(self, card: str, amount: int) -> None:
        """Charges the card with the amount."""


def pay_order(order: Order, card: CreditCard, processor: PaymentProcessor):
    """Process payment with order basket to given credit card"""
    if order.total == 0:
        raise ValueError("Can't pay an order with total 0.")
    processor.charge(card, amount=order.total)
    order.pay()