
class Car:
    def __init__(self, passengers, make, model, max_speed = 100): #CONSTRUCTOR
        self.num_passengers = passengers
        self.make = make
        self.model = model
        self.max_speed = max_speed
        self.speed = 0
    
    def accelerate(self, increment):
        if self.speed + increment > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += increment



my_car = Car(5, "Chevy", "Equinox")
my_car.accelerate(160)
print(f"My {my_car.make} {my_car.model} is going {my_car.speed} MPH!")
