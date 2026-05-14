# Activity 1: Fizz Buzz
("""list_num_range = list(range(1, 100))
for i in list_num_range:
    if i % 3 == 0 or i % 5 == 0 or i % 15 == 0:
        print("Fizz Buzz")
    else:
        print("Cannot be divided by 3/5/15")  

# Activity 2: Swap Cases
text_to_swap = input("Please add a text to swap: ")
age_text = str(text_to_swap)
print(age_text.swapcase())

# Activity 3: Swap Numbers without 3rd variable tupple unpacking
x , y = 6, 5
print("Before swapping:", x, y)
x, y = y, x
print("After swapping:", x, y)

# Swap Numbers with 3rd variable
x = 7
y = 8
z = x # x = 7, y = 8, z = 7
x = y
y = z
print("x= ", x)
print("y= ", y)

# Activity 4: Fibonacci Series
while True:

    n = int(input("Enter the length of the Fibonacci series: ")) #check number of iterations 

    # define the first two numbers in the series
    a, b = 0, 1
    count=0
    while True:
        # check if the lenth is valid
        if n<=0:
            print("Enter positive integer!!!")
            
        # if there is only 1, return "a"
        elif n==1:
            print("Fibonnaci series upto ",n,":",a)
            
        #loop to generate the series up to n
        else:
            print("Fibonacci sequence:")
        while count < n:
            print(a)
            nth = a + b
            # update values
            a = b
            b = nth
            count += 1  
        break """)  

# Activity 5: Number Guessing Game
import random
message = "You won!"
guess_count = 0
guess_count_limit = 5
rand_numb = random.randint(1, 100)
while guess_count < guess_count_limit:
        print(f"{guess_count_limit} attempts left")
        guess_count_limit -=1
        user_num = int(input("Please choose a randon number to start the game: "))
        try:
            if user_num == rand_numb:
                print("You Won!")
                break 
            else:
                print("You Lost Try Again")
                continue
        except ValueError:
            print("Only integers are allowed")
if guess_count == guess_count_limit:
        print("You have reached maximum attampt")
print(message)

# Activity 6: Basic Calculator
class calculator:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
    def mult(self):
        return self.num_1 * self.num_2
    def divide(self):
        return self.num_1 / self.num_2
    def subtr(self):
        return self.num_1 - self.num_2
    def add(self):
        return self.num_1 + self.num_2
    
my_class = calculator(7, 5)
print(my_class.mult())
print(my_class.subtr())
 

# How can you add your define functions inside your If-else statements?
class check_exceptns:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        num1 = int(input("Input your first number for calculation: "))
        num2 = int(input("Input your second number for calculation:"))
    def mult(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1 / self.num2
    def subtr(self):
        return self.num1 - self.num2
    def add(self):
        return self.num1 + self.num2

my_class2 = check_exceptns(4,7)

print(my_class2.divide())

# another alternative
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("SELECT OPERATION")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

    choice = input("ENTER CHOICE: ")

    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("INVALID INPUT. \n Please enter a number between 1-4: ")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
    
        New_calculation = input("Do you want to do any other calculation (yes/no): ")
        if New_calculation == "no":
          break
    else:
        print("Invalid Input")