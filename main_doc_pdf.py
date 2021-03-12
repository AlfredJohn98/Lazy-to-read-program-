import pyttsx3 # python package to convert to speak
import PyPDF2 # python package to read pdf files

read_material = open("Insert doc name here","rb") # open the file and set to read binary property
package_reader= PyPDF2.PdfFileReader(read_material) # call the package function to read
page_num =package_reader.numPages # set to read the page number
print(page_num)  # print the page number to read

machine_read = pyttsx3.init()    # initialize the package

for num_read in range(0, page_num):
  page_num =package_reader.getPage(0) # set the page number that want to read
  reading_page =page_num.extractText() # call function to extract and read from page number
  machine_read.say(reading_page) # read from the page number
  machine_read.runAndWait()

# insert the the document that you want this program to read at the page holder for you
# It would be best if it is in a pdf format
# Dont not insert a online pdf book it will read every single line of that book for example the page and etc

