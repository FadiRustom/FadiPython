# قسم قائمة حسب عدد حروف عناصرها
jour = ['dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi']
a=b=0
j1=[]
j2=[]
while a<7:
    #loop
    b=len(jour[a])
    if b>=6:
	    j1.append(jour[a])
	    print(a,'j1',jour[a])
    else:
	    j2.append(jour[a])
	    print(a,'j2',jour[a])
    a=a+1
print(">=6: ",j1,end="\n")
print("<6: ",j2,end="\n")
#end
# برنامج الأشهر بالقائمة
t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2=['Jan','Feb','Mar','Apr','Mai','Jun','Jul','Aoq','Sep','Oct','Dec']
a=b=0
t3=[]
while a<12: #Error?
    t3.append(t2[a])
    a=a+1
    t3.append(t1[b])
    b=b+1
print(t3,'\n')
#end
