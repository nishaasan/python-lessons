def multi(args):
  print(args)
  result=1
  for arg in args:
    result*=arg
  return result
  
def sum(args):
  print(args)
  result=1
  for arg in args:
    result+=arg
  return result
  
# print(sum(1,3,4,5))
def apply(*args,ops):
  if ops=="*":
    return multi(*args)
  elif ops=="+":
    return sum(*args)
  else:
    print("choose an operator")

print(apply((1,2,3,4),ops="+"))