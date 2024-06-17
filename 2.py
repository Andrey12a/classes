class Person:
    def __init__(self):
        self.name = 'Alex'

alex = Person()
#object
alex.name
#'Alex'
alex, andrey = Person(), Person()
#object
alex.name, andrey.name
#('Alex', 'Alex')
