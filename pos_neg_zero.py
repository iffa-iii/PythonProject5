#to check whether a no. is Positive , Negative or Zero
def pos_neg_zero(a):
    if a < 0:
        return "Negative"
    elif a == 0:
        return "Zero"
    elif a > 0:
        return "Positive"
    else:
        return "Invalid Input"

val1 = int(input("Enter a number: "))

print(pos_neg_zero(val1))
