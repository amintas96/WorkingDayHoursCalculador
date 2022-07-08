from datetime import timedelta


# entrada
def entradadeDados(entrada1):
    entrada1 = entrada1.strip().split(" ")
    horarios1 = []

    for horario1 in entrada1:
        horario2 = horario1.split(':')
        horarios1.append(timedelta(hours=int(horario2[0]), minutes=int(horario2[1])))
    return horarios1


# calculo
def CalculaHoraDeSair(horarios1, totalHorasTrabalhadas):   
    horaSair = totalHorasTrabalhadas[0] - (horarios1[1] - horarios1[0])
    horaSair += horarios1[2]
    return horaSair


def calculoDeHorasDia(horarios1):     
    totalTrabalhados = horarios1[1] - horarios1[0]
    totalTrabalhados += horarios1[3] - horarios1[2]
    if len(horarios1) > 5:
        totalTrabalhados += horarios1[5] - horarios1[4]

    return totalTrabalhados

def convert(listas):
    res_dict = {listas[i]: listas[i+1] for i in range(0, len(listas),2)}
    return res_dict
