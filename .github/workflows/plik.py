def dodaj(a,b):
    return a+b

def test_dodaj():
    assert dodaj(5,2) == 7
    assert dodaj(5,5) == 10
    assert dodaj(5,3) == 8
    assert dodaj(5,6) == 11