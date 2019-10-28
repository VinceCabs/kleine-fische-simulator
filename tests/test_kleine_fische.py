import pytest
import kleine_fische

def test_de():
    couleur = Partie.de()
    assert type(couleur) is str