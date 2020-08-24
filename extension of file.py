name=input("Input the Filename: ")
ext=name.split(".")
if ext[-1]=="py":
    print("The extension of the file is : python")
elif ext[-1]=="cpp":
    print("The extension of the file is : c++")
elif ext[-1]=="doc":
    print("The extension of the file is : word")
elif ext[-1]=="txt":
    print("The extension of the file is : text")
elif ext[-1]=="exe":
    print("The extension of the file is : executable")
else:
    print("The extension of the file is : ",ext[-1])
