class Person:
    def __init__(self):
        self.address = id(self)

alex = Person()
#object
id(alex) == alex.address
#True