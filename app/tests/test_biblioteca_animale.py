import lib.biblioteca_animale as animal

def test_culoare_lenes():
    col = animal.culoare_ananas()
    if col == 'maro':
        assert True
    else:
        assert False

def test_hrana_lenes():
    food = animal.hrana_lenes()
    if food == 'ierbivor':
        assert True
    else:
        assert False

def test_invelisul_corpului_lenes():
    inv = animal.invelisul_corpului_lenes()
    if inv == 'blana':
        assert True
    else:
        assert False