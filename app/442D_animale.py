from flask import Flask
import lib.biblioteca_animale
app=Flask(__name__)
print('442D_animale')

'''
 ------------------------------------
    Alexandru Ion - ornitorinc
 ------------------------------------
'''

@app.route("/ornitorinc", methods=['GET'])
def obtine_ornitorinc():
    ret = "<h1>ornitorinc:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_ornitorinc()
    ret += "<br>"

    ret += "<b>hrana: </b>"
    ret += lib.biblioteca_animale.hrana_ornitorinc()
    ret += "<br>"

    ret += "<b>invelisul_corpului: </b>"
    ret += lib.biblioteca_animale.invelisul_corpului_ornitorinc()
    ret += "<br>"

    print("DBG: apel obtine_ornitorinc")
    return ret

@app.route("/ornitorinc/culoare", methods=['GET'])
def obtine_culoare_ornitorinc():
    ret = ""
    ret += lib.biblioteca_animale.culoare_ornitorinc()
    return ret

@app.route("/ornitorinc/hrana", methods=['GET'])
def obtine_hrana_ornitorinc():
    ret = ""
    ret += lib.biblioteca_animale.hrana_ornitorinc()
    return ret

@app.route("/ornitorinc/invelisul_corpului", methods=['GET'])
def obtine_invelisul_corpului_ornitorinc():
    ret = ""
    ret += lib.biblioteca_animale.invelisul_corpului_ornitorinc()
    return ret

app.run(host = "127.0.0.1", port = 5002)
