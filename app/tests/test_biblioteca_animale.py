import lib.biblioteca_animale as banimale

def test_culoare_caine():
    cul = banimale.culoare_caine()
    if cul == "maro" : 
        assert True
    else: 
        assert False
        

def test_hrana_caine():
    cul = banimale.hrana_caine()
    if cul == "carnivor" :
        assert True
    else: 
        assert False

def test_invelis_caine():
    cul = banimale.invelis_caine()
    if cul == "blana" :
        assert True
    else: 
        assert False
        
        
        
        
        

def test_culoare_pantera():
    cul = banimale.culoare_pantera()
    if cul == "negru" : 
        assert True
    else: 
        assert False
        

def test_hrana_pantera():
    cul = banimale.hrana_pantera()
    if cul == "carnivor" :
        assert True
    else: 
        assert False

def test_invelis_pantera():
    cul = banimale.invelis_pantera()
    if cul == "blana" :
        assert True
    else: 
        assert False
