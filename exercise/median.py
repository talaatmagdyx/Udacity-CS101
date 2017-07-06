def median(x, y, z):

    if (x>=y and x>=z and y>=z) or (z>=x and z>=y and y>=x):
        return y
    if (y>=x and y>=z and x >=z) or( z>=x and z>=y and x>=y):
        return x

    return z


print(median(1,3,2))