from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("How are you? ") == 20
    assert value("What are you doing? ") == 100