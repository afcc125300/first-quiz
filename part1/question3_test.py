class Oven:
    def __init__(self):
        self.ingredients = []
        self.output = None

    def add(self, item):
        self.ingredients.append(item)

    def freeze(self):
        # Combine ingredients at freezing temperature
        # You should define your own logic for this
        self.output = "Frozen result"

    def boil(self):
        # Combine ingredients at boiling temperature
        # You should define your own logic for this
        self.output = "Boiled result"

    def wait(self):
        # Combine ingredients with no change in temperature
        # You should define your own logic for this
        self.output = "No temperature change result"

    def get_output(self):
        return self.output

def make_oven():
    return Oven()

def alchemy_combine(oven, ingredients, temperature):
    for item in ingredients:
        oven.add(item)

    if temperature < 0:
        oven.freeze()
    elif temperature >= 100:
        oven.boil()
    else:
        oven.wait()

    return oven.get_output()
