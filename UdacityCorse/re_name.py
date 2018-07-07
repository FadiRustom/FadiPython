import os

def re_name():
    #(1) get file name from a folder
    file_list =  os.listdir("C:\Users\DELL\Desktop\animals")
    print(file_list)
    cwd = os.getcwd()
    os.chdir("ضع مسار الملف هنا")
    print("cwd is: {0}".format(cwd))
    #(2) for each file,rename filename
    for file_name in file_list:
        table = str.maketrans(dict.fromkeys("1234567890"))
        new_file_name = file_name.translate(table)
        os.rename(file_name, new_file_name)
    
re_name()
