class Parent:
    def earn_money(self):
        print('Родитель зарабатывает')

class Child(Parent):
    def play(self):
        print('Ребенок играет')

c = Child()
c.play()
c.earn_money()