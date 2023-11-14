users=[(0,"John","password"),
   (1,"Bob","pas123"),
   (2,"Jane","Bob123")]
# dict2={x:x*x for x in list1}
# print(dict2)
new_dict={user[1]:user for user in users}
print(new_dict)

user_input=input("enter ur username")
pwd_input=input("enter ur password")
_,username,password=new_dict[user_input]
print(_,username,password)
if pwd_input==password:
    print("ur details are correct")
else:
    print("details are wrong")