class Application(object):
	def __init__(self):
	 	"""Constructeur de la fenêtre principale"""
		self.root = Tk()
		self.root.title('Code des couleurs')
		self.dessineResistance()#رسم المقاومة
		Label(self.root, text ="Entrez la valeur de la résistance, en ohms :").\
			grid(row =2, column =1, columnspan =3)
		Button(self.root, text ='Montrer', command =self.changeCouleurs).\
			grid(row =3, column =1)
		Button(self.root, text ='Quitter', command =self.root.quit).\
			grid(row =3, column =3)
		self.entree = Entry(self.root, width =14)
		self.entree.grid(row =3, column =2)
		# : اللوان للقيمة من 0 إلى 9
		self.cc = ['black','brown','red','orange','yellow',
					'green','blue','purple','grey','white']
		self.root.mainloop()

	def dessineResistance(self):
		"""Canevas avec un modèle de résistance à trois lignes colorées"""
		self.can = Canvas(self.root, width=250, height =100, bg ='ivory')
		self.can.grid(row =1, column =1, columnspan =3, pady =5, padx =5)
		self.can.create_line(10, 50, 240, 50, width =5) # fils
		self.can.create_rectangle(65, 30, 185, 70, fill ='light grey', width =2)
		#: (رسم ثلثة خطوط ملونة (أسود في البداية # # 26
		self.ligne =[] # تخزين الخطوط الثلثة في قائمة واحظدة
		for x in range(85,150,24):
			self.ligne.append(self.can.create_rectangle(x,30,x+12,70,
                                                        fill='black',width=0))

	def changeCouleurs(self):
		"""Affichage des couleurs correspondant à la valeur entrée"""
		self.v1ch = self.entree.get()
		#هذا السلوب يقوم بيإرجاع سلسلة واحظدة # # 35			
		try:
			v = float(self.v1ch) # تحويلها إلى قيمة رقيمة
		except:
			err = 1#خطأ: المعطيات ليست رقمية # 1
		else:
			err =0
		if err ==1 or v < 10 or v > 1e11 :
			self.signaleErreur() # المدخلت خاطفئة أو خارجة
		else:
			li =[0]* 3#قائمة من 3 رموز لعرض # 3
			logv = int(log10(v)) # الجزء الصحيح من الخوارزمية
			ordgr = 10**logv # ترتيب الحجم
			#: استخراج أول أرقام هامة # # 48
			li[0] = int(v/ordgr) # جزء صحيح
			decim = v/ordgr - li[0]# جزء حظقيقي # [ 0
			#: استخراج أول أرقام هامة # # 51
	 		li[1] = int(decim*10 +.5) # +. لتقريب بيشكل صحيح 5
			#:عدد الصفار المرتبطة بيالرقمين الكبيرين # # 53
			li[2] = logv -1
			#:تلوين الخطوط الثلثة # # 55
			for n in range(3):
				self.can.itemconfigure(self.ligne[n], fill =self.cc[li[n]])
#
	def signaleErreur(self):
		self.entree.configure(bg ='red') # تلوين خلفية
		self.root.after(1000, self.videEntree) # امسحهُ بيعد 1 ثانية

	def videEntree(self):
		self.entree.configure(bg ='white') # استعد الخلفي البيضاء
		self.entree.delete(0, len(self.v1ch)) # ازالة الحروف المكتوبية

#: البرنامج الرئيسي #
if __name__ == '__main__':
        from tkinter import *
	from math import log10 # خوارزمية بيأساس 10
	f = Application() # تمثيل كائن التطبيق
