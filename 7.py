class Human:
    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек ходит')

class Doctor(Human):
    def heal(self):
        print('Доктор лечит')

d = Doctor()
d.walk()
Человек ходит
d.breathe()
Человек дышит
d.heal()
Доктор лечит



class Doctor(Hman):
    def heal(self):
        print('Доктор лечит')
    def walk(self):
        print('Доктор ходит')
