import pandas as pd
import pdf 

disctHours = pdf.extrairPdf('relatorio (2).pdf')

listDates = list(disctHours.keys())
listHours = list(disctHours.values())
listHoursWorker = list(pdf.calculaHorasLista(disctHours).values())

dictWorker = {'Data': listDates,
               'PontosBatidos':listHours}


dt = pd.DataFrame(dictWorker)
print(dt)
# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
  
# Convert the dictionary into DataFrame 

# select two columns
