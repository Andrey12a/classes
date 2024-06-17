class Cat:
    def info(self):
        print(f'I am a cat.')

    def make_sound(self):
        print('Meow')


class Dog:
    def info(self):
        print(f'I am dog')

    def make_sound(self):
        print('Wow')


c = Cat()
d = Dog()
for animal in (c, d):
    animal.make_sound()
    animal.info()
    animal.make_sound()
Meow
I am cat
Meow
Wow
I am dog
Wow