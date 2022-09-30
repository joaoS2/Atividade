#tentativa 2 (sem datetime)


print("Digite a primeira data abaixo:")
day1 = int(input("Dia(1 a 31): "))
month1 = int(input("Mês(1 a 12): "))
year1 = int(input("Ano: "))
print("Digite uma segunda data abaixo:")
day2 = int(input("Dia(1 a 31): "))
month2 = int(input("Mês(1 a 12): "))
year2 = int(input("Ano: "))

if year1 == year2:
    if month1>month2:
        print(f"A data cronologicamente maior é: {day1}/{month1}/{year1}")
    elif month1<month2:
        print(f"A data cronologicamente maior é: {day2}/{month2}/{year2}")
    else:
        if day1>day2:
            print(f"A data cronologicamente maior é: {day1}/{month1}/{year1}")
        elif day1<day2:
            print(f"A data cronologicamente maior é: {day2}/{month2}/{year2}")
        else:
            print(f"As duas datas são iguais.")
elif year1>year2:
    print(f"A data cronologicamente maior é: {day1}/{month1}/{year1}")
else:
    print(f"A data cronologicamente maior é: {day2}/{month2}/{year2}")