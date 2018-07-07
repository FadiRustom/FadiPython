#inheritance
class Parent():
  ''' Parent class for inheritance, in Father'''
  FATHER_NAME = "Parent"

  def __init__(self, LastName, EyeColor):
    self.LName = LastName
    self.EColor = EyeColor
    print ("Parent Constructor Called: ", self.LName)

  def ShowInfo(self):
    print("Last Name - " + self.LName)
    print("Eye Color - " + self.EColor)
   
class Child(Parent):
  def __init__(self, LastName, EyeColor, NumGame):
    Parent.__init__(self, LastName, EyeColor)
    self.num_toys = NumGame
    print ("Child Constructor Called: ", self.LName)

fadi = Parent("Rustom","Green")
print (fadi.EColor, "\n FATHER     " ,fadi.FATHER_NAME)
print
fadi.ShowInfo()
print("-------------------------")
ali = Child("Ali","blue", 3)
print (ali.EColor)
print
ali.ShowInfo()
