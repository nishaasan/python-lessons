names = ["Ram", "Sara", "John"]
#loop through Lists
for x in names:
    print(x)

#loop through Strings

for x in "Mississippi":
    print(x)

#break to exit the condition
for x in names:
    if x == "Sara":
        break
    print(x)

#continue the execution using continue

for x in names:
    if x == "Sara":
        continue
    print(x)

# for x in range(4):
#     print(x)

# for x in range(2, 4):
#     print(x)

for x in range(5, 101, 5):
    print(x)
else:
    print("Glad that\'s over!")

#nested for loop like hours and minutes

names = ["Ram", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")