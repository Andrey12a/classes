class Car:
    def __init__(self, color, typ, year):
        self.color = color
        self.typ = typ
        self.year = year

    @staticmethod
    def starting_car():
        print('starting car')

    @staticmethod
    def car_is_stopped():
        print('car is stopped')

    def color_car(self):
        print(f'color: {self.color}')

    def type_car(self):
        print(f'typ: {self.typ}')

    def year_car(self):
        print(f'year: {self.year}')
