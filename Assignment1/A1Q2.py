num = int(input("Enter the number :"))
temp = num

d = int(num % 10)
num = num / 10

c = int(num % 10)
num = num / 10

b = int(num % 10)
num = num / 10


a = int(num)
print(a,b,c,d)
print(a*1000,b*100,c*10,d )
print(d,c,b,a)
