from pythport import __version__
from pythport.bcrypt import Bcrypt_Encrypt
import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_bcrypt_returns_hash_len_60():
    a = Bcrypt_Encrypt('spam')
    b = Bcrypt_Encrypt('SpamAndEggs')
    c = Bcrypt_Encrypt('hi')
    assert len(a.cook_hash()) == 60
    assert len(b.cook_hash()) == 60
    assert len(c.cook_hash()) == 60

