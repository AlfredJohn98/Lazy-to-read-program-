import pyttsx3 # python package to convert to speak
import PyPDF2 # python package to read pdf files


machine = pyttsx3.init()

machine.say ( '''

Type in what you want to say and i can say it for you. Dont forget to run the program bro


''')
machine.runAndWait()