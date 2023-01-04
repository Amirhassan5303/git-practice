my_list2 = ['Amirhassan', 'Ali', 'Amin', 'Taha']
my_list3 = ['Abbas', 'Fatemeh']

class Human:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f'The person name is {self.fname}'
         