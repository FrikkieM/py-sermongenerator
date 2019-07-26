from SermonLister import fnGenerateIt
import sys

if len(sys.argv) != 2:
    print('Incorrect Usage.\nPlease pass a date in the format YYYYMMDD to the program.')
    print('Example Usage:\n            py main.py 20190725    ')
    exit
else:
    #Specify the date
    dateToGenerate = sys.argv[1]
    #Call the function
    fnGenerateIt(dateToGenerate)

print('\n\n\nThank you for using the Sermon HTML Generator. :)  ')
