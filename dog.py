class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def sit(self):
        return f"A dog whose name is {self.name} is sitting"
    def bark(self):
        return f"A dog whose name is {self.name} and have {self.color} color"