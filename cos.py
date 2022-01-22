import plik


def test_dodaj():
    assert plik.dodaj(5,6) == 11
    assert plik.dodaj(5,2) == 7
    assert plik.dodaj(5,5) == 10
    assert plik.dodaj(5,3) == 8