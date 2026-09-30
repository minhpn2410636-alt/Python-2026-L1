n=int(input("Enter n:"))
a=True if n>= 2 else False
for i in range(2,n):
    if n % i == 0:
        a=False
        break
if a== True:
    print("yes")
else:
    print("no")