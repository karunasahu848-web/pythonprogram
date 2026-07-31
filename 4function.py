#function- reusable block of code 
'''def hello():            #function define
    print("Hello how are u")
    print("What is your name???")

hello()  #funtion call

def addition(a,b):
    print(f"The sum of given number is {a + b}")
addition(2,43)
addition(2,4)

#parameters are the vallues you accept while 
#arguments are the valules you provide to parameters while calling the function 
#palindrome check multiple time
def palindrome(a):
    copy = a 
    rev = 0
    while a > 0 :
        rev = rev *  10 + a % 10
        a = a // 10 
    if rev == copy :
        print(f"{copy} is palindrome number")
    else :
        print(f"{copy} is not a palindrome number ")
palindrome(1221)
palindrome(122)

def add(a,b,c,d=12): #default arguments no need to give value to d , always write default values in the end
    print(a+b+c+d)

add(2,5,4)    #position argument 2->a, 5->b .... you have to provide all parameter value
add(20,d = 23,b = 32) #keyword arguments jiski value phele deni hai usko = krke likh do or same dusre wale ko bhi 


#return concept

def hello():
    return "How are you"  # return that value to calling func hello() = How are you

print(hello())'''
