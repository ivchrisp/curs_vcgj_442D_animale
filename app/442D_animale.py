from flask import Flask
import lib.biblioteca_animale
app=Flask(__name__)
print('442D_animale')

'''
 ------------------------------------
    #21  Mihailescu THEODOR
 ------------------------------------
'''

@app.route("/urs", methods=['GET'])
def obtine_urs():
    ret = "<h1>urs:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_urs()
    ret += "<br>"
    ret += "<b>hrana: </b>"
    ret += lib.biblioteca_animale.hrana_urs()
    ret += "<br>"

    ret += "<b>invelisul_corpului: </b>"
    ret += lib.biblioteca_animale.invelisul_corpului_urs()
    ret += "<br>"

    print("DBG: apel obtine_urs")
    return ret

@app.route("/urs/culoare", methods=['GET'])
def obtine_culoare_urs():
    ret = ""
    ret += lib.biblioteca_animale.culoare_urs()
    return ret

@app.route("/urs/hrana", methods=['GET'])
def obtine_hrana_urs():
    ret = ""
    ret += lib.biblioteca_animale.hrana_urs()
    return ret
app.run(host = "127.0.0.1", port = 5002)
