def biggest (a,b,c):
    if(a>=b and a>=c):
        return a
    if(b>=a and b>=c):
        return b
    if(c>=a and c>=b):
        return c


print (biggest(3,6,8))


def big (a,b,c):
    if(a>=b):
        if(a>=c):
            return a
        else:
            return c
    else:
        if(b>=c):
            return b
        else:
            return c

print(big(3,6,8))