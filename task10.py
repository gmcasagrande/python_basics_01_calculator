# 10. Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.

'''
 Uma certa vacina precisa ser aplicada em um grupo de 52 pessoas,
 sendo 5 crianças, 12 adolescentes, 20 adultos e 15 idosos.
 As crianças precisam de apenas uma dose, enquanto os adolescentes
 precisam de 2 doses, os audltos 3 doses e os idosos 4 doses.
 Calcule a média de doses aplicadas por pessoa.
'''
criancas = 5
adolescentes = 12
adultos = 20
idosos = 15
total = (criancas + adolescentes + adultos + idosos)
mediadedoses = float((criancas*1 + adolescentes*2 + adultos*3 + idosos*4) / total)
print('Cada pessoa receberá uma média de %.2f doses de vacina' %(mediadedoses))
