number=int(input("enter a number: "))
for i in range(2,number):
    if (number%i==0):
      print(number,"is a not prime ")
      break
else:
  print(number,"is prime")