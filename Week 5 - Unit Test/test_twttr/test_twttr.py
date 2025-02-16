from twttr import shorten

def test_shorten():
    assert shorten("anas") == "ns"
    assert shorten("anas ahmed") == "ns hmd"
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("bcdfgh") == "bcdfgh"
    assert shorten("BCDFGH") == "BCDFGH"
    assert shorten("12345") == "12345"
    assert shorten("h3y") == "h3y"
    assert shorten("!@.") == "!@."
