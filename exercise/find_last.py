def find_last(full_string , target_string):
    last=-1
    while True :
        pos=full_string.find(target_string,last+1)
        if(pos==-1):
            return last
        last = pos

print(find_last("talaat","r"))
