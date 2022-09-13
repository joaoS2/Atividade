#Entrada
Medida=float(input("informe sua medida em pés: "))
#Processamento
jardas=Medida/3
Polegadas=Medida*12
Milhas=Medida/1.760
#Saída
print(f"seu valor em polegadas é de {round(Polegadas,2)}")
print(f"seu valor em jardas é de {round(jardas,2)}")
print(f"seu valor em milhas é de {round(Milhas,2)}")
