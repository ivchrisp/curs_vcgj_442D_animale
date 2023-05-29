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
        
        
        
        
        

def test_culoare_tigru():
    cul = banimale.culoare_tigru()
    if cul == "portocaliu" : 
        assert True
    else: 
        assert False
        

def test_hrana_tigru():
    cul = banimale.hrana_tigru()
    if cul == "carnivor" :
        assert True
    else: 
        assert False

def test_invelis_tigru():
    cul = banimale.invelis_tigru()
    if cul == "blana" :
        assert True
    else: 
        assert False
