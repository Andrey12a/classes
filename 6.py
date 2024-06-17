class A:
    def _private(self):
        print('Это приватный метод')


class Animal:
    def _move(self):
        print('I am going')

duck = Animal()
duck._move()
I am going


class Animal:
    def __move(self):
        print('I am going')

duck = Animal()
duck.__move()
I am going


dir(duck)
['_Animal__move', '__class__']
duck._Animal__move()
I am going