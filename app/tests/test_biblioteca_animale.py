import lib.biblioteca_animale as banimale
     
def test_culoare_iepure():
    cul = banimale.culoare_iepure()
    if cul == "bej" : 
        assert True
    else: 
        assert False
        

def test_hrana_iepure():
    cul = banimale.hrana_iepure()
    if cul == "ierbivor" :
        assert True
    else: 
        assert False

def test_invelis_iepure():
    cul = banimale.invelis_iepure()
    if cul == "blana" :
        assert True
    else: 
        assert False
