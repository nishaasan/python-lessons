band = {
    "name": "John",
    "course": "Python",
    "age":17,
  

}
#Dictionary methods and access the members

print(band)
print(type(band))
print(len(band))
print(band["age"])
print(band.get("name"))
print(band.values())

band2 = dict(things="Plant", nonthings="Chair")
print(band2.items())

# # list all keys
# print(band.keys())

# # list all values
# print(band.values())

#verify a key exists
print("things" in band2)
print("triangle" in band2)

# Change values
band2["Animals"] = "Cat"
band2.update({"Fruits": "Apple"})
print(band2)

# # print(band2)

print(band2.pop("Animals"))
print(band2)

print(band2.popitem()) # tuple
print(band2)

band3 =band # create a reference
print(band3)


band2 = band.copy()
print(band2)
