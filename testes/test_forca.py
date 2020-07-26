from app.core import Forca

def test_animais():
    f = Forca('animais')

    assert isinstance(f.palavra(), str)

def test_paises():
    f = Forca('paises')

    assert isinstance(f.palavra(), str)