# Criando uma Classe Estudante, que pode é abstraida do mundo real
class Student:
    def __init__(self, name, major, gpa, is_in_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_in_probation = is_in_probation
    def on_honor_hall(self):
        if self.gpa >= 9.5:
            return True
        else:
            return False