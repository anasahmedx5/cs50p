from plates import is_valid

def test_is_valid():
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False
    assert is_valid("1234") ==  False
    assert is_valid("ANAS05") == False
    assert is_valid("AN50AS") == False
    assert is_valid("CS50P") == False
    assert is_valid("ANAS?") == False
    assert is_valid("CS50") == True
