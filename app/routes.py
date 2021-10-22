from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request 


# class Planet:
#     def __init__(self, id, name, description, has_moons=True):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.has_moons = has_moons

# planets = [
#     Planet(1, "Earth", "Has Humans"),
#     Planet(2, "Mars", "No Humans"),
#     Planet(3, "Neptune", "No Humans"),
#     Planet(4, "Saturn", "No Humans"),
#     Planet(5, "Venus", "No Humans"),
#     Planet(6, "Uranus", "No Humans"),
#     Planet(7, "Mercury", "No Humans"),
#     Planet(8, "Jupiter", "No Humans"),
# ] 

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# @planets_bp.route("", methods=["GET"])
# def handle_planets():
#     #describe response for displaying all planets
#     planets_response = []
#     for planet in planets:
#         planets_response.append(
#             {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "has_moons": planet.has_moons
#             }
#         )
#     return jsonify(planets_response)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     planet_id = int(planet_id)
#     planet_response = jsonify("id not valid")
#     for planet in planets:
#         if planet.id == planet_id:
#             planet_response = {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "has_moons": planet.has_moons
#             }
#     return planet_response