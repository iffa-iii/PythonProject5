#TO IDENTIFY THE LARGER OF THE TWO NO. SPECIFIED:

def larger(a,b):
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
print(output)