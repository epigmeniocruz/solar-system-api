from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    size = db.Column(db.Integer)

    def to_dict(self):
        planet_dict = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "size": self.size}
        
        return planet_dict

    @classmethod
    def from_dict(cls, planet_dict):
        if "name" in planet_dict and "description" in planet_dict and "size" in planet_dict:
            new_obj = cls(name=planet_dict["name"], description=planet_dict["description"], size=planet_dict["size"])
            return new_obj
