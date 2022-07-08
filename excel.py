import pandas as pd
import pdf 
import CalculoDeHoras as ch

disctHours = pdf.extrairPdf('relatorio (2).pdf')

listDates = list(disctHours.keys())
listHours = list(disctHours.values())
listHoursWorker = list(ch.calculaHorasDict(disctHours).values())

dictWorker = {'Data': listDates,
              'PontosBatidos':listHours}


