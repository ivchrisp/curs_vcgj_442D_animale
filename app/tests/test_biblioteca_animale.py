import lib.biblioteca_animale as b_animale

def test_culoare_frenchbulldog():
    cul = b_animale.culoare_frenchbulldog()
    if cul == 'gri':
        assert True
    else:
        assert False

def test_hrana_frenchbulldog():
    inf = b_animale.hrana_frenchbulldog()
    if inf == 'carnivor':
        assert True
    else:
        assert False

def test_invelisul_corpului_frenchbulldog():
    inf = b_animale.invelisul_corpului_frenchbulldog()
    if inf == 'blana':
        assert True
    else:
        assert False
