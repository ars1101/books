class Book():
    def __init__(self,author,name):
        self.author = author
        self.name = name


class books_sorting():
    def __init__(self,list_author,list_book):
        self.list_author = list_author
        self.list_book = list_book
    def sort_by_author(self):
        a = 0
        b = 0
        pr = []
        list_sort = []
        list1 = self.list_author
        list2 = self.list_book
        for i in range(len(list1)):
            a = list1.pop()
            b = list2.pop()
            pr.append(a)
            pr.append(b)
            list_sort.append(" - ".join(pr))
            pr.clear()
        list_sort.sort()
        return (list_sort)
    def sort_by_name(self):
        a = 0
        b = 0
        pr = []
        list_sort = []
        list1 = self.list_author
        list2 = self.list_book
        for i in range(len(list1)):
            b = list1.pop()
            a = list2.pop()
            pr.append(a)
            pr.append(b)
            list_sort.append(" - ".join(pr))
            pr.clear()
        list_sort.sort()
        return (list_sort)
    def find(self,line):
        a = 0
        b = 0
        pr = []
        list1 = self.list_author
        list2 = self.list_book
        list_filtered = []
        for i in range(len(list1)):
            b = list1.pop()
            a = list2.pop()
            pr.append(a)
            pr.append(b)
            pr2 = (" - ".join(pr))
            pr.clear()
            if (pr2.find(self.line)) != -1:
                list_filtered.append(pr2)
        return(list_filtered)


b = int(input("введите кол-во добавляемых книг:"))
c = ""
f = ""
g = []
h = []
for i in range(b):
    c = input("Название:")
    f = input("Автор")
    g.append(c)
    h.append(f)
books = books_sorting(f,c)
a = int(input("Отсортировать по автору = 1"
          "Отсортировать по названию = 2"
          "поиск по строке = 3"
          "Введите ID желаемой операции:"))
if a == 1:
    print(books.sort_by_author())
elif a == 2:
    print(books.sort_by_name())
elif a == 3:
    c = input("Строка поиска:")

