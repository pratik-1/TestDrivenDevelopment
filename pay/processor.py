from datetime import datetime
from pay.creditcard import CreditCard


class PaymentProcessor:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    # check api key
    def _check_api_key(self) -> bool:
        # dummy api key hardcoded to demo. Should be defined ouside the code.
        return self.api_key == "6cfb67f3-6281-4031-b893-ea85db0dce20"

    # charge amount to creditcard
    def charge(self, card: CreditCard, amount: int) -> None:
        if not self.validate_card(card):
            raise ValueError("Invalid card")
        if not self._check_api_key():
            raise ValueError("Invalid API key")
        print(f"Charging card number {card.number} for ${amount/100:.2f}")

    # validate card
    def validate_card(self, card: CreditCard) -> bool:
        return luhn_checksum(card.number) and datetime(card.expiry_year, card.expiry_month, 1) > datetime.now()


def luhn_checksum(card_number: str) -> bool:
    """Check if card number is valid (Could be any other implementation)"""
     
    nDigits = len(card_number)
    checksum = 0
    isSecond = False
     
    for i in range(nDigits - 1, -1, -1):
        d = ord(card_number[i]) - ord('0')
     
        if (isSecond == True):
            d = d * 2
  
        # We add two digits to handle
        # cases that make two digits after doubling
        checksum += d // 10
        checksum += d % 10
  
        isSecond = not isSecond
    return checksum % 10 == 0
     