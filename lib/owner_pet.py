class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type  
        if owner:
            self.owner = owner 
        else:
            self._owner = None
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, value):
        if value in Pet.PET_TYPES:
            self._pet_type = value
        else:
            raise Exception("pet_type not found")

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if isinstance(value, Owner):
            self._owner = value
        else:
            raise Exception("owner must be an instance of Owner")

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("pet must be an instance of Pet")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
