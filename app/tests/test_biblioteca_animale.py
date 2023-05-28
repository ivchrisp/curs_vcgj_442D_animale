import lib.biblioteca_animale as b_animale

def test_culoare_veverita():
    cul = b_animale.culoare_veverita()
    if cul == 'maro':
        assert True
    else:
        assert False

def test_hrana_veverita():
    inf = b_animale.hrana_veverita()
    if inf == 'ierbivor':
        assert True
    else:
        assert False

def test_invelisul_corpului_veverita():
    inf = b_animale.invelisul_corpului_veverita()
    if inf == 'blana':
        assert True
    else:
        assert False

