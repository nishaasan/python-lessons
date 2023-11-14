def add(x,y):
  return (x+y)

def sub(x,y):
  return (x-y)

def multi(x,y):
  return (x*y)

def div(x,y):
  return (x/y)

dict1={
    "+":add,
    "-":sub,
    "X":multi,
    "/":div
}
for sym in dict1:
    print(sym)

ops=input("pick an symbol: ")
num1=int(input("enter  number1: "))#5
num2=int(input("enter number 2"))
print(f"{num1} {ops} {num2}={dict1[ops](num1,num2)}")


