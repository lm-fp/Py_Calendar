import calendar

dia = int(input("Digite um dia: "))
mes = int(input("Digite um mês corresponde a 1/12 de um ano: "))
ano = int(input("Digite um ano: "))

dia_semana = calendar.weekday(ano,mes,dia)

if dia_semana == 0:
    print("Segunda-Feira")
elif dia_semana == 1:
    print("Terca-Feira")
elif dia_semana == 2:
    print("Quarta-Feira")
elif dia_semana == 3:
    print("Quinta-Feira")
elif dia_semana == 4:
    print("Sexta-Feira")
elif dia_semana == 5:
    print("Sabado")
else: 
    print("Domingo")