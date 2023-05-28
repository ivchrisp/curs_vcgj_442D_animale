import lib.biblioteca_animale as b_animale



def test_culoare_oaie ():

    cul = b_animale.culoare_oaie()

    if cul == 'alb':

        assert True

    else:

        assert False



def test_hrana_oaie():

    inf = b_animale.hrana_oaie ()

    if inf == 'ierbivor':

        assert True

    else:

        assert False



def test_invelisul_corpului_oaie():

    inf = b_animale.invelisul_corpului_oaie ()

    if inf == 'lana':

        assert True

    else:

        assert False


