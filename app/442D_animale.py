from flask import Flask
import lib.biblioteca_animale

app = Flask(__name__)
print('442D_animale')

'''
------------------------------------
MihaiGeorgeElian - rata
------------------------------------
'''

@app.route("/rata", methods=['GET'])
def obtine_rata():
    ret = "<h1>rata:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_rata()
    ret += "<br>"
    ret += "<b>hrana: </b>"
    ret += lib.biblioteca_animale.hrana_rata()
    ret += "<br>"
    ret += "<b>invelisul_corpului: </b>"
    ret += lib.biblioteca_animale.invelisul_corpului_rata()
    ret += "<br>"
    print("DBG: apel obtine_rata")
    return ret

@app.route("/rata/culoare", methods=['GET'])
def obtine_culoare_rata():
    ret = ""
    ret += lib.biblioteca_animale.culoare_rata()
    return ret

@app.route("/rata/hrana", methods=['GET'])
def obtine_hrana_rata():
    ret = ""
    ret += lib.biblioteca_animale.hrana_rata()
    return ret

@app.route("/rata/invelisul_corpului", methods=['GET'])
def obtine_invelisul_corpului_rata():
    ret = ""
    ret += lib.biblioteca_animale.invelisul_corpului_rata()
    return ret

app.run(host="127.0.0.1", port=5002)
