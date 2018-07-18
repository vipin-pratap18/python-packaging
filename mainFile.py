from models import Mammals, Birds, Vehicle, Person
from pymongo import MongoClient
import pprint

'''import mysql.connector as my'''
'''from models import Birds
from models import Vehicle
from models import Person'''

mymammal = Mammals()
mybird = Birds()

mymammal.printmembers()
mybird.printmembers()

one = 1
two = 2
some_number = 10000
anydecimal = 10.23
isTrue = True
isFalse = False
someString = "This is the hello world string"

print(one)
print(two)
print(one + two)
print(anydecimal)
print(anydecimal + two)

if isTrue:
    print("This is the True value")

if isFalse:
    print("This is the False from if")
else:
    print("This is False from else")


if one > two :
    print("1 is greater than 2")
elif one == two:
    print("1 is equals 2")
else:
    print("1 is not greater than 2")


num = 1
while num <= 10:
    print("This is number %s" %num)
    num += 1

for i in range(1, 11):
    print(i)

"""Collections"""

'''List'''

my_integers = [1, 2, 3, 4, 5]
print(my_integers[0])
print(my_integers[4])

my_strings = ["vipin", "kumar"]
print(my_strings[0])
print(my_strings[1])
my_strings.append("singh")
my_strings.append("giuguiy")
print(my_strings[2])
print(my_strings[3])

'''Dictionary'''
my_dictionary = {"key1" : "value1",
                 "key2" : "value2",
                 "key3" : "value3"}

print(my_dictionary)
print(my_dictionary["key2"])

my_dictionary["key4"] = 67
print(my_dictionary)
print(my_dictionary["key4"])

for num in my_integers:
    print(num)

for str in my_strings:
    print(str)

for key in my_dictionary:
    print("Dictionary Value %s" %my_dictionary[key])

for key, value in my_dictionary.items():
    print("Key %s, Value %s" %(key, value))


car = Vehicle(4, "Car Tank", 4, 120)

print(car.number_of_wheels)
car.set_number_of_wheels(10)
print(car.number_of_wheels)
print(car.type_of_tanks)
car.makenoise()


person = Person("Ram", 20, "UP")
print(person.name)
print(person.age)
print(person.country)
'''print(person._state)'''
'''print(person.get_state())'''
print(person.get_double_age())



'''db = my.connect(host="127.0.0.1",
                user="root",
                passwd="",
                db="world"
                )

print(db)'''

client = MongoClient()
db = client.truck_geo
truck_journey = db.truck_journey
journey1 = truck_journey.find_one({"truckId" : "10"})
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(journey1)
