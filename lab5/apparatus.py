class tv:

    def __init__(self, name, kanal = None, volym = None):
        self.kanal = kanal or 1
        self.volym = volym or 5
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

