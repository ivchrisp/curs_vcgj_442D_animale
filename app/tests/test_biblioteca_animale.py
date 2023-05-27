import lib.biblioteca_animale as banimale

def test_culoare_pisica():
    cul = banimale.culoare_pisica()
    if cul == "portocaliu" : 
        assert True
    else: 
        assert False

def test_hrana_pisica():
    cul = banimale.hrana_pisica()
    if cul == "carnivor" :
        assert True
    else: 
        assert False



def test_invelis_pisica():
    cul = banimale.invelis_pisica()
    if cul == "blana" :
        assert True
    else: 
        assert False
