#class syntax
class Book:
    material = 'paper'
    cover = 'paperback'
    all_books = []

class River:
    all_rivers=[]
    def __init__(self,name,length):
        self.name = name
        self.length = length
        River.all_rivers.append(self)
    def get_info(self):
        print("Длина {0} равна {1} км.".format(self.name,self.length))


my_book = Book()
print(my_book.material)
print(my_book.cover)
print(my_book.all_books)

volga = River('Волга',3530)
seine = River('Сена',776)
nile = River('Нил',6832)
for river in River.all_rivers:
    print(river.name)
volga.get_info()
seine.get_info()
nile.get_info()