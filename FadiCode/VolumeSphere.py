# VolumeSphere
#مكعب عدد
def cube(num):
    n=num**3
    return n
#حجم الكرة
def vulBall(rayon):
    r=rayon
    pi=3.1416
    vul=4*pi * cube(r) /3
    return vul
#Start
r= float(input('Enter the vulem of Rayon: '))
print ('Valume of Sphere Ball vaut ',vulBall(r))
#end


#جدول الضرب في قائمة
def table(num):
	r=[]
	n=1
	while n<11:
		b=n*num
		r.append(b)
		n=n+1
	return r
#ٍStart
n=int(input('Enter the Number for Table: \n'))
print(table(n))
#end

