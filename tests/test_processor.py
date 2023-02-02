from datetime import date
from pay.processor import luhn_checksum, PaymentProcessor
from pay.creditcard import CreditCard
import pytest
import os

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY') or ''


@pytest.fixture
def card() -> CreditCard:
    year = date.today().year + 2
    return CreditCard('4111111111111111', 12, year)

@pytest.fixture
def invalid_card() -> CreditCard:
    year = date.today().year - 2
    return CreditCard('123456789', 12, year)

def test_api_key_invalid(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        processor= PaymentProcessor("")
        processor.charge(card,100)


def test_api_key(card: CreditCard) -> None:
    processor= PaymentProcessor(API_KEY)
    processor.charge(card, 100)


def test_card_invalid_date(invalid_card: CreditCard) -> None:
    with pytest.raises(ValueError):
        processor= PaymentProcessor(API_KEY)
        processor.charge(invalid_card, 100)


def test_card_invalid_luhn(invalid_card: CreditCard) -> None:
    assert not luhn_checksum(invalid_card.number)

def test_card_valid_luhn(card: CreditCard) -> None:
    assert luhn_checksum(card.number)

def test_validate_invalid_card(invalid_card: CreditCard) -> None:
    processor= PaymentProcessor(API_KEY)
    assert not processor.validate_card(invalid_card)

def test_validate_card(card: CreditCard) -> None:
    processor= PaymentProcessor(API_KEY)
    assert processor.validate_card(card)
