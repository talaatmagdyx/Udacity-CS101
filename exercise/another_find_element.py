def find_element (p,t):
    if t in p:

        return p.index(t)
    return -1

print (find_element([1,2,3],3))
print (find_element(['alpha','beta'],'gamma'))
