def biggest (a,b,c):
    if(a>=b and a>=c):
        return a
    if(b>=a and b>=c):
        return b
    if(c>=a and c>=b):
        return c
def min (a,b,c):
    if(a<=b and a<=c):
        return a
    if(b<=a and b<=c):
        return b
    if(c<=a and c<=b):
        return c
def set_range(a,b,c):
    x=biggest(a,b,c)
    y=min(a,b,c)

    return x-y



print (set_range(10, 4, 7))
#>>> 6  # since 10 - 4 = 6

print (set_range(1.1, 7.4, 18.7))
#>>> 17.6 # since 18.7 - 1.1 = 17.6