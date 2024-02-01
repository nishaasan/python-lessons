from flask import Flask, request, jsonify
from model import Pet

app = Flask(__name__)

# In-memory data store for pets
pets_data = [Pet(id=1, name="Fluffy"), Pet(id=2, name="Buddy")]

# Define a simplified Pet schema using Marshmallow
class PetSchema:
    def __init__(self, pet):
        self.id = pet.id
        self.name = pet.name

# Create a route for listing all pets
@app.route("/pets", methods=["GET"])
def list_pets():
    return jsonify({"pets": [PetSchema(pet).__dict__ for pet in pets_data]})

# Create a route for creating a new pet
@app.route("/pets", methods=["POST"])
def create_pet():
    new_pet_data = request.get_json()
    new_pet_obj = Pet(id=len(pets_data) + 1, name=new_pet_data["name"])
    pets_data.append(new_pet_obj)
    return jsonify(PetSchema(new_pet_obj).__dict__), 201

if __name__ == "__main__":
    app.run(debug=True)
