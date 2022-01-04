import pytest
import json
import tkinter as tk
from pythport import __version__
from pythport.bcrypt import BcryptEncrypt
from pythport.aes import AesEncrypt
from pythport.main import PythPortMain, LoginPage

def test_version():
    assert __version__ == '0.1.0'


def test_bcrypt_returns_hash_len_60():
    a = BcryptEncrypt('spam')
    b = BcryptEncrypt('SpamAndEggs')
    c = BcryptEncrypt('hi')
    assert len(a.cook_hash()) == 60
    assert len(b.cook_hash()) == 60
    assert len(c.cook_hash()) == 60


def test_matching_password():
    bc = BcryptEncrypt("password")
    hash = bc.cook_hash()
    assert bc.validate_pwd("password", hash)


def test_matching_password():
    bc = BcryptEncrypt("password")
    hash = bc.cook_hash()
    assert not bc.validate_pwd("badpass", hash)


def test_init_pythportmain():
    ppm = PythPortMain()
    assert ppm.title() == "PythPort"
    assert ppm.pm == None


def test_login_length_success(reset_master_json):
    ppm = PythPortMain()
    log = LoginPage(ppm)
    log.pw_entry = tk.StringVar(value="potato123")
    assert log.submit() == 'Success'     


def test_login_length_fail(reset_master_json):
    ppm = PythPortMain()
    log = LoginPage(ppm)
    log.pw_entry = tk.StringVar(value = "potato")
    assert log.submit() == 'Fail' 


def test_aes_encrypt():
    aes = AesEncrypt("password")
    phrase = "supersecret"
    encrypted = aes.encrypt(phrase)
    assert encrypted != phrase
    
    
def test_aes_encrypt_decrypt():
    aes = AesEncrypt("password")
    phrase = "supersecret"
    encrypted = aes.encrypt(phrase)
    decrypted = aes.decrypt(encrypted)
    assert decrypted == phrase


def test_aes_bad_key():
    aes = AesEncrypt("password")
    phrase = "supersecret"
    encrypted = aes.encrypt(phrase)

    bad_aes = AesEncrypt("wrongpass")
    with pytest.raises(Exception) as e:
        bad_aes.decrypt(encrypted)
        assert e


@pytest.fixture
def reset_master_json():
    with open('assets/master.json', "w") as f:
        master_dict = {"master": {"hash": None}}
        f.write(json.dumps(master_dict))
    return 

