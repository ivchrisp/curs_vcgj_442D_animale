import lib.biblioteca_animale as b_animale

def test_culoare_puma():
    cul = b_animale.culoare_puma()
    if cul == 'bej':
        assert True
    else:
        assert False

def test_hrana_puma():
    inf = b_animale.hrana_puma()
    if inf == 'carnivor':
        assert True
    else:
        assert False

def test_invelisul_corpului_puma():
    inf = b_animale.invelis_puma()
    if inf == 'blana':
        assert True
    else:
        assert False
