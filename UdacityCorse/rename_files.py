# Python 2-3

import os
def rename_files():
    # Get FileName
    file_list = os.listdir(r"C:\oop\prank")
    saved_path = os.getcwd()
    print (file_list,'#',saved_path)
    os.chdir(r"C:\oop\prank")
    #For each file, ReName FileName
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))

    os.chdir(saved_path)
     
rename_files()
