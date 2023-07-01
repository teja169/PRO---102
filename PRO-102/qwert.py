import os , shutil 

from_dir = "C:/Users/SANDHYA PASIKANTI/Downloads"
to_dir = "D:/organisedfile"

listoffiles = os.listdir(from_dir)
print(listoffiles)

for file in listoffiles :
    name , ext = os.path.splitext(file)
    print(name)
    print(ext)
    
    if ext == "" :
        continue
    
    if ext in [".pdf" , ".jpeg" ]:
        path1 = from_dir + "/" + file
        path2 = to_dir + "/" + ext
        path3 = to_dir + "/" + ext + "/" + file 
        
        print(path1)
        print(path3)
        
        if os.path.exists(path2):
            print("moving" + file )
            shutil.move(path1 , path3)
        
        else:
            os.mkdir(path2)
            print("moving" + file)
            shutil.move(path1 , path3)
        