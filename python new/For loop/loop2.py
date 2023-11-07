#for loop

# for i in range(1,10):
#   print(i)
# print()
# for i in "python":
#   print(i)

# names = {"Name":"john","class":5,"place":"India"}
# for x in names.items():
#     print(x)

#continue and break
# list1=["John","Eva","Sara","Dave"]
# for x in list1:
#     if x == "Sara":
#         break
#     print(x)

# list1=["John","Eva","Sara","Dave"]
# for x in list1:
#     if x == "Sara":
#         continue
#     print(x)

# for x in range(5,101,5):

#   if x==50:
#     continue
#   print(x)
# else:
#   print("Glad that\'s over!")

# name=[1,2,3,4,5]
# revname=[]
# for i in name:
#   revname=[i]+revname
#   print(revname)

# name = input("enter ur name:")
# str1 = ""
# for i in name:
#   str1 = i + str1
#   print(str1)
# print(f"ur reversed name is {str1}")
# if name == str1:
#   print("ur name is a palndrome")
# else:
#   print("ur name is a palndrome")

#even nos extraction

# list2=[1,2,3,4,5,6,7,8,9,10,11,2,43,26]
# even=""
# for i in list2:
#   if i%2!=0:
#     even=even+str(i)
    
# print(even)

list2=[1,2,3,4,5,6,7,8,9,10,11,2,43,26]
even=[]
for i in list2:
  if i%2==0:
    even.append(i)
print(even)
