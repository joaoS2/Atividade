#tentativa 1 (com datetime)


import datetime
print("Digite a primeira data abaixo:")
day1 = int(input("Dia(1 a 31): "))
month1 = int(input("Mês(1 a 12): "))
year1 = int(input("Ano: "))
print("Digite uma segunda data abaixo:")
day2 = int(input("Dia(1 a 31): "))
month2 = int(input("Mês(1 a 12): "))
year2 = int(input("Ano: "))

data1 = datetime.datetime(day= {day1}, month= {month1}, year= {year1})
data2 = datetime.datetime(day= {day2}, month= {month2}, year= {year2})
 
if data1.year == data2.year:
    if data1.month>data2.month:
        print(f"A data cronologicamente maior é: {data1}")
    elif data1.month<data2.month:
        print(f"A data cronologicamente maior é: {data2}")
    else:
        if data1.day>data2.day:
            print(f"A data cronologicamente maior é: {data1}")
        elif data1.day<data2.day:
            print(f"A data cronologicamente maior é: {data2}")
        else:
            print(f"As duas datas são iguais.")
elif data1.year>data2.year:
    print(f"A data cronologicamente maior é: {data1}")
else:
    print(f"A data cronologicamente maior é: {data2}")