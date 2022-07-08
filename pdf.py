from PyPDF2 import PdfReader
import CalculoDeHoras as ch

def extrairPdf(entrada):

    reader = PdfReader(entrada)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    listHours = text.split('\n')
    listHours = listHours[21:]

    listHours = [i for i in listHours if i != '']
    discHours = ch.convert(listHours)
    discHours = {i: k[8:] for i, k in  discHours.items()}
    return discHours

def calculaHorasLista(discHours):
    discHours2 = {i: ch.calculoDeHorasDia(ch.entradadeDados(k)) for i , k in discHours.items() if k != "Feriado" if k != "Folga" if k != "DSR" if k != "Compensação Dia"}
    return discHours2


