# التعامل مع الملفات
# فتح ملف

# نسخ ملف
def fcopy(source, destination):
    "Copy Function: copy the text of sourse to destination - 50 cher"
    fs= open(source, 'r')
    fd= open(destination, 'w')
    while 1:  #True
        txt= fs.read(50)
        if txt == "":
            break #end while
        fd.write(txt)
    fs.close()
    fd.close()
    return

# القراءة من ملف

# التحقق من وجود الملف
def existe():
    global fName
    fName= input('Enter FileName for Find: ')
    try:
        f=open(fName,'r')
        f.close()
        return "Fuond the File: ", fName
    except:
        return "Not Fuond the File: ", fName
    #
    #
            
