class Student:
    school="AkiraChix"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        return f"Hello class, My name is {self.name}"
    def year_of_birth(self):
        return f"I was born {2021-self.age}"