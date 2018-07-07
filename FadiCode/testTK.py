class TestTK(object):
    def __init__(self):
        self.frm=Tk()
        self.frm.title('Test Tk')
        Label(self.frm, text="Fadi Rustom").pack()
        Button(self.frm, text="Exit", command=self.frm.destroy).pack()
        self.txt=Entry(self.frm, width =14)
        self.txt.pack()
        self.frm.mainloop()


        

if __name__ == '__main__':
    from tkinter import *
    f= TestTK()
