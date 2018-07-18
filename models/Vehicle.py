class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tanks = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    '''@property'''
    def number_of_wheels(self):
        return self.number_of_wheels

    '''@number_of_wheels.setter'''
    def set_number_of_wheels(self, wheel_number):
        self.number_of_wheels = wheel_number

    def makenoise(self):
        print("VRRROOOMMMMM")

