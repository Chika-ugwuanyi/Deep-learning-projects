import random

print('ROCK PAPER SCISSIOR GAME! \n' + 
        'Game Rules \n' +
        'Rock vs Paper --> Paper wins \n' +
        'Rock vs Scissior --> Rock wins \n' +
        'Paper vs Scissor --> Scissor wins \n')

while True:
    print('Enter your choice: \n 1-Rock \n 2-Paper \n 3-Scissor')

    choice=int(input('Enter you choice: '))

    while choice>3 or choice<1:
        choice=int(input('Enter a valid choice please: '))
        
    if choice==1:
            choice_name='Rock'
    elif choice==2:
            choice_name='Paper'
    else:
            choice_name='Scissor'
    
    print('User choice is: ', choice_name)
    print('Now its computers turn!')

    comp_choice=random.randint(1,3)
    while comp_choice== choice:
        comp_choice=random.randint(1,3)

    if comp_choice==1:
        comp_choice_name='Rock'
    elif comp_choice==2:
        comp_choice_name='Paper'
    else:
        comp_choice_name='Scissor'
    print("Computer choice is: ",comp_choice_name)
    print(choice_name,' VS ',comp_choice_name)

    
    if choice==comp_choice:
        print('Draw', end='')
        result='Draw'
    
    if (choice==1 and comp_choice==2):
        print('Paper wins: ',end='')
        result='Paper'
    elif(choice==2 and comp_choice==1):
        print('Paper wins:', end='')
        result='Paper'

    if (choice==1 and comp_choice==3):
        print('Rock wins: ',end= "")
        result='Rock'
    elif (choice==3 and comp_choice==1):
        print('Rock wins: ',end= "")
        result='Rock'

    if (choice==2 and comp_choice==3):
        print('Scissors wins: ',end="")
        result='Scissor'
    elif (choice==3 and comp_choice==2):
        print('Scissors wins: ',end="")
        result='Scissor'
    
    if result == 'Draw':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")

    else:
        print("<== Computer wins ==>")

    answer = input('Do you want to play again? (Y/N): ')
    if answer =='n':
        print("Thanks for playing")
        break
        
    else:
        continue

# Binary search

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Take array input from user
arr = list(map(int, input("Enter space separated integers: ").split()))

# Ask for index value to search
target = int(input("Enter the value to search: "))

# Call binary search function
result = binary_search(arr, target)

# Check if result is valid
if result != -1:
    print(f"Target value {target} found at index {result}.")
else:
    print(f"Target value {target} not found in the array.")


# Send email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# email information
sender_email = "your_email@example.com"
sender_password = "your_email_password"
recipient_email = "recipient_email@example.com"
email_subject = "Subject line of your email"
email_body = "Body of your email."

# create a message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = email_subject
message.attach(MIMEText(email_body, 'plain'))

# create an SMTP object and send the message
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()
smtp_object.login(sender_email, sender_password)
smtp_object.sendmail(sender_email, recipient_email, message.as_string())
smtp_object.quit()

# Zodiac sign

import datetime
import csv
import pandas

Dictionary1={}
def takeUserDay():
    try:
        day =int(input('Enter day: '))

        if day != str:
            if day <= 0 or day > 31:
                print('Enter a valid day!!! ')
                return takeUserDay()
            
            else:
                return day
    except:
        print('ERROR: Only Numbers are accepted!')
        return takeUserDay()




def takeUserMonth():
    month = input('Enter month: ')
    if month == 'January' or month == '1' or month == 'Jan' or month == 'january' or month == 'jan' or month == '01':
        monthNumber = 1
        return monthNumber
    elif month=='February' or month == '2' or month == 'Feb' or month =='february' or month =='feb' or month =='02' :
        monthNumber = 2
        return monthNumber
    elif month=='March' or month =='3' or month =='Mar' or month =='march' or month =='mar' or month =='03':
        monthNumber = 3
        return monthNumber
    elif month=='April' or month =='4' or month =='Apr' or month =='april' or month =='apr' or month =='04':
        monthNumber = 4
        return monthNumber
    elif month=='May' or month =='5' or month =='may' or month =='05':
        monthNumber = 5
        return monthNumber
    elif month=='June' or month =='6' or month =='june' or month =='06':
        monthNumber = 6
        return monthNumber
    elif month=='July' or month =='7' or month =='july' or month =='07':
        monthNumber = 7
        return monthNumber
    elif month=='August' or month =='8' or month =='Aug' or month =='august' or month =='aug' or month =='08':
        monthNumber = 8
        return monthNumber
    elif month=='September' or month =='9' or month =='Sept' or month =='september' or month =='sept' or month =='09':
        monthNumber = 9
        return monthNumber
    elif month=='October' or month =='10' or month =='Oct' or month =='october' or month =='oct':
        monthNumber = 10
        return monthNumber
    elif month=='November' or month =='11' or month =='Nov' or month =='november' or month =='nov':
        monthNumber = 11
        return monthNumber
    elif month=='December' or month =='12' or month =='Dec' or month =='december' or month =='dec':
        monthNumber = 12
        return monthNumber
    else:
        print('ERROR: Enter a valid month ')
        return takeUserMonth()



def takeUserYear():

    try:

        year = int(input('Enter year: '))
        
        if year != str:
            if year <= 0:
                print('ERROR:  ')
                return takeUserYear()
            elif year%4 == 0:
                print('Leap year!')
                return year
            else:
                return year
    except:
        print('ERROR: Enter Numerical Value Only')
        return takeUserYear()
    



def calculateSign(day,month):
      
    if month == 12:
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
    elif month == 1:
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
    elif month == 2:
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'
    elif month == 3:
        astro_sign = 'Pisces' if (day < 21) else 'aries'
    elif month == 4:
        astro_sign = 'Aries' if (day < 20) else 'taurus'
    elif month == 5:
        astro_sign = 'Taurus' if (day < 21) else 'gemini'
    elif month == 6:
        astro_sign = 'Gemini' if (day < 21) else 'cancer'
    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'leo'
    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'virgo'
    elif month == 9:
        astro_sign = 'Virgo' if (day < 23) else 'libra'
    elif month == 10:
        astro_sign = 'Libra' if (day < 23) else 'scorpio'
    elif month == 11:
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
        
    return astro_sign

def takeDate(year,month,day):
    date1=datetime.date(year,month,day)
    print('DOB: ',date1)
    return date1




def repeatQuestion():
    Finder=input('Do you want to find any other Zodiac sign(yes/no): ')
    if Finder =='yes':
        return True
    else:
        return False


def UserInput(count):
    
    userName= input('Enter the name of the user: ')
    userYear = takeUserYear()
    userMonth = takeUserMonth()
    userDate = takeUserDay()
    fullDate = takeDate(userYear,userMonth,userDate)
    yourSign = calculateSign(userDate, userMonth)
    print(userName, "your Zodiac sign is :",yourSign)
    Dictionary1[count] = { 'FullName' : '', 'DateOfBirth' : '', 'ZodiacSign' : '' }
    Dictionary1[count]['FullName'] = userName
    Dictionary1[count]['DateOfBirth'] = str(fullDate)
    Dictionary1[count]['ZodiacSign'] = yourSign
    
    
    print(Dictionary1[count])
    
def SavetoPandas():
    pass

if __name__=='__main__':
    Repeat = True
    Count = 1
    while Repeat == True:
        UserInput(Count)
        Count +=1
        Repeat = repeatQuestion()
    df = pandas.DataFrame(data=Dictionary1)
    fileName = input('PLease enter file Name:   ')
    savedData = df.to_csv(fileName+'.csv', index = True)
    print(df)

# change multiple file name stored in computer 

import os

path = input("Enter path: ")

print(path)

print(os.listdir(path)) #After writing/pasting your path DON'T FORGET to put '/' after the directory.

def main():
    i=1
    for filename in os.listdir(path):
        new_name = path + str(i) + '.jpg' #write the suitable file extension at the end as per your needs.
        old_name = path + filename
        os.rename(old_name,new_name)
        i+=1

main()