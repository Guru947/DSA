def prime(n):
    c = 0
    for i in range(2, n // 2):
        if n % i == 0:
            c += 1
            break
    if c == 0:
        print("prime num")
    else:
        print("not prime")

n = int(input("enter the number for prime r not: "))
prime(n)
