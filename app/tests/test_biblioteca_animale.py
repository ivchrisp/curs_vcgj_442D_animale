import lib.biblioteca_animale as b_animale

def test_culoare_ornitorinc():
    cul = b_animale.culoare_ornitorinc()
    if cul == 'cafeniu':
        assert True
    else:
        assert False

def test_hrana_ornitorinc():
    inf = b_animale.hrana_ornitorinc()
    if inf == 'carnivor':
        assert True
    else:
        assert False

def test_invelisul_corpului_ornitorinc():
    inf = b_animale.invelisul_corpului_ornitorinc()
    if inf == 'blana':
        assert True
    else:
        assert False
