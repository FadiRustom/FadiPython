class Operator:
    def __init__(self,**kwargs):
        self.v=kwargs
    def setName(self,n):
        self.v['name']=n
    def getName(self):
        return self.v['name']
    def setCity(self,c):
        self.v['c']=c
    def getCity(self):
        return self.v['c']
    def setDegree(self,d):
        self.v['de']=d
    def getDegree(self):
        return self.v['de']
    
