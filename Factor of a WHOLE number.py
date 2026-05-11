#TO FIND THE FACTORS OF A WHOLE NUMBER:

def factors(n):
    print("The factors are : ")

    for i in range(1,n+1):
        if n%i==0:
            print(i,end=' ')



val1=int(input("Enter a no.: "))
factors(val1)