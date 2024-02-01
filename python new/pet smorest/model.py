class Pet:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }
        
# pet1=Pet(1,"fluffy")
# print(pet1.to_dict())
    