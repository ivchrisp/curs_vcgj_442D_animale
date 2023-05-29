import lib.biblioteca_animale as b_animale

def test_culoare_bursuc():
    cul = b_animale.culoare_bursuc()
    if cul == 'gri':
        assert True
    else:
        assert False

def test_hrana_bursuc():
    inf = b_animale.hrana_bursuc()
    if inf == 'omnivor':
        assert True
    else:
        assert False

def test_invelisul_corpului_bursuc():
    inf = b_animale.invelisul_corpului_bursuc()
    if inf == 'blana':
        assert True
    else:
        assert False
