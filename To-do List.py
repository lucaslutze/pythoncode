import os

folderPath = "C:/Users/LucasLutze/PycharmProjects/pythonProject1" # User chooses file path
files = os.listdir(folderPath)
txtFiles = [f for f in files if f.endswith('.txt')]

print("Welcome to your to-do list! Select an existing to-do list below or create a new one:")

for txtFile in txtFiles:
    print(txtFile)

fileName = input("Please enter the name of the file you want to edit or create: ")
filePath = os.path.join(folderPath, fileName)

if os.path.exists(filePath):
    file = open(filePath, "r")
    tasks = file.read()
    print("Your current to-do list:")
    print(tasks)
    file.close()
    file = open(filePath, "a")
else:
    createFile = input("The list could not be located. Would you like to create one? (yes/no) ").lower()
    if createFile == "yes":
        file = open(filePath, "w")
    else:
        print("Okay, try to search for your file again")
        quit()

while True:
    task = input("Please enter your task or type 'exit' to exit: ")
    if task.lower() == "exit":
        break
    file.write(task + "\n")
    print("Task added to the file.")

file.close()
