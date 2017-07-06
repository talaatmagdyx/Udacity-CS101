def find_element (list , p):
    i=0
    while i <len(list):
        if(list[i]==p):
            return i
        i=i+1
    return -1

list=[1,2,3]
print(find_element(list,3))

def find_element2 (s,t):
    i=0
    for e in s :
        if(e==t):
            return i
        i=i+1
    return -1

print(find_element2([1,2,3,4],4))