from flask import Flask
import lib.biblioteca_animale
app=Flask(__name__)
print('442D_animale')

'''
 ------------------------------------
    Bordei Rucsandra - koala
 ------------------------------------
'''

@app.route("/koala", methods=['GET'])
def obtine_koala():
    ret = "<h1>koala:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_koala()
    ret += "<br>"

    ret += "<b>hrana: </b>"
    ret += lib.biblioteca_animale.hrana_koala()
    ret += "<br>"

    ret += "<b>invelisul_corpului: </b>"
    ret += lib.biblioteca_animale.invelisul_corpului_koala()
    ret += "<br>"

    print("DBG: apel obtine_koala")
    return ret

@app.route("/koala/culoare", methods=['GET'])
def obtine_culoare_koala():
    ret = ""
    ret += lib.biblioteca_animale.culoare_koala()
    return ret

@app.route("/koala/hrana", methods=['GET'])
def obtine_hrana_koala():
    ret = ""
    ret += lib.biblioteca_animale.hrana_koala()
    return ret

@app.route("/koala/invelisul_corpului", methods=['GET'])
def obtine_invelisul_corpului_koala():
    ret = ""
    ret += lib.biblioteca_animale.invelisul_corpului_koala()
    return ret

app.run(host = "127.0.0.1", port = 5002)

