import re
import os, fnmatch
import sys

# ======================================= MAIN CLASS =======================================

class SermonHTMLGenerator:
    def __init__(self, filenameMP3, filenamePDF):
        self.FileMP3 = filenameMP3
        self.FilePDF = filenamePDF

    def fnGetCampus(self, s):
        CampusDict = {"TDO":"Ooskampus", "TDM":"Moederkampus", "NOVA":"NOVA","TDE":"English Campus","TDCC":"City Campus"}
        try:
            #Find the campus' abbreviation in uppercase as key and return that value from dictionary
            return CampusDict[s.upper()]
        except:
            #Use a regular expression to insert spaces at Uppercase for special cases
            return re.sub(r"(?<=\w)([A-Z])", r" \1", s)

    def fnGetPastor(self, s):
        PastorDict = {"DO":"Danie Oosthuizen", 
                    "BF":"Berron Fuhri", "FM":"Frikkie v.d. Merwe", "AW":"Albert v.d. Westhuizen",
                    "RB":"Retief Booysen","DB":"Douglas Brooks","JR":"Jaco Roggeband","CG":"Christiaan Gouws",
                    "CC":"Chante Cornelius","JS":"Johan Steyn","LdP":"Lemmer du Plessis","MS":"Myan Subrayan",}
        try:
            #Find the pastor's abbreviation in uppercase as key and return that value from dictionary
            return PastorDict[s.upper()]
        except:
            #Use a regular expression to insert spaces at Uppercase for special cases
            return re.sub(r"(?<=\w)([A-Z])", r" \1", s)

    def fnGetTitle(self, s):
        #Replaces the underscores in the title with spaces and changes "n" to "'n"
        s = re.sub(r"(?<=\w)(_)", r" ", s)  #Replace underscores with spaces
        s = re.sub(r"(-)(_)", r"- ", s)  #Replaces -_ with -
        s = re.sub(r"( n )", r" 'n ", s)    #Replace n with 'n
        s = re.sub(r"(Q.)", r"?.", s)       #Replace Q. with ?. for questionmark at end of title
        s = re.sub(r"(E.)", r"!.", s)       #Replace E. with !. for questionmark at end of title
        s = s[:-4]                          #Removes the last 4 characters, thus hiding .mp3 file ending (Should change this to remove last fullstop and everything thereafter)
        return s

    def fnCreateFileLinks(self):
        #Creates the URL Links to the files: HQ Audio, SQ Audio, PDF Sermon notes (if any)
        #--Questionmark: End filename with Q. Exclamation: End filename with E
        s1 = self.FileMP3
        s2 = self.FilePDF
        s = "\n<td><a href=\"../content/preke/" + s1 + "\"> <img src=\"http://tabernadei.co.za/wp-content/uploads/2019/04/play1.png\"> </a></td>"
        if len(s2.strip()) > 0:
            s += "\n<td><a href=\"../content/preke/" + s2 + "\"> <img src=\"http://tabernadei.co.za/wp-content/uploads/2019/04/pdf.png\"> </a></td>"
        else:
            s += "\n<td> </td>"
        return s

    def GenerateHTML(self):
        filedata = self.FileMP3.split("_", 3)
        sermonDate = filedata[0]
        sermonCampus = self.fnGetCampus(filedata[1])
        sermonPastor = self.fnGetPastor(filedata[2])
        sermonTitle = self.fnGetTitle(filedata[3])
        sermonFiles = self.fnCreateFileLinks()
        HTMLString = "<tr>\n<td>" + sermonDate + "</td>\n<td>" + sermonCampus + "</td>\n<td>"
        HTMLString += sermonPastor + "</td>\n<td>" + sermonTitle + "</td>" + sermonFiles
        HTMLString += "\n</tr>"
        return HTMLString

# ======================================= DIRECTORY FUNCTIONS =======================================

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


# ======================================= MAIN PROGRAM =======================================

if len(sys.argv) != 2:
    print('Incorrect Usage.\nPlease pass a date in the format YYYYMMDD to the program.')
    print('Example Usage:\n            py main.py 20190725    ')
    exit
else:
    #Specify the date
    dateToGenerate = sys.argv[1]
    #Call the function
    print(dateToGenerate)
    fnGenerateIt(dateToGenerate)

print('\n\n\nThank you for using the Sermon HTML Generator. :)  ')
