class Food:
    def __init__(self, name, calories, is_vegan):
        self.name = name
        self.cals = calories
        self.is_vegan = is_vegan
        self.seasonings = []

    def add_seasoning(self, seasoning):
        self.seasonings.append(seasoning)
        return self

class Dish(Food):
    def __init__(self, name, calories, is_vegan, is_spicy):
        super().__init__(name, calories, is_vegan)
        self.is_spicy = is_spicy

    def grill(self):
        self.name = f"Grilled {self.name}"

steak = Dish("t-bone", 1000, False, False)

print(steak.name)
steak.add_seasoning("Salt")
print(steak.seasonings)
steak.grill()
print(steak.name)