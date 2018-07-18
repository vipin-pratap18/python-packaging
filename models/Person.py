from models.Parent import Parent


class Person(Parent):
    country = "India"

    def __init__(self, name, age, state):
        Parent.__init__(self, name, age, state)
        '''self.name = name
        self.age = age
        self._state = state'''

    def get_state(self):
        return self._state

    def get_double_age(self):
        return self._double_age()

    def _double_age(self):
        return 2 * self.age

