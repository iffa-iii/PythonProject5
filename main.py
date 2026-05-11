#CALCULATOR USING FUNCTIONS:
'''def calculator(a,b,n):
    if n==1:
        return a+b


    elif n==2:
        return a-b


    elif n==4:
        return a/b


    elif n==3:
        return a*b

    else:
        return "Invalid choice"


print("1:ADDITION  2:SUBTRACTION  3:MULTIPLY  4:DIVISION")
print("Enter the no. corresponding to the operation to be performed ")
n= int(input(""))
val1=int(input("enter value 1: "))
val2=int(input("enter value 2: "))
final=calculator(val1,val2,n)
print(f"Result: {final}")'''


#to check whether a no. is Positive , Negative or Zero
'''def pos_neg_zero(a):
    if a < 0:
        return "Negative"
    elif a == 0:
        return "Zero"
    elif a > 0:
        return "Positive"
    else:
        return "Invalid Input"

val1 = int(input("Enter a number: "))

print(pos_neg_zero(val1))'''


#TO IDENTIFY THE LARGER OF THE TWO NO. SPECIFIED:

'''def larger(a,b):
    if a>b:
        return f"{a} is larger"

    elif a<b:
        return f"{b} is larger"

    else:
        return"Invalid Input"
print("WELCOME!\nThis is a program to compare the two numbers entered by you  ")
val1=int(input("Enter no.1: "))
val2=int(input("Enter no.2: "))
output=larger(val1,val2)
print(output)'''


#TO FIND THE VEN NUMBERS OUT OF A LIST:
'''def even(n):
    
    for i in n :
        if i %2==0:
            print(f"{i} is even")



n=eval(input("enter a list: "))

even(n)'''



