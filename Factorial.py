#FACTORIAL

def factorial(n):
    for i in range(1,n+1):
        n*=i


    return n



num=int(input("Enter a no: "))
print(factorial(num))


