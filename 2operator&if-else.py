
'''name = "karuna"
age = 23
print(f"my name is {name} and my age is {age}")
print("hi my name is", name, "my age is", age)

#input
a = input("Enter your name :")
print(a)
b = int(input("what is your age :- "))
print("Your age is", b)

#Arithmatic Operatorn(+,-,/,//,*,**,%)
left->right 
() bracet, ** exponent, * / // %, + -
a = 65
b = 3
print(a - b)
print(a + b)
print(a/b) #float 12/2
print(a//b) #int 
print(a*b)
print(a**b)#power 
print(a%b)


#Comparison operator(==, >=, ,<=, <, >, !=) ans- boolean 

#Assignment operator (+=, -=, *=, /=, //=, %=, **=)
a = 10 
a = a + 12 
a += 12
print(a)
#Logical operators( and {both should be true - True}, or{atleastt one shoul be True - True}, not(True)- False)
print(not ( (5>3 and 4!=5) or (43 == 34 or 4 > 3)))

# Conditional Statement 
if not(5 == 2 or 4 !=3) : 
    print("True ")
else :
    print("condition does not satisfy ")

#take input age and tell a person can vote or not 
age = int(input("Enter your age :"))
if age >= 18 :
    print("You can vote.")
else :
    print("You can not vote.") 

# aske your mom for money if she give u 10 then buy a chocobar, if 50 then buy pakode, if 100 then buy mcd meal
money = int(input("Give money :"))
if money == 10 :
    print("Buy Chocobar")
elif money == 50 :
    print("I'll buy pakoda")
elif money == 100 :
    print("buy mcd meal")
elif money == 500 :
    print("cafe party ")
elif money == 0 :
    print("Bhukha rahungi maii")
else :
    print("I'll buy something according to money ")

#input 2 nums and print greatest between them
a = int(input("Enter first num :"))
b = int(input("Enter second num :"))
if a > b :
    print("largest number is ", a)
elif b > a :
    print("largest number is ", b)
else : 
    print("Both are equal.")

# accept gender from a person and print greeting message 
gen = input("Enter your Gender :")
if gen == "F" or gen == "f" :
    print("Hello ma'am")
elif gen == "M" or gen == "m":
    print("Hello sir")
else :
    print("Other")

# Accept an integer and check if it is an even or an odd num
a = int(input("Enter your number :"))
if a % 2 == 0 :
    print("It is an even number.")
else :
    print("Your number is odd numbers")

# Accept name and age to check if it is valid voter or not 
name = input("Enter your name :")
age = int(input("Enter your age :"))
if age >= 18 :
    print(f"Hello {name}, your age is {age} and you are a valid voter.")
else :
    print(f"Hello {name}, you can vote after {18 - age} years. ")

#Accept a year and check if it is leap year 
year = int(input("Enter any year :"))
if  year % 100 == 0 and year % 400 == 0 :
    print("It is a leap year.")
elif year % 100 != 0 and year % 4 == 0:
    print("leap year ")
else :
    print("Not a leap year")

# Accept temperature in degree C and add description
temp = int(input("Enter temperature :"))
if temp <= 0 :
    print("Freezing cold")
elif 0 < temp <= 25 :
    print("Pleasant")
else :
    print("Hot")'''

