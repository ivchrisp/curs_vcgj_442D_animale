import lib.biblioteca_animale as b_animale

def test_culoare_sinsila():
    cul = b_animale.culoare_sinsila()
    if cul == 'cafeniu':
        assert True
    else:
        assert False

def test_hrana_sinsila():
    inf = b_animale.hrana_sinsila()
    if inf == 'carnivor':
        assert True
    else:
        assert False

def test_invelisul_corpului_sinsila():
    inf = b_animale.invelisul_corpului_sinsila()
    if inf == 'blana':
        assert True
    else:
        assert False
