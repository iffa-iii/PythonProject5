def replace(str1):
    str2=""
    for i in str1:
        if i not in "aeiouAEIOU" :
            str2+=i

        else:
            str2+="*"



    return str2



str1=input("enter a string: ")
r=replace(str1)
print(r)