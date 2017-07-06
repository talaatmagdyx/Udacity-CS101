def output(number, unit):
    return "{0} {1}{2}".format(number, unit, "s" if number != 1 else "")

def convert_seconds(n):
    h, remainder = divmod(int(n), 3600)
    m = remainder / 60
    return "{0}, {1}, {2}".format(output(h, "hour"), output(m, "minute"),
                                  output(n - (3600*h + 60*m), "second"))
print (convert_seconds(3661))
#>>> 1 hour, 1 minute, 1 second

print (convert_seconds(7325))
#>>> 2 hours, 2 minutes, 5 seconds

print (convert_seconds(7261.7))
#>>> 2 hours, 1 minute, 1.7 seconds