# Atividade:  Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
# Autor: Higor Stanley
# Instrutor: Brunno
# Data: 11/05/2024
# Edit: Adicionado km no resultado

distancia = float(input('Insira a distância em metros para que seja convertido: '))

#Magimatica
dam = distancia / 10
hm = dam / 10
km =  hm / 10
dm = distancia * 10
cm = dm * 10
mm =  cm * 10
#WTFisKilometer = 
#pes =

print('A distância de', distancia, 'metros em outras medidas é:\n')
print(km,'Km', '        ', hm,'Hm')
print(dam, 'dam', '         ', dm, 'dm')
print(cm,'cm', '        ', mm,'mm')