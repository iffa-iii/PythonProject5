#CALCULATOR USING FUNCTIONS:
def calculator(a,b,n):
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


print("1:ADDITION,2:SUBTRACTION , 3:MULTIPLY, 4:DIVISION")
n= int(input(""))
val1=int(input("enter value 1: "))
val2=int(input("enter value 2: "))
final=calculator(val1,val2,n)
print(f"Result:{final}")