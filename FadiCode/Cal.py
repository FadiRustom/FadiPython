'''Visual Calculator
Athour: Fadi Rustom'''
from tkinter import *
#Click Number Function
def btnClick(numbers):
    global opertor
    opertor = opertor+ str(numbers)
    txtInput.set(opertor)

# Click Clear
def Clear():
    global opertor
    opertor =""
    txtInput.set('')

# Click Equals
def Equals():
    global opertor
    sumup = str(eval(opertor))
    txtInput.set(sumup)
    opertor = ""

cal= Tk()
cal.title('Calculator Fadi')
opertor=''

# Text Input Numbers Visual
txtInput=StringVar()
textDisplay=Entry(cal,font=('arial',20,'bold'),textvariable=txtInput,bd=30,insertwidth=4,bg='powder blue',justif='right').grid(columnspane=4)
# Enter Number & Opertore Visual Buttoms
#Row=1
btn7 = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='7',bg='powder blue' ,command=lambda : btnClick(7)).grid(row=1,column=0)
btn8 = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='8',bg='powder blue',command=lambda : btnClick(8)).grid(row=1,column=1)
btn9 = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='9',bg='powder blue',command=lambda : btnClick(9)).grid(row=1,column=2)
Addition = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='+',bg='powder blue',command=lambda : btnClick('+')).grid(row=1,column=3)
#Row=2
btn4 = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='4',bg='powder blue',command=lambda : btnClick(4)).grid(row=2,column=0)
btn5 = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='5',bg='powder blue',command=lambda : btnClick(5)).grid(row=2,column=1)
btn6 = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='6',bg='powder blue',command=lambda : btnClick(6)).grid(row=2,column=2)
Subtraction = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='-',bg='powder blue',command=lambda : btnClick('-')).grid(row=2,column=3)
#Row=3
btn1 = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='1',bg='powder blue',command=lambda : btnClick(1)).grid(row=3,column=0)
btn2 = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='2',bg='powder blue',command=lambda : btnClick(2)).grid(row=3,column=1)
btn3 = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='3',bg='powder blue',command=lambda : btnClick(3)).grid(row=3,column=2)
Multiply = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='*',bg='powder blue',command=lambda : btnClick('*')).grid(row=2,column=3)
#Row=4
btn0 = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='0',bg='powder blue',command=lambda : btnClick(0)).grid(row=4,column=0)
btnClear = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='C',bg='powder blue',command=Clear()).grid(row=4,column=1)
btnEquals = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='=',bg='powder blue',command=Equals()).grid(row=4,column=2)
Division = Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='/',bg='powder blue',command=lambda : btnClick('/')).grid(row=4,column=3)
#Row=3

cal.mainloop()
