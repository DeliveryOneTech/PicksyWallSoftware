import os


def ConvertUIFileToPyFile(uiFilePath, pyFilePath):
    os.system("pyuic5 " + uiFilePath + " -o " + pyFilePath)


# .qrc file to .py file
def ConvertQRCFileToPyFile(qrcFilePath, pyFilePath):
    os.system("pyrcc5 " + qrcFilePath + " -o " + pyFilePath)


def ConvertAllUIFilesToPyFiles():
    # get all uiFiles in current directory
    uiFiles = [f for f in os.listdir(".") if f.endswith(".ui")]
    for uiFile in uiFiles:
        pyFile = uiFile.replace(".ui", "UI.py")
        # first char to upper case
        pyFile = pyFile[0].upper() + pyFile[1:]
        ConvertUIFileToPyFile(uiFile, pyFile)


# ConvertUIFileToPyFile("addCargoSensorView.ui", "AddCargoSensorViewUI.py")

ConvertQRCFileToPyFile("picksy_wall.qrc", "resource.py")

# ConvertAllUIFilesToPyFiles()
