def factori(Number):
    if Number==0:
        return 1
    n= Number
    while n>0:
        if n == 1:
            return n
        else :
            n *= (n-1)
            n -= 1
    return n
Num= int(input("enter Number:"))
fac = factori(Num)
print (fac)
