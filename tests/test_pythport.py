from pythport import __version__
from pythport.bcrypt import BcryptEncrypt
import pytest
import json

def test_version():
    assert __version__ == '0.1.0'


def test_bcrypt_returns_hash_len_60():
    a = BcryptEncrypt('spam')
    b = BcryptEncrypt('SpamAndEggs')
    c = BcryptEncrypt('hi')
    assert len(a.cook_hash()) == 60
    assert len(b.cook_hash()) == 60
    assert len(c.cook_hash()) == 60
    

@pytest.fixture
def reset_test_json():
    with open('assets/test.json', "w") as f:
        master_dict = {"master": {"hash": None}}
        f.write(json.dumps(master_dict))
    return 