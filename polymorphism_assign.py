
# Parent Class
class Vehicle:
    # Added Attributes to parent class with __init__
    def __init__(self,wheels,doors,speed):
        self.wheels = wheels
        self.doors = doors
        self.speed = speed
    
    # Add method getMotionInfo that contains a if/else statement
    def getMotionInfo(self):
        if (self.speed > 0):
            print("Vehicle is moving a speed of {}".format(self.speed))
        else:
            print("Vehicle is not moving")

# Child Class
class Car(Vehicle):
    # Add __init__() to create a new object
    def __init__(self,wheels,doors,speed):
        # super() function that makes the child class inherit the methods and props from the parent
        super().__init__(wheels,doors,speed)
        self.Make = "Ford"
        self.Model = "Mustang"
        
    
    def getMotionInfo(self):
        if (self.speed > 0):
            print("The {} {} is moving at a speed of {} mph".format(self.Make,self.Model,self.speed))
        else:
            print("The {} {} is not moving".format(self.Make,self.Model))

# Second Child Class
class Helicopter(Vehicle):
    def __init__(self,wheels,doors,speed):
        super().__init__(wheels,doors,speed)
        self.rotor_system = "Single Main Rotor"
        self.heli_type = "attack"

    def getMotionInfo(self):
         if(self.speed > 0):
             print("The {} {} helicopter is hovering at speeds of {} knots".format(self.rotor_system,self.heli_type,self.speed))
         else:
             print("The helicopter is not moving")

# Create a new Car object
x = Car(4,4,40)
# call the getMotionInfo method from the Car class
x.getMotionInfo()
# Create a Helicopter object
y = Helicopter(4,3,0)
# Call the getMotionInfo method from the Helicopter class
y.getMotionInfo()
