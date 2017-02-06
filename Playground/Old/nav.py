import time, os, sys, datetime, shutil

now = datetime.datetime.now()
downloadLocation = "../../Downloads"
recyclingLocation = "../../.Trash"

downloadNumber = 0
recyclingNumber = 0

downloadDir = os.listdir(downloadLocation)
recyclingDir = os.listdir(recyclingLocation)

for file in downloadDir:
    downloadNumber += 1

for file in recyclingDir:
    recyclingNumber += 1

print("Welcome to Stefan's bin program.")

print('The year is %d. \nDownloads folder has %d files \nRecycling bin has %d files' % (now.year, downloadNumber, recyclingNumber))
print("Press 1 to check downloads folder, 2 to check recycling bin.")
#print("------------------------------------------------")
#print("- Press 1 to empty downloads folder press 2 to empty recycling bin-")
#print("------------------------------------------------")

def yesNoCheck(message):
    Input = input(message + " Y/No")
    if Input == "Y" or Input == "y" or Input == "yes":
        return True
    else:
        return False

def showFolderContents(dir):
    osDir = os.listdir(dir)
    for file in osDir:
        print(file)

while True:
    userInput = input("Enter your choice:")

    if userInput == "1":
        print("The downloads folder contains the following files:")

        #showFolderContents(downloadDir)
        showFolderContents(downloadLocation)

        if yesNoCheck("Are you sure you want to delete?"):

            shutil.rmtree(downloadLocation)
            if not os.path.exists(downloadLocation):
                os.makedirs(downloadLocation)
            print("Downloads folder contents deleted")
            break
        else:
            print("I didn't think so")
            break

    elif userInput == "2":

        print("The downloads folder contains the following files:")

        showFolderContents(recyclingLocation)

        if yesNoCheck("Are you sure you want to delete?"):
            shutil.rmtree(recyclingLocation)
            if not os.path.exists(recyclingLocation):
                os.makedirs(recyclingLocation)

            print("Recycling bin folder deleted")
            break
        else:
            print("I didn't think so.")
            break

    else:
        print("Invalid option, try again")
