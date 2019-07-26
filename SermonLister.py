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
    relevantMP3 = ""
    relevantPDF = ""
    patternMP3 = "*" + campusCode + "*.mp3"
    patternPDF = "*" + campusCode + "*.pdf"
    
    for entry in relevantFilesArray:
        if fnmatch.fnmatch(entry, patternMP3):
            relevantMP3 = entry
            
    for entry in relevantFilesArray:
        if fnmatch.fnmatch(entry, patternPDF):
            relevantPDF = entry

    #If found, the relevant MP3 and PDF will be added to the array for processing, else it will be empty
    #and thus return and empty <td> </td> in the HTML from the Class.
    relevantFiles.append(relevantMP3)
    relevantFiles.append(relevantPDF)
    
    #print(relevantFiles)   #I used this for error checking
    return relevantFiles
    
def fnGenerateIt(dateToGenerate):
    campusToGenerate = ["TDO","TDM","NOVA"]

    for entry in campusToGenerate:
        try:
            files = fnSplitByCampus((fnSermonsByDate('Exports - Website',dateToGenerate)),entry) 
            #print(files)   #Used for error checking
            p = SermonHTMLGenerator(files[0],files[1])
            print(p.GenerateHTML())
        except:
            print('Error in Generating It')



