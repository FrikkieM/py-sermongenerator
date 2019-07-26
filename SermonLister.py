from SermonHTMLGeneratorClass import SermonHTMLGenerator
import os, fnmatch

#Unused function, but good to remember
def fnDirScanner(dirName):
    with os.scandir(dirName) as entries:
        for entry in entries:
            print(entry.name)


def fnSermonsByDate(dirName, dateToMatch):
    #Returns an array of files from specific date
    listOfFiles = os.listdir(dirName)
    pattern = dateToMatch + "*.*"
    relevantFiles = []

    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            relevantFiles.append(entry)
    
    return relevantFiles
 
def fnSplitByCampus(relevantFilesArray,campusCode):
    #Looks for specific campus's files from relevantFilesArray, 
    # and only returns the MP3 and PDF file for specific campus
    relevantFiles = []
    pattern = "*" + campusCode + "*.*"
    for entry in relevantFilesArray:
        if fnmatch.fnmatch(entry, pattern):
            relevantFiles.append(entry)
    
    return relevantFiles
    
def fnGenerateIt(dateToGenerate):
    campusToGenerate = ["TDO","TDM","NOVA"]

    for entry in campusToGenerate:
        try:
            files = fnSplitByCampus((fnSermonsByDate('WebsitePreke',dateToGenerate)),entry) 
            p = SermonHTMLGenerator(files[0],files[1])
            print(p.GenerateHTML())
        except:
            pass


