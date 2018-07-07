class Time(object):
    "Time class for Heure, Minute & Seconde"
    def __init__(self, h=12, m=0, s=0):
        "Encore une nouvelle classe temporelle"
        self.heure =h
        self.minute =m
        self.seconde =s
    def show(self):
        "Time Show Function"
        print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde))
    
