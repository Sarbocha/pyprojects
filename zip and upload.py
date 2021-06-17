import zipfile

target = ""

handle = zipfile.ZipFile(target)
handle.extractall("#path")
handle.close()

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

print('Document Mover started...')

destination = input('Choose a directory:')

# Authentication
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


# Searching folder in GDrive
def searchFolder(folderName):
    response = drive.ListFile({"q": "mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in response:
        if (folder['title'] == folderName):
            print("Folder '" + folderName + "' found")
            return folder

    print("Could not found folder " + folderName)
    exit()


# Uploading file to GDrive
def uploadToDrive(sourceFile):
    if (destination == '1'):
        folder = searchFolder('Bills')
    elif (destination == '2'):
        folder = searchFolder('Taxes')
    elif (destination == '3'):
        folder = searchFolder('Car')
    elif (destination == '4'):
        folder = searchFolder('Bank')
    elif (destination == '5'):
        folder = searchFolder('Insurance')

    file = drive.CreateFile({
        'title': sourceFile.split('\\')[-1],
        'parents': [{
            'kind': 'drive#fileLink',
            'id': folder['id']
        }]
    })
    file.SetContentFile(sourceFile)
    file.Upload()


# Windows Harddrive
sourceFolder = "D:\BuWit\Pictures\Scans"

for file in os.listdir(sourceFolder):
    if (file.endswith('.pdf') and file.startswith('Scans')):
        print("Renaming...")
        pureFileName = file.split('_', 1)[1]
        newFilePath = "%s\%s" % (sourceFolder, pureFileName)
        oldFilePath = "%s\%s" % (sourceFolder, file)
        os.rename(oldFilePath, newFilePath)

        print("Uploading...")
        uploadToDrive(newFilePath)
        print("File '" + pureFileName + "' successfully uploaded.")

        os.remove(newFilePath)

print("Finished moving files")
exit()

