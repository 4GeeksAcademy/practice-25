from flask import Blueprint, jsonify, request
from src.models.animal import Animal

animal_bp = Blueprint("animals", __name__, url_prefix="/animals")

animals = []
next_id = 3

tommy = Animal(id=1, name="tommy", type="gato", age=1)
kaiser = Animal(id=2, name="kaiser", type="perro", age=2)

animals.append(tommy)
animals.append(kaiser)


def find_animal(id):
    return next((a for a in animals if a.id == id), None)


@animal_bp.route("/", methods=["GET"])
def get_animals():
    return jsonify([a.serializer() for a in animals])


@animal_bp.route("/<int:id>", methods=["GET"])
def get_animal(id):
    animal = find_animal(id)
    if animal:
        return jsonify(animal.serializer()), 200
    return jsonify({"error": "animal no encontrado"}), 400


@animal_bp.route("/", methods=["POST"])
def create_animal():
    global next_id
    data = request.get_json()
    

    if not isinstance(data.get("name"), str) or not data.get("type") or not isinstance(data.get("age"), int):
        return jsonify({"error": "datos invalidos"}), 400

    new_animal = Animal(
        id=next_id, name=data.get("name"), type=data.get("type"), age=data.get("age")
    )

    animals.append(new_animal)
    next_id += 1
    return jsonify(new_animal.serializer()), 201


@animal_bp.route("/<int:id>", methods=["PUT"])
def update_animal(id):
    data = request.get_json()
    animal = find_animal(id)
    if animal:
        animal.name = data.get("name", animal.name)
        animal.type = data.get("type", animal.type)
        animal.age = data.get("age", animal.age)
        return jsonify(animal.serializer())
    return jsonify({"error": "tu eta loco"})
        
