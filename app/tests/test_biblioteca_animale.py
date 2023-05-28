import lib.biblioteca_animale as b_animale

def test_culoare_hamster():
    cul = b_animale.culoare_ornitorinc()
    if cul == 'bej':
        assert True
    else:
        assert False

def test_hrana_hamster():
    inf = b_animale.hrana_ornitorinc()
    if inf == 'ierbivor':
        assert True
    else:
        assert False

def test_invelisul_corpului_hamster():
    inf = b_animale.invelisul_corpului_ornitorinc()
    if inf == 'blana':
        assert True
    else:
        assert False
