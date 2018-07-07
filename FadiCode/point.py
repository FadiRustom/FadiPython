class Point(object):
	"""docstring for Point إحداثيات نقطة"""
	def __init__(self, x, y):
		super(Point, self).__init__()
		self.x = x
		self.y = y

class Rectangle(object):
	"""docstring for Rectangle"""
	def __init__(self, ang, lar, hau):
		#super(Rectangle, self).__init__()
		self.ang = ang
		self.lar = lar
		self.hau = hau

	def trouveCentre(self):
		xc = self.ang.x + self.lar /2
		yc = self.ang.y + self.hau /2
		return Point(xc, yc)

class Carre(Rectangle):
	"""docstring for Carre= Rectangle partculier"""
	def __init__(self, coin, cote):
		#super(Carre, self).__init__()
		Rectangle.__init__(self, coin, cote, cote)
		self.cote = cote

	def surface(self):
		return self.cote **2


#-------------Main---------------
csgR=Point(40, 30)
csgC=Point(10, 25)
#Boites Rectangle
boiteR = Rectangle(csgR, 100, 50)
boiteC =Carre(csgC, 40)
#pour
cR= boiteR.trouveCentre()
cC= boiteC.trouveCentre()
#View
print ("centre du rect.:", cR.x, cR.y)
print ("centre du carre :", cC.x, cC.y)

print("surf. du carre :", end='')
print(boiteC.surface())
