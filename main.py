import os
from pay.creditcard import CreditCard
from pay.order import LineItem, Order
from pay.processor import PaymentProcessor
from pay.payment import pay_order
from dotenv import load_dotenv


def read_card_info() -> CreditCard:
    card = input("Please enter your card number: ")
    month = int(input("Please enter your card expiry month: "))
    year = int(input("Please enter your card expiry year: "))
    return CreditCard(card, month, year)

def main():
    load_dotenv()
    api_key = os.getenv('API_KEY')
    processor = PaymentProcessor(api_key)

    #Test card number: 1234556789
    order = Order()
    order.line_items.append(LineItem(name="Shoes", price=100, quantity=2))
    order.line_items.append(LineItem(name="Hat", price=50))

    card = read_card_info()
    pay_order(order, card, processor)


if __name__ == '__main__':
    main()

