from re import M


sex: str; nome: str

nome = input("Digite seu nome: ")
sex = input("Digite seu sexo (M - F): ")
while sex != "M" and sex != "m" and sex != "masculino" and sex != "Masculino":
    nome = input("Digite seu nome: ")
    sex = input("Digite seu sexo (M - F): ")