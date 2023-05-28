import lib.biblioteca_animale as b_animal

def test_culoare_lenes():
    col = b_animal.culoare_lenes()
    if col == 'maro':
        assert True
    else:
        assert False

def test_hrana_lenes():
    food = b_animal.hrana_lenes()
    if food == 'ierbivor':
        assert True
    else:
        assert False

def test_invelisul_corpului_lenes():
    inv = b_animal.invelisul_corpului_lenes()
    if inv == 'blana':
        assert True
    else:
        assert False