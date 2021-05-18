from datetime import datetime
import calendar

# Codigo para mostar o calendario do ano inteiro
# print(calendar.TextCalendar(calendar.SUNDAY).formatyear(2021))

hoje = datetime.now()

mes = hoje.month
ano = hoje.year
dia = hoje.day

calendario = calendar.month(ano, mes)

print(calendario)
print(f'Dia atual: {dia}')

