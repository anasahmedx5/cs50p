from numb3rs import validate


def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True
    assert validate("11.99.22.88") == True
    assert validate("249.249.249.249") == True

    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("275.3.6.28") == False
    assert validate("199.9911.123.321") == False
