import lib.biblioteca_animale as b_animale

def test_culoare_urs():
    cul = b_animale.culoare_urs()
    if cul == 'brun':
        assert True
    else:
        assert False
def test_hrana_urs():
    inf = b_animale.hrana_urs()
    if inf == 'omnivor':
        assert True
    else:
        assert False

def test_invelisul_corpului_urs():
    inf = b_animale.invelisul_corpului_urs()
    if inf == 'blana':
        assert True
    else:
        assert False
