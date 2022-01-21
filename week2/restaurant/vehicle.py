class Vehicle:
    def __init__(self, max_spd, num_passengers, manufacturer):
        self.current_spd = 0
        self.max_spd = max_spd
        self.num_passengers = num_passengers
        self.manufacturer = manufacturer

    def accelerate(self, increment):
        if self.current_spd + increment <= self.max_spd:
            self.current_spd += increment
        else:
            self.current_spd = self.max_spd
        return self

    def decelerate(self, increment):
        if self.current_spd - increment >= 0:
            self.current_spd -= increment
        else:
            self.current_spd = 0
        return self
    

class Car(Vehicle):
    def __init__(self, max_spd, num_passengers, manufacturer, num_wheels, num_doors, model):
        super().__init__(max_spd, num_passengers, manufacturer)
        self.num_wheels = num_wheels
        self.num_doors = num_doors
        self.model = model

    def accelerate(self, increment):
        return super().accelerate(increment)

class Bicycle(Vehicle):
    pass

class Boat(Vehicle):
    pass

equinox = Car(100, 6, "Chevrolet", 4, 5, "Equinox")
equinox.accelerate()
print(equinox.current_spd)
equinox.accelerate(10)
print(equinox.current_spd)
