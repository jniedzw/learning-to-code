import pytest
from twttr import shorten

def test_shorten():
    assert shorten("hello world") == "hll wrld"

def test_uppercase():
    assert shorten("UppEr CaSE") == "ppr CS"

def test_vowel():
    assert shorten("aeiou") == ""

    