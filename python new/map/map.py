list1=[1,2,3,4,5]#list
list2=[2,3,4]
def add(n):
    return n+n
print(list(map(add,list1)))



#list comprehension
list_new=[x*x for x in list1 ]
print(list_new)
#dictionary comprehension
new_list=(lambda x:x*x,list1)
print(new_list)
print(list(map(lambda x,y:x+y,list1,list2)))

