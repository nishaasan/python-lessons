from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app)
ma = Marshmallow(app)



# Define the Pet model
class Pet:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
pets_data = [Pet(id=1, name="Fluffy"), Pet(id=2, name="Buddy")]


# Define the PetSchema using Marshmallow
class PetSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")

pet_schema = PetSchema()
pets_schema = PetSchema(many=True)

# Resource for listing and creating pets
class PetsResource(Resource):
    def get(self):
        return {"pets": pets_schema.dump(pets_data)}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, help="Name cannot be blank.")
        args = parser.parse_args()

        new_pet_obj = Pet(id=len(pets_data) + 1, name=args["name"])
        pets_data.append(new_pet_obj)
        return pet_schema.dump(new_pet_obj), 201

# Register the PetsResource at the '/pets' endpoint
api.add_resource(PetsResource, '/pets')

if __name__ == "__main__":
    app.run(debug=True)
