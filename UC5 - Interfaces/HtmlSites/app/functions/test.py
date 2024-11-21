import pytest
import errorhandler
import validadors # Replace `your_module` with the file name where `validator` is defined.

def test_validate_email():
    v = validadors()
    assert v.validate_email("test@test.com") == True
    assert v.validate_email("invalid-email") == False

def test_validate_password():
    
    v = validadors()
    with pytest.raises(errorhandler):
        v.validate_password("short")  # Invalid: Too short

    with pytest.raises(errorhandler):
        v.validate_password("longbutnocapitals123")  # Invalid: Missing capital letters

    assert v.validate_password("Valid1@Password") == True

def test_validate_telefone():
    v = validadors()
    with pytest.raises(errorhandler):
        v.validate_telefone("12345")  # Invalid: Too short

    with pytest.raises(errorhandler):
        v.validate_telefone("abcdefghijk")  # Invalid: Not numeric

    assert v.validate_telefone("12345678901") == True
