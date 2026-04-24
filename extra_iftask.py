#create a program that checks login credentials:
#"acces granted" if email="admin@gmail.com"and password="admin@123"

#"wrong password"if email is correct but password is wrong
#"email not found" otherwise

email=input("enter email:")
password=input("enter password:")
correct_email="admin@gmail.com"
correct_password="admin123"

if email=="admin@gmail.com" and password=="admin123":
    print("Access granted")
elif email=="admin@gmail.com" and password!="admin123":
    print("wrong password")
else:
    print("Email not found")

#Q2
valid_email=input("enter valid email:")
correct_valid_email="contain '@'" and " ."
correct_valid_gmail="ends with'@gmail.com'"

if email!="contain '@' or '.' ":
    print("inavalid email")
elif email=="@gmail.com":
    print("Gmail account")
else:
    print('Other email provider')


#Q3
#write a program that checks password strength:
#"weak" if length<6
#"moderate" if length 6-10 and contains at least one digit
#"strong" if length>10 and contain contains both digits and uppercase letters

password=input("enter a password:")
if  len(password)<6:
    print("weak")
elif  len(password)<=6 and len(password)<=10 and password.isalnum():
    print("moderate")
elif len(password)>10 and password.isalnum() or password.isupper():
    print("strong")
#write a program that checks a password:
#"invalid" if it does not end with a capital letter
#"invalid"if it does not end with a number
#"valid password" otherwise
check_password=input("enter your password:")
if password[-1].isupper() and password[-1].isdigit():
    print("valid")
else:
    print("invalid")

#q5
#write a progra, that takes a number and ckecks:
#"fizz" if divisible by 3
#"buzz" if divisible by 5
#"fizzbuzz"if divisible by both
#otherwise print the number
number=int(input("enter a number:"))
if number%3==0 and number%5==0:
    print("fizzbuzz")
elif number%3==0:
    print("fizz")
elif number%5==0:
    print("buzz")
else:
    print("number")



#q6
#create a program that takes a score and prints a grade:
#A(>=80)
#B(70-79)
#C(60-69)
#D(50-59)
#F(<50)

marks_Score=int(input("enter marks_scored:"))
if marks_Score>=80:
    print("grade A")
elif marks_Score>=70 and marks_Score<=79:
    print("grade B")
elif marks_Score>=60 and marks_Score<=69:
    print("grade C")
elif marks_Score>=50 and marks_Score<=59:
    print("grade D")
else:
    print("grade F")


#q7
#create a program that takes two numbers and prints:
#"equal" if same
#"first is greate"
# "second is greater"
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
if num1==num2:
    print("Equal")
elif num1>num2:
    print("First is greater")
else:
 print("Second is greater")

#q8
#write a program that takes a day number(1-7)and prints:
#weekday(1-5)
#weekend(6-7)
#invalid input otherwise

day_number=int(input("enter the day:"))
if day_number>=1 and day_number<=5:
    print("weekday")
elif day_number>=6 and day_number<=7:
    print("weekend")
else:
    print("invalid input")

#create a program that takes a temperature and prints:
#"freezing" if<=0
#"cold"if 1-5
#"hot"if >30
temp=int(input("enter the temp:"))
if temp<=0:
    print("freezing")
elif temp>=1 and temp<=15:
    print("cold")
elif temp>=16 and temp <=30:
    print("warm")
else:
    print("Hot")

#q10
#create a program that takes a year and prints:
#"leap year" if divisible by 4
#"century"if divisible by 100
#"common year" otherwise

year=int(input("enter the year:"))
if year%4==0:
    print("leap year")
elif  year%100==0:
    print("century")
else:
    print("common year")
