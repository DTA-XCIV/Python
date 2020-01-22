class Sort(object):
    def __init__(self, to_sort):
        self.sort = to_sort

    def sort_for_me(self):
        self.sort.sort()
        print (self.sort)
        return self.sort

wirwar = (["d", "l", "i", "w", "x"])

beestenboel = (["walvis", "konijn", "papegaai", "neushoorn", "egel"])

sorteer = Sort(wirwar)
dieren = Sort(beestenboel)

dieren.sort_for_me()
