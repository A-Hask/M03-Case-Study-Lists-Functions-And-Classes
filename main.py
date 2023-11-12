class Vehicle:
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def car():
    type = input("What type of vehicle is this? ")
    year = input("What year was the vehicle made? ")
    make = input("What make is the vehicle? ")
    model = input("What model is the vehicle? ")
    doors = input("Does this vehicle have 2 doors or 4 doors? ")
    roof = input("Does this vehicle have a roof feature? ")
    print("Vehicle type: " + type)
    print("Year: " + year)
    print("Make: " + make)
    print("Model: " + model)
    print("Number of doors: " + doors)
    print("Type of roof: " + roof)

car()