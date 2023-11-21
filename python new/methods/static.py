type=("fiction","non-fiction")
class Books:
  name="Alice"
  type=("comic","non-comic")
  def __init__(self,book_type):
    self.name="harry Potter"
    self.type=book_type

  def __repr__(self):

    return f"<Books: \n Name:{self.name} \n Type:{self.type}>"

  @classmethod
  def hardcover(cls,name):
    return (name,Books.type[0])

  @classmethod
  def pagebook(cls,name,weight):
    return (name,Books.type[1],weight)

  @staticmethod

  def newbook():
    print("static method called")
    print(f"Name:{Books.name}\nType:{Books.type[0]}")
   
  

# print(Books.type)
# print(type)
Book1=Books("comedy")
print(Book1)
book2=Books.hardcover("HP2")
print(book2)
book3=Books.pagebook("King of Guards",100)
print(book3)
Books.newbook()