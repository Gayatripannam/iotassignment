# Q6. factorial num


def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)

num=int(input("Enter the number:"))
#print("factorial of", num ,"is ",fact(num))
print ( f"factorial of is:{fact(num)}")