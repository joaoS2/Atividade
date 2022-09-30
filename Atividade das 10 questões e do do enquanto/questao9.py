import datetime
data = datetime.datetime.now()
dia = data.day
mes = data.month
ano = data.year
h = data.hour
min = data.minute

if mes == 1:
    print(f"{dia}-janeiro-{ano}, {h}:{min}")
elif mes == 2:
    print(f"{dia}-fevereiro-{ano}, {h}:{min}")
elif mes == 3:
    print(f"{dia}-março-{ano}, {h}:{min}")
elif mes == 4:
    print(f"{dia}-abril-{ano}, {h}:{min}")
elif mes == 5:
    print(f"{dia}-maio-{ano}, {h}:{min}")
elif mes == 6:
    print(f"{dia}-junho-{ano}, {h}:{min}")
elif mes == 7:
    print(f"{dia}-julho-{ano}, {h}:{min}")
elif mes == 8:
    print(f"{dia}-agosto-{ano}, {h}:{min}")
elif mes == 9:
    print(f"{dia}-setembro-{ano}, {h}:{min}")
elif mes == 10:
    print(f"{dia}-outubro-{ano}, {h}:{min}")
elif mes == 11:
    print(f"{dia}-novembro-{ano}, {h}:{min}")
else:
    print(f"{dia}-dezembro-{ano}, {h}:{min}")