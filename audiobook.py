import pyttsx3
import camelot
book = open('oop.pdf', 'rb')
pdfReader = camelot.read_pdfReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(5, pages):
    page = pdfReader.getPage(5)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
