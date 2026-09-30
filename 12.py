def pattern(m, n):
    for i in range(m):
        for j in range(n):
            print("*", end=" ")
        print()

m = int(input("Enter m: "))
n = int(input("Enter n: "))

pattern(m, n)