# Tuples
#Tuples are immutable
#tules can be duplicated

mytuple = tuple(('Tom', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)
print(anothertuple)


print(anothertuple.count(2))