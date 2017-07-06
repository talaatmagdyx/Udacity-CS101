# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    if (len(list_of_numbers) == 0):
        return 0
    else:
        x=0
        while (x < len(list_of_numbers)):
            if(list_of_numbers[x+1]>=list_of_numbers[x]):
                return list_of_numbers[x+1]
            else:
                return list_of_numbers[x]
            x=x+1

print (greatest([4,23,1]))
# >>> 23
print (greatest([]))
# >>> 0


