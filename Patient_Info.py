class Vent():
    def __init__(self, temp, rate, breath_vol):
        self.temp = temp
        self.rate = rate
        self.breath_vol = breath_vol

class Patient(Vent):
    def __repr__(self):
        print("Patient anthropometric info. This class will add pertinent info that you can then use to call estimated needs")

    def __inti__(self, height, weight, age, gender):
    self.height = height
    self.weight = weight
    self.age = age
    self.sex = sex

