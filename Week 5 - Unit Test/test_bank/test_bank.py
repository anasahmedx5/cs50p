from bank import value

def test_value():
    assert value("Hello") == 0
    assert value(" Hello ") == 0
    assert value("How you doing?") == 20
    assert value("What's up?") == 100
    assert value("How was your day?") == 20
    assert value("Sup") == 100
