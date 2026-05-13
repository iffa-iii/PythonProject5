def linearsearch(l1,n):

    pos=0
    for i in l1:
        if n==i:
            print(pos)

        else:
            pos+=1




l1=eval(input("enter a list :  "))
n=int(input("Enter a no.: "))

linearsearch(l1,n)


def linearsearch(l1, n):

    pos = 0
    flag = False

    for i in l1:

        if n == i:
            print("Element found at position:", pos)
            flag = True
            break

        pos += 1

    if flag == False:
        print("Element not found")


l1 = eval(input("Enter a list: "))
n = int(input("Enter a number: "))

linearsearch(l1, n)