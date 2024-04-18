# find average and assigning grade

subject1 = float(input("Enter marks: "))
subject2 = float(input("Enter marks: "))
subject3 = float(input("Enter marks: "))

Average = (subject1+subject2+subject3)/3
print("The Average marks :" ,Average)

if Average > 90:
    print ("grade A")
elif Average > 80:
    print ("grade B")
elif Average > 70:
    print ("grade C")
elif Average > 60:
    print ("grade D")
else:
    print("grade F")
