#13. Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
print("Calculando quantos dias durará o alimento com base na quantidade em kg e consumo diário de 50g...")

print("Digite a quantidade em quilos do alimento:")
kg = float(input())

#conversão de kg para g:
g = kg*1000
dias = g/50

print() #print estético
print("O alimento será o suficiente durante" , dias , "dias.")