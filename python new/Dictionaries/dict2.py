def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Alex", "John", "Sara","Sam",100)


def mult_named_items(**wargs):
  print(wargs)
  print(type(wargs))


mult_named_items(first="Andrew", last="John", age=17) 