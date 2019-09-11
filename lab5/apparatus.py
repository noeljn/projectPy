class tv:

    def __init__(self, name):
        self.kanal = 1
        self.volym = 5
        self.name = name

    def bytKanal(self, x):
        self.kanal = x

    def sankVolym(self):
        if self.volym != 0:   
            self.volym += -1

    def hojVolym(self):
        if self.volym != 10:
            self.volym += 1

    def getName(self):
        return self.name
    
    def getVolym(self):
        return self.volym

    def getKanal(self):
        return self.kanal

