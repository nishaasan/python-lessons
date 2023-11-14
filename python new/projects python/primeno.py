num = int(input("Enter a number: "))#5

#  # define a flag variable
flag = False

if num == 1:
     print(num, "is not a prime number")
elif num > 1:
     # check for factors
     for i in range(2, num):#5/2,5/3,5/4
         if (num % i) == 0:
             # if factor is found, set flag to True
             flag = True
             # break out of loop
             break

     # check if flag is True
     if flag:
         print(num, "is not a prime number")
     else:
         print(num, "is a prime number")
