def union (list1,list2):
   for e in list2:
      if(e not in list1):
          list1.append(e)
   return list1
print(union([1,2],[2,3]))

