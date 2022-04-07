import os

cwd = os.getcwd()  # Get the current working directory (cwd)
fileName = input("Enter file name: ")
path = cwd + "/basic_command/" + fileName
fPoem = open(path, "r+")
# r, r+
print(fPoem)
print(fPoem.read())
print("Write....")
newText = input("Enter new text: ")
print(fPoem.write(newText))