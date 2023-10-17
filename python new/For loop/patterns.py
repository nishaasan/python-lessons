#pattern 1

 # outer loop to handle number of rows
    # 5 rows in this case
for i in range(0,5):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
    for j in range(0, i+1):
         
        # printing stars
        print("* ",end="")
      
        # ending line after each row
    print()
print("__________________________________________________________________________________________")

#how to reverse this pattern
print("REVERSE PATTERN USING -1")
print()
for i in range(5,0,-1):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
    for j in range(i):
         
        # printing stars
        print("* ",end="")
      
        # ending line after each row
    print()