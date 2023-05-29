import lib.biblioteca_animale as b_animale

def test_culoare_broasca():
    cul = b_animale.culoare_broasca()
    if cul == 'verde':
        assert True
    else:
        assert False

def test_hrana_broasca():
    inf = b_animale.hrana_broasca()
    if inf == 'omnivor':
        assert True
    else:
        assert False

def test_invelisul_corpului_broasca():
    inf = b_animale.invelisul_corpului_broasca()
    if inf == 'carapace':
        assert True
    else:
        assert False

