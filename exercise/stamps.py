def stamps(n):
    x = int (n / 5)
    y = int (n % 5 / 2)
    z = int (n % 5 % 2 / 1)
    return x , y , z



print(stamps(10))