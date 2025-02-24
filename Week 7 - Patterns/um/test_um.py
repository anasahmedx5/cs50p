from um import count

def test_count():
    assert count("") == 0
    assert count("hello there!") == 0
    assert count("Plum and rummage") == 0
    assert count("um, I don't know.") == 1
    assert count("It's um amazing, um I must say.") == 2
    assert count("um, I think um, really um!") == 3
    assert count("Um, um, UM, uM!") == 4


