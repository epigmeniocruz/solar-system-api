from flask import Blueprint, jsonify, request
from app import db
from app.models.planets import Planet
from app.routes_helper import get_one_obj_or_abort

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        size=request_body["size"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return {"id": new_planet.id}, 201

@planet_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
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


@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_bike(planet_id):

    chosen_planet = get_one_obj_or_abort(Planet, planet_id)

    planet_dict = chosen_planet.to_dict()

    return jsonify(planet_dict), 200


@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet_with_new_vals(planet_id):

    chosen_planet = get_one_obj_or_abort(Planet, planet_id)

    request_body = request.get_json()

    if "name" not in request_body or \
        "description" not in request_body or \
        "size" not in request_body:
            return jsonify({"message":"Request must include name, description, and size."}), 400

    chosen_planet.name = request_body["name"]
    chosen_planet.description = request_body["description"]
    chosen_planet.size= request_body["size"]

    db.session.commit()

    return jsonify({f"message": f"Successfully replaced planet with id `{planet_id}`"}), 200
