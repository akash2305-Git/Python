import os
print("Operating system name:",os.name)
#print("\n Information of current Operating system:",os.uname())
print("\n current working directory:",os.getcwd())
print("\n List of file in current Directory:")
print(os.listdir('.'))
print("\n if current file exist or not")
try:
    filename = "myfile.txt"
    f = open(filename,'r')
    text = f.read()
    print(text)
    f.close()
except:
    print("File is not access" + filename)