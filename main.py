# Programa que mostra o calendario de determinado mês
import calendar

mes = int(input("Digite um mês corresponde a 1/12 de um ano: "))
ano = int(input("Digite um ano: "))

print(calendar.month(ano, mes))
