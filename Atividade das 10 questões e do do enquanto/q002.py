#2º

#Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, para os quais fornece a quantidade de ração em gramas. a diária de ração fornecida para cada gato é sempre a mesma. Faça um programa que receba o peso do saco de ração fornecida para cada gato, calcule e mostre quanto restará de ração no saco após cinco dias.

pesoquilo: float; pesograma: int; diariagrama: float; resto: float
pesoquilo = float(input('Informe quantos quilogramas tem o saco de ração: '))
racaodiaria = float(input('Informe quantas gramas de ração seu cada gato come por dia: '))
pesograma = pesoquilo * 1000
resto = pesograma - racaodiaria * 2 * 5
print('O restante de ração, depois de cinco dias, seria: ',resto,'gramas')