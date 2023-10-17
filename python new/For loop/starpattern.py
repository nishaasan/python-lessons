#three loops used
#first loop for rows
#second loop for spaces
#third loop to print stars
# number of spaces
n=5 #5 rows of pattern
k = n - 1
 
    # outer loop to handle number of rows
for i in range(0, n):
     
    # inner loop to handle number spaces
    # values changing acc. to requirement
    for j in range(0, k):
        print(end=" ")
     
        # decrementing k after each loop
    k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
    for j in range(0, i+1):
         
       # printing stars
        print("*", end=" ")
     
        # ending line after each row
    print()
 



