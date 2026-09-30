import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from validator import validate_email, validate_phone


def test_validate_email_valid():
    assert validate_email("user@example.com") is True


def test_validate_email_invalid():
    assert validate_email("not-an-email") is False


def test_validate_phone_valid():
    assert validate_phone("+79161234567") is True
    assert validate_phone("89161234567") is True
    assert validate_phone("79161234567") is True


def test_validate_phone_invalid():
    assert validate_phone("12345") is False
    assert validate_phone("+1234567890") is False
    assert validate_phone("abc") is False# test: add phone validation tests
