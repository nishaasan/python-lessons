def name(**args):
  print(f"The key args are {args}")

def print_new(**args):
  name(**args)
  for key,value in args.items():
    print(f"{key}:{value}")

print_new(name="nisha",lname="rafi",age=25)