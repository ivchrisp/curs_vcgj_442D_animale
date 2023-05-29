from flask import Flask
import lib.biblioteca_animale
app=Flask(__name__)
print('442D_animale')

'''
 ------------------------------------
    NELU Alexandru-George  - broasca
 ------------------------------------
'''

@app.route("/broasca", methods=['GET'])
def obtine_broasca():
    ret = "<h1>broasca:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_broasca()
    ret += "<br>"

    ret += "<b>hrana: </b>"
    ret += lib.biblioteca_animale.hrana_broasca()
    ret += "<br>"

    ret += "<b>invelisul_corpului: </b>"
    ret += lib.biblioteca_animale.invelisul_corpului_broasca()
    ret += "<br>"

    print("DBG: apel obtine_broasca")
    return ret

@app.route("/broasca/culoare", methods=['GET'])
def obtine_culoare_broasca():
    ret = ""
    ret += lib.biblioteca_animale.culoare_broasca()
    return ret

@app.route("/broasca/hrana", methods=['GET'])
def obtine_hrana_broasca():
    ret = ""
    ret += lib.biblioteca_animale.hrana_broasca()
    return ret

@app.route("/broasca/invelisul_corpului", methods=['GET'])
def obtine_invelisul_corpului_broasca():
    ret = ""
    ret += lib.biblioteca_animale.invelisul_corpului_broasca()
    return ret

app.run(host = "127.0.0.1", port = 5002)

