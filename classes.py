class StringAble():
    def __init__(self, sName = "Biff"):
        self.sTest = "Hello. I'm " + sName
    def __str__(self):
        return str(vars(self)) 