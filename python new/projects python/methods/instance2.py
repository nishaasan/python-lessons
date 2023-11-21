
class Store:
  def __init__(self,name):
      # You'll need 'name' as an argument to this method.
      # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
      self.name=name
      self.items=[]

  def add_item(self, item, price ):
      # Create a dictionary with keys name and price, and append that to self.items.
      self.dict={'item':item,'price':price}
      self.items.append(self.dict)
      print(self.items)

  def price(self):
    print(self.items[0]["price"])
    total=(self.items[0]["price"])
    avg=sum(total)/len(total)
    print(avg)

s1=Store("jane")
s1.add_item("tea",[90,80,70])
s1.price()