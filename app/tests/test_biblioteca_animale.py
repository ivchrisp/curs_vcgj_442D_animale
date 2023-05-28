'''
 ------------------------------------
    Stiuca-Mihaescu Mihnea 442D - hamster
 ------------------------------------
'''

import lib.biblioteca_animale as b_animale

def test_culoare_hamster():  # Defines a test function for culoare_hamster()
    cul = b_animale.culoare_hamster()
    if cul == 'bej':  # If the function returns 'bej', the test

 passes
        assert True
    else:  # If the function does not return 'bej', the test fails
        assert False

# The following two functions are similar to the one above, but for different tests
def test_hrana_hamster():
    inf = b_animale.hrana_hamster()
    if inf == 'ierbivor':
        assert True
    else:
        assert False

def test_invelisul_corpului_hamster():
    inf = b_animale.invelisul_corpului_hamster()
    if inf == 'blana':
        assert True
    else:
        assert False
