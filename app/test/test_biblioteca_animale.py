import lib.biblioteca_animale as b_animale

def test_culoare_koala():
    cul = b_animale.culoare_koala()
    if cul == 'gri si alb':
        assert True
    else:
        assert False

def test_hrana_koala():
    inf = b_animale.hrana_koala()
    if inf == 'ierbibor':
        assert True
    else:
        assert False

def test_invelisul_corpului_koala():
    inf = b_animale.invelisul_corpului_koala()
    if inf == 'blana':
        assert True
    else:
        assert False

