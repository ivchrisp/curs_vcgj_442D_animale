@app.route("/hamster", methods=['GET'])  # Defines a route for GET requests to "/hamster"
def obtine_hamster():  # Defines a function that will be called when the route is accessed
    ret = "<h1>hamster:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_hamster()  # Calls a function from the biblioteca_animale library
    ret += "<br>"

    ret += "<b>hrana: </b>"
    ret += lib.biblioteca_animale.hrana_hamster()  # Calls a function from the biblioteca_animale library
    ret += "<br>"

    ret += "<b>invelisul_corpului: </b>"
    ret += lib.biblioteca_animale.invelisul_corpului_hamster()  # Calls a function from the biblioteca_animale library
    ret += "<br>"

    print("DBG: apel obtine_hamster")  # Prints a debug message
    return ret  # Returns the built HTML string

@app.route("/hamster/culoare", methods=['GET'])  # Defines a route for GET requests to "/hamster/culoare"
def obtine_culoare_hamster():  # Defines a function that will be called when the route is accessed
    ret = ""
    ret += lib.biblioteca_animale.culoare_hamster()  # Calls a function from the biblioteca_animale library
    return ret  # Returns the result of the function

# The following two functions are similar to the one above, but for different routes
@app.route("/hamster/hrana", methods=['GET'])
def obtine_hrana_hamster():
    ret = ""
    ret += lib.biblioteca_animale.hrana_hamster()
    return ret

@app.route("/hamster/invelisul_corpului", methods=['GET'])
def obtine_invelisul_corpului_hamster():
    ret = ""
    ret += lib.biblioteca_animale.invelisul_corpului_hamster()
    return ret
