class Book():
    def __init__(self,author,name):
        self.author = author
        self.name = name


class Sorter():
    def __init__(self,spis):
        self.spis = spis
    def line(self):
        sp = []
        for i in spis:
            sp.append(f"{i.name} - {i.author}")
        return ','.join(sp)
    def sortba(self):
        spis_sort = list(sorted(self.spis, keu=lambda x: x.author))
        return self.line(spis_sort)
    def sortbn(self):
        spis_sort = list(sorted(self.spis, keu=lambda x: x.name))
        return self.line(spis_sort)
    def find(self,line):
        spis_choose = list(filter(lambda x: line.lower() in x.name.lower(), self,spis_books))
        return self.line(spis_choose)
