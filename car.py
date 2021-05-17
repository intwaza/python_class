class Car:
    def __init__(self,make,color):
        self.make= make
        self.color=color
    def start(self):
        return f"I am starting my car which has color of {self.color}"
    def speed(self):
        return f"My car of {self.make} has 400speed/km"