from flask import Flask, jsonify, request
app = Flask(__name__)
hobbies = []
drinks = []


@app.route('/')
def index():
    return "Hello World"

@app.route('/hobbies')
def get_hobbies():
    return jsonify({"hobbies": hobbies})

@app.route('/drinks')
def get_drinks():
    return jsonify({"drinks": drinks})


@app.route('/add_hobby')
def add_hobby():
    new_hobby = request.args.get('hobby'.lower())
    drink = request.args.get('drink'.lower())
    if new_hobby in hobbies:
        return jsonify({"message": "Hobby already exists"})
    hobbies.append(new_hobby)    
    if drink in drinks:
        return jsonify({"message": "Drink already exists"})
    drinks.append(drink)
    return jsonify({"message": "hobbies and drinks added successfully"})
    


@app.route('/remove_hobby_drink')
def remove_hobby_drink():
    hobby = request.args.get('hobby'.lower())
    drink = request.args.get('drink'.lower())
    hobby_exists = hobby in hobbies
    drink_exists = drink in drinks
    if hobby_exists:
        hobbies.remove(hobby)
    if drink_exists:
        drinks.remove(drink)
    return jsonify({"message": "Hobby and Drink removed", "hobby": hobby, "drink": drink})



@app.route('/search_hobby_drink')
def search_hobby_drink():
    hobby = request.args.get('hobby'.lower())
    drink = request.args.get('drink'.lower())
    hobby_exists = hobby in hobbies
    drink_exists = drink in drinks
    if hobby_exists and drink_exists:
        return jsonify({"message": "Hobby and Drink exist", "hobby": hobby, "drink": drink})
    elif hobby_exists:
        return jsonify({"message": "Hobby exists", "hobby": hobby})
    elif drink_exists:
        return jsonify({"message": "Drink exists", "drink": drink})
    return jsonify({"message": "Hobby and Drink do not exist", "hobby": hobby, "drink": drink})

app.run(debug=True)