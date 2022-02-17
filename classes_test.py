import classes as C

def test_StringAble():
    oStringable = C.StringAble()
    assert "Biff" in str(oStringable)

def test_StringAbleConstructor():
    oStringAble = C.StringAble("George")
    assert "George" in str(oStringAble)