class Person:
    description = 'This is a human'

Person.description




class Person:
    max_count = 123

[attribute for attribute in dir(Person) if not attribute.startswith('__')]
['max_count']