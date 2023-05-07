#Importerar os module, som används för att arbeta med datorns filsystem
import os
import shelve

"""Funktionen söker efter filer i en mapp som "kunden" har angett den har 
textfiler och ger tillbaka en lista med alla textfiler som slutar med ".txt" och som inte heter "directoryPath.txt"""""
def getTxtFilesInFolder(folder_path):
    files = os.listdir(folder_path)
    return [f for f in files if f.endswith('.txt') and f != "directoryPath.txt"]

#Funktionen söker sig till mappen och ger namnet på en fil och ger tillbaka namnet på filerna
def getFilePath(folder_path, file_name):
    return os.path.join(folder_path, f"{file_name}.txt")

#Funktionen hittar en textfil och visar en lista med allt som står i filen.
def readTasksFromFile(file_path):
    with open(file_path, "r") as f:
        tasks = f.readlines()
    return tasks

"""Funktionen "createOrOpenFile" tar sökvägen till en fil och boolean variabeln som
 säger om filen ska skapas om den inte finns. Funktionen
 öppnar filen antingen i append mode, write mode, 
 eller returnerar "None" om filen inte kan öppnas eller skapas."""

def createOrOpenFile(file_path, create_file=False):
    if os.path.exists(file_path):
        mode = "a"
    elif create_file:
        mode = "w"
    else:
        return None
    return open(file_path, mode)

"""Funktionen söker en fil och indexet(nummret) för en uppgift som ska tas bort från filen. Den 
läser in alla uppgifter från filen och tar bort uppgiften som motsvarar det givna indexet. Varje rad i filen är en siffra för index
Funktionen skriver sedan uppgifterna till filen och skriver ut en rad på vilken uppgift som har tagits bort."""
def removeTask(file_path, task_index):
    tasks = readTasksFromFile(file_path)

    if task_index < 1 or task_index > len(tasks):
        print("Invalid task index.")
        return

    task = tasks.pop(task_index - 1)

    with open(file_path, "w") as f:
        f.writelines(tasks)

    print(f"Task '{task.strip()}' removed from the file.")

def directoryConfig():                  #Kommer ihåg vald katalog av användaren
    db = shelve.open("ToDoListConfig")
    if not db:                          #Kollar om det finns en lagrad värde
        directoryPath = input("Enter the directory where you want your lists to be saved here: ")
        db["directoryPath"] = directoryPath
    else:
        directoryPath = db['directoryPath']
        print(f"The current directory path is {directoryPath}")

    changeDirectory = input("Would you like to change the directory path? (yes/no): ")  #Om det finns ett lagrat värde kollar den med användaren om den vill byta
    if changeDirectory.lower() == 'yes' or changeDirectory.lower() == 'y':
        directoryPath = input("Please enter a directory where you want to have your lists saved: ")
        db['directoryPath'] = directoryPath



def main():
    directoryConfig()  # Här får användaren välja var filerna ska sparas
    db = shelve.open("ToDoListConfig")
    folder_path = db["directoryPath"]
    db.close()

    while not os.path.isdir(
            folder_path):  # En while-loop som ser till att programmet inte kraschar när katalogen inte hittas
        folder_path = input("The directory could not be found. Please enter again: ")

    txt_files = getTxtFilesInFolder(folder_path)

    print("Welcome to your to-do list! Select an existing to-do list below or create a new one:")

    for txt_file in txt_files:
        print(txt_file[:-4])

    file_name = input("Please enter the name of the file you want to edit or create: ")
    file_path = getFilePath(folder_path, file_name)

    file = createOrOpenFile(file_path, create_file=True)
    if file is None:
        print("Could not locate or create file. Exiting.")
        return

    tasks = readTasksFromFile(file_path)
    print("Your current to-do list:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task.strip()}")

    while True:
        command = input("Enter 'add' to add a task, 'remove' to remove a task,'new' to choose another list, or 'exit' to exit: ")
        if command.lower() == "exit":
            break
        elif command.lower() == "add":
            task = input("Please enter your task: ")
            file.write(task + "\n")
            print("Task added to the file.")
        elif command.lower() == "remove":
            tasks = readTasksFromFile(file_path)
            print("Your current to-do list:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.strip()}")

            task_indices = [i+1 for i in range(len(tasks))]
            print(f"Task indices: {task_indices}")

            task_index = int(input(f"Please enter the index of the task you want to remove (1-{len(tasks)}): "))
            removeTask(file_path, task_index)
        elif command.lower() == "new":  # Här körs en kod som gör det möjligt för användaren att välja en ny lista
            txtFiles = getTxtFilesInFolder(folder_path)
            print("Existing to-do lists:")
            for txtFile in txtFiles:
                print(txtFile[:-4])
            newFileName = input("Please enter the name of the new file you want to edit or create: ")
            newFilePath = getFilePath(folder_path, newFileName)
            newFile = createOrOpenFile(newFilePath, create_file=True)
            if newFile is None:
                print("Could not locate or create file. Exiting.")
                return
            tasks = readTasksFromFile(newFilePath)
            print(f"Your current to-do list ({newFileName}):")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task.strip()}")
            filePath = newFilePath
            file = newFile
        else:
            print("Invalid command.")

    file.close()

main()