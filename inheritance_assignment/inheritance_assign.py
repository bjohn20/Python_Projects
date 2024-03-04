
# Parent class with attributes/properties
class Nissan:
    # def __init__(self, wheels, doors, model, fuel_type,passengers)
        wheels = 0
        doors = 0
        model = ' '
        fuel_type = ' '
        passengers = 0

        # Utilizing the dunder method to attach the arguments from the parent object to the attributes to the object
        def __init__(self, wheels, doors, model, fuel_type, passengers):
                self.wheels = wheels
                self.doors = doors
                self.model = model
                self.fuel_type = fuel_type
                self.passengers = passengers

# Child class
class Altima(Nissan):
    transmission = "Automatic"
    airbags = 5

# Second child class 
class Rogue(Nissan):
        cargo_space = "36.3 to 36.5 ft"
        roof_rails = True



if __name__ == "__main__":
   New_Altima = Altima(4,4,"Altima","gasoline",5)
   print(New_Altima.transmission)
