from flask import Blueprint


class Planet:
    def __init__(self, id, name, description, has_moons=True):
        self.id = id
        self.name = name
        self.description = description
        self.has_moons = has_moons

planets = [
    Planet(1, "Earth", "Has Humans"),
    Planet(2, "Mars", "No Humans"),
    Planet(3, "Neptune", "No Humans"),
    Planet(4, "Saturn", "No Humans"),
    Planet(5, "Venus", "No Humans"),
    Planet(6, "Uranus", "No Humans"),
    Planet(7, "Mercury", "No Humans"),
    Planet(8, "Jupiter", "No Humans"),
] 