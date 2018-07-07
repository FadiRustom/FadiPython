Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from turtle import *
>>> forward(120)
>>> left(90)
>>> color('red')
>>> forward(80)
>>> reset()
>>> a=0
>>> while a<12:
	a=a+1
	forward(150)
	left(150)

	
>>> reset()
>>> a=0
>>> color('red')
>>> while a<12:
	a=a+1
	forward(150)
	left(150)

	
>>> forward(120)
>>> right(100)
>>> color('blak')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    color('blak')
  File "<string>", line 8, in color
  File "C:\Users\Fadi Rustom\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 2216, in color
    pcolor = self._colorstr(pcolor)
  File "C:\Users\Fadi Rustom\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 2696, in _colorstr
    return self.screen._colorstr(args)
  File "C:\Users\Fadi Rustom\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 1158, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: blak
>>> color('black')
>>> forward(200)
>>> right(90)
>>> forward(100)
>>> heft(150)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    heft(150)
NameError: name 'heft' is not defined
>>> left(150)
>>> foreard(100)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    foreard(100)
NameError: name 'foreard' is not defined
>>> forward(100)
>>> reset()
>>> while a<12:
	a=a+1
	forward(a*10)
	left(150)

	
>>> a=0
>>> while a<12:
	a=a+1
	forward(a*10)
	left(150)

	
>>> a=0
>>> while a<12:
	a=a+1
	forward(a*15)
	left(150)

	
>>> a=0
>>> while a<12:
	a=a+1
	color('red')
	forward(a*15)
	left(150)
	color('black')
	forward(a*10)
	right(120)

	
>>> reset()
>>> a=0
>>> while a<12:
	a=a+1
	color('red')
	forward(a*15)
	left(150)
	color('black')
	forward(a*10)
	right(120)

	
>>> reset()
>>> a=0
>>> while a<15:
	a=a+1
	color('red')
	forward(a*15)
	left(150)
	color('black')
	forward(a*10)
	right(120)

	
>>> 
