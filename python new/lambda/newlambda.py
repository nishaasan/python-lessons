def add(x):
    return x+3

# print(add(5))

# add=lambda x:x+3
# print(add(5))

# print((lambda x,y:x+y)(5,3))

list1=[1,2,3,4,5]
double=[add(x) for x in list1]
# print(double)
doubled=[(lambda x:x*2)(x) for x in list1]
# print(doubled)
new_list=map(double,list1)
print(new_list)

