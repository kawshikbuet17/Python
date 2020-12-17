#pip install pyttsx3
#pip install PyPDF2==1.26.0

import pyttsx3
import PyPDF2

book = open('audioBook/book_pdf.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print('Total pages = ', pages)


from_pg = 2
to_pg = 3

for num in range(from_pg, to_pg):
    speaker = pyttsx3.init()
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    # speaker.say('Look, I can talk')
    speaker.runAndWait()