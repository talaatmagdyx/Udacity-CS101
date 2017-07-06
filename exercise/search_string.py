def find_second (full_string , target_string):
        first = full_string.find(target_string)
        second = full_string.find(target_string,first+1)
        return second

print (find_second("Talaat","Ta"))

print (2==3)
