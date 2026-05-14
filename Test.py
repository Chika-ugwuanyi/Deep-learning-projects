# variable
a=2
b=3
print(a+b*3)

# variable name
first_name = "chika"
last_name = "ugwuanyi"
print(first_name + " " + last_name)
num_1 = 5
num_2 = 20
# division
result = num_2 / num_1
print(result)
print(result+11)

# remainder
rend = num_1 % num_2
print(rend)
exp = (num_1 ** num_2)
print(exp)
print("last_name\tfirst_name")

# data structure in python
# list (not immutable/ it is changable )
nums = [1,2,3]
car = ['bmw','audi','hundai']
car.append('toyota')
print(car)
car.clear()

# tuple ( immutable/ not changeable)
car_branch = ('bmw', 'audi', 'haundai')
print(car_branch)

# set (changeable does not allow duplicate values)
car_brand_set = {'bmw', 'audi', 'haundai', 'audi'}
# shows how many times an object appear in a list
car_branch = ('bmw', 'audi', 'haundai','audi')
print(car_branch.count('audi'))

# dictionary
student_details = {'name':'chika A', 'age':27, 'sex':'female'}
student_details.update({'name':'Ali M'})
print(student_details)

# slicing
car = ['bmw','audi','hundai']
print(car[0])
# print 1st-3 items
print(car[0:3])
# print first name
name = "Wahala Dawn"
print(name[0:5])
# print from 6th character to last
print(name[6:])

# print dict
student_details = {'name':'chika A', 'age':27, 'sex':'female'}
print(student_details.get('sex'))

# conditional statement
age = input("Please enter your age: ")
age_int = int(age)
if age_int >= 18:
    print("Eligible")
else:
    print("Not eligible")

# while loop
i= 1
while i<6:
    print('Ali')
    i = i+1

print('--------------------------')

# for loop
for i in range(5):
    print('Ali')

# while loop with break statement

i= 1
while i<6:
    print('Ali')
    if i == 2:
        print("Breaking loop")
        break
    i = i+1

print('--------------------------')

# for loop with continue statement
for i in range(10):
    print('Ali')
    if i == 4:
        print(f"Skipping {i}")
        continue
    print(i)

# logical operators
# AND -> execute when both are true
# OR -> when one condition is true
# NOT -> when value is not true

age = input("Please enter your ag8: ")
age = int(age)
gender = input("Please enter your gender: ")

if gender == 'male' and age > 18:
    print('Eligible')
elif gender == 'male' or age > 18:
    print('Partially Eligible')
else:
    print('Not eligible')

if not gender == 'male':
    print('Female')

# python functions
def make_smth(num1, num2):
    print(num1 + num2)

make_smth(7,9)

# return a function
def retun_fnc(num1, num2):
    result = num1 + num2
    return result
answer = retun_fnc(4,6)

print(answer)

# define function parameters
def name(first_name = 'Chika', last_name = 'Anya'):
    print(last_name + first_name)
    
name(first_name='Ali')

# function arguements
# args (variable length arguements *args)
# kwargs (variable length keyword arguements **kwargs)

def add(num1, *nums):
    print(num1)
    print(nums)

add(3, 6, 6, 7, 8)

def add_2(num1, *nums):
    result = 0
    for i in nums:
        result = result + i
    print(result)

add_2(3, 6, 6)

# kwargs
def student_data(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

student_data('chika', age=18, roll_num=230)

# lambda functs (anonymous functs)
def square(num):
    print(num*num)

square(6)
# declare smart object function
f = lambda num: num*num
result = f(5)
print(result)

f = lambda num1, num2: num1*num2
result = f(5,4)
print(result)

# modules in python
# pandas(used for analysing real life data)
# matplotlib (used for plotting and visualising data for real world)
# numpy (used to do scientific computing of variables)

# call a function from another file

from module import add
add(6,7)

# OOP (object oriented programming)
# class and instance

class Car:
    # attributes of my car class
    def __init__(self, userbrand, usermodel):
        # constructor
        # make brand private
        self.__brand = userbrand
        self.model = usermodel
    # create method of a class
    def func(self):
        return f"{self.model} {self.__brand}"
    # call private data (brand) by using get func
    def get_brand(self):
        return self.__brand
    
# polymorphysim (define fuel type)
    def fuel_type(self):
        return "Petrol or Diesel"
# instance of a class (function)
my_class = Car('Toyota', 'Corolla')
print(my_class.model)
print(my_class.func())

# in heritance in python
class ElectricCar(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.brand = brand
        self.model = model
        # encapsulae battery and make it private
        self.__batterysize = batterysize
    # polymorphysim
    def fuel_type(self):
        return "Electric charge"

my_class = Car("Toyota", "Corolla")
print(my_class.fuel_type())
        

my_e_car = ElectricCar("Tesla", "Model S", "855Kwh")
print(my_e_car.model)

# encapsulation in python (used to hide a data you would not want someone to use) make a data private
# call private data by using get func
print(my_class.func())

# exception handling
x = 4
try:
    if x > 0:
        print("Hello")
except Exception as e:
    print(e)
    print("Some error in your code")

x = 4
try:
    x/0
except ZeroDivisionError as a:
    print(a)
except Exception as e:
    print(e)
    print("Some error in your code")
finally:
    print("In final block")
