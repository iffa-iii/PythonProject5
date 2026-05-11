def prime_or_not(n):
    factor_count=0
    if n<=1:
        print("Not Prime")

    elif n==2:
        print("Prime")




    else:
        for i in range(3,n):
            if n%i==0:
                factor_count+=1



    if factor_count>0:
        print("Composite")

    else:
        print("Prime")

val1=int(input("Enter a no. to check whether its Prime or not: "))

prime_or_not(val1)