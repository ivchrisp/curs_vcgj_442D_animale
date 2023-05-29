#OANTA INGRID ELENA 442D - bursuc

from flask import Flask
import lib.biblioteca_animale
app=Flask(__name__)
print('442D_animale')

@app.route("/bursuc", methods=['GET'])  # Defines a route for GET requests to "/bursuc"
def obtine_bursuc():  # Defines a function that will be called when the route is accessed
    ret = "<h1>bursuc:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_bursuc()  # Calls a function from the biblioteca_animale library
    ret += "<br>"

    ret += "<b>hrana: </b>"
    ret += lib.biblioteca_animale.hrana_bursuc()  # Calls a function from the biblioteca_animale library
    ret += "<br>"

    ret += "<b>invelisul_corpului: </b>"
    ret += lib.biblioteca_animale.invelisul_corpului_bursuc()  # Calls a function from the biblioteca_animale library
    ret += "<br>"

    print("DBG: apel obtine_bursuc")  # Prints a debug message
    return ret  # Returns the built HTML string

@app.route("/bursuc/culoare", methods=['GET'])  # Defines a route for GET requests to "/bursuc/culoare"
def obtine_culoare_bursuc():  # Defines a function that will be called when the route is accessed
    ret = ""
    ret += lib.biblioteca_animale.culoare_bursuc()  # Calls a function from the biblioteca_animale library
    return ret  # Returns the result of the function

# The following two functions are similar to the one above, but for different routes
@app.route("/bursuc/hrana", methods=['GET'])
def obtine_hrana_bursuc():
    ret = ""
    ret += lib.biblioteca_animale.hrana_bursuc()
    return ret

@app.route("/bursuc/invelisul_corpului", methods=['GET'])
def obtine_invelisul_corpului_bursuc():
    ret = ""
    ret += lib.biblioteca_animale.invelisul_corpului_bursuc()
    return ret

app.run(host = "127.0.0.1", port = 5002)
