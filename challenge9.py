# 9. Crie um código que solicita 3 notas de um estudante e imprima a média das notas.

nota1 = float(input('Digite a nota de História: '))
nota2 = float(input('Digite a nota de Artes: '))
nota3 = float(input('Digite a nota de Geografia: '))
media = float((nota1 + nota2 + nota3) / 3)
print('A média das notas foi de %.1f' %(media))
