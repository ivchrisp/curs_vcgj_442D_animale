from flask import Flask
import lib.biblioteca_animale
app=Flask(__name__)
print('442D_animale')





@app.route("/cal", methods=['GET'])  # Defines a route for GET requests to "/cal"
def obtine_cal():  # Defines a function that will be called when the route is accessed
    ret = "<h1>cal:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_cal()  # Calls a function from the biblioteca_animale library
    ret += "<br>"

    ret += "<b>hrana: </b>"
    ret += lib.biblioteca_animale.hrana_cal()  # Calls a function from the biblioteca_animale library
    ret += "<br>"

    ret += "<b>invelisul_corpului: </b>"
    ret += lib.biblioteca_animale.invelisul_corpului_cal()  # Calls a function from the biblioteca_animale library
    ret += "<br>"

    print("DBG: apel obtine_cal")  # Prints a debug message
    return ret  # Returns the built HTML string

@app.route("/cal/culoare", methods=['GET'])  # Defines a route for GET requests to "/cal/culoare"
def obtine_culoare_cal():  # Defines a function that will be called when the route is accessed
    ret = ""
    ret += lib.biblioteca_animale.culoare_cal()  # Calls a function from the biblioteca_animale library
    return ret  # Returns the result of the function

# The following two functions are similar to the one above, but for different routes
@app.route("/cal/hrana", methods=['GET'])
def obtine_hrana_cal():
    ret = ""
    ret += lib.biblioteca_animale.hrana_cal()
    return ret

@app.route("/cal/invelisul_corpului", methods=['GET'])
def obtine_invelisul_corpului_cal():
    ret = ""
    ret += lib.biblioteca_animale.invelisul_corpului_cal()
    return ret


app.run(host = "127.0.0.1", port = 5002)