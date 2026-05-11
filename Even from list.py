# TO FIND THE VEN NUMBERS OUT OF A LIST:
def even(n):

    for i in n :
        if i %2==0:
            print(f"{i} is even")



n=eval(input("enter a list: "))

even(n)

