import pandas as pd
import pdf 
import CalculoDeHoras as ch

disctHours = pdf.extrairPdf('relatorio (2).pdf')
disctHours = {i: k for i , k in disctHours.items() if k != "Feriado" if k != "Folga" if k != "DSR" if k != "Compensação Dia" }
listDates = list(disctHours.keys())
listHours = list(disctHours.values())
listHoursWorker = list(ch.calculaHorasDict(disctHours).values())


print(listDates)
dictWorker = {'Data': listDates,
              'Pontos Batidos':listHours,
               'Horas Trabalhadas':listHoursWorker }


dictWorker = pd.DataFrame(dictWorker)

file_name = 'HorasTrabalhadas.xlsx'
dictWorker.to_excel(file_name)