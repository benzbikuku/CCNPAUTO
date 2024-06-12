import os
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
print(os.listdir("."))
print(len(os.listdir(".")))
print(f"The current working directory is ;  {os.getcwd()} ")
print(os.system('ls -larth'))
files = os.listdir()
files.sort()

for file in files:
    print(f" \n\n printing {'#'*10} {file}  {'#'*10} \n\n")
    try:
        with open(file) as file_data:
            print(file_data.readlines())
    except IsADirectoryError:
        print("This is directory and cannot be opened")
            
