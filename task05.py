# 5. Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

numero1 = int(input('Digite um número de 1 a 10: '))
numero2 = int(input('Digite outro número de 1 a 10: '))
divisao = float(numero1 / numero2)
print('Se dividirmos um número pelo outro teremos o resultado %.2f.' %(divisao))
