from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size

planets = [
    Planet(1, "Auberon", "rocky", 10000),
    Planet(2, "Jerica", "icy", 20000),
    Planet(3, "Nancy", "hot", 5000),
    Planet(4, "Goeun", "sandy", 30000),
]

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["GET"])
def get_all_planets():
    response = []
    for planet in planets:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "size": planet.size
            }
        response.append(planet_dict)
    return jsonify(response), 200

# single planet 

@planet_bp.route("/<planet_id>", methods=["GET"])

def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        response = f"Invalid planet ID {planet_id}. ID must be an integer"
        return jsonify(response), 400

    for planet in planets:
        if planet.id == planet_id:
            planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "size": planet.size
            }
            return jsonify(planet_dict), 200
 
    response_message = f"Planet ID {planet_id} not found."
    return jsonify(response_message), 404



