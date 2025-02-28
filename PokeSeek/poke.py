from flask import Flask, request, render_template , jsonify
import requests

#initalize flask app
app = Flask(__name__)

#function to fectch poke data from pokeapi
def get_pokemon_data(name):
    url =f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        return None #return none if poke not found 
    
    data = response.json()

    pokemon_info ={
        "name":data["name"].capitalize(),
        "image": data["sprites"]["front_default"],
        "height": data["height"] / 10,  # Convert decimeters to meters
        "weight": data["weight"] / 10,  # Convert hectograms to kilograms
        "types": [t["type"]["name"].capitalize() for t in data["types"]],
        "abilities": [ability["ability"]["name"].capitalize() for ability in data["abilities"]],
       # "moves": [move["move"]["name"].replace("-", " ").capitalize() for move in data["moves"][:3]],  # Get first 5 moves
        "hp": data["stats"][0]["base_stat"],
        "attack": data["stats"][1]["base_stat"],
        "defense": data["stats"][2]["base_stat"],
        "speed": data["stats"][5]["base_stat"]

    }

    return pokemon_info

#function to fetch description
def get_pokemon_description(name):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{name.lower()}"
    response = requests.get(url)

    if response.status_code !=200:
        return "No description available"
    
    data = response.json()

    
    for entry in data["flavor_text_entries"]:
        if entry["language"]["name"] == "en":
            return entry["flavor_text"].replace("\n"," ").replace("\f"," ").replace("POK\u00e9MON", "Pokemon")
    
    return "No Description available"

#Api route to get poke details 
@app.route("/pokemon/<string:name>", methods=["GET"])
def get_pokemon(name):
    pokemon_data = get_pokemon_data(name)
    description = get_pokemon_description(name)

    if not pokemon_data:
        return jsonify({"error: Pokemon not found"}),404
    
    pokemon_data["description"] = description

    return jsonify(pokemon_data)

#Main route to handle requests
@app.route("/", methods=["GET", "POST"])
def index():
    pokemon = None
    error = None

    if request.method == "POST":
        name = request.form.get("pokemon_name")
        if name:
            pokemon = get_pokemon_data(name)
            if pokemon:
                pokemon["description"] = get_pokemon_description(name)
            else:
                error = "Pokémon not found! Please check the name and try again."
    return render_template("poke.html", pokemon=pokemon, error=error) #render html with poke data

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True) #run flask app