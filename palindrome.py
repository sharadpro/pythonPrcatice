num=int(input("enter number: "))
sum=0
temp=num
while temp > 0:
    sum=(sum*10) +(temp%10)
    temp=temp//10
if sum==num:
    print("Plaindrom")
else:
    print("Not a Palindrom")
print(sum)
