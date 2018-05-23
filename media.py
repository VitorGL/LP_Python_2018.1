def media(notas):
    med = 0.0
    pesos = [2, 3, 4, 1]
    for pe, nota in zip(pesos, notas):
        med += pe * nota

    med /= 10
    print('Media: {}'.format(round(med, 1)))
    if med >= 7.0:
        print('Aluno Aprovado.')
    elif med < 5.0:
        print('Aluno Reprovado.')
    else:
        print('Aluno em exame.')
        exame = float(input('Digite a nota do exame: '))
        print('Nota do exame: {}'.format(round(exame, 1)))
        med = (exame + med) / 2
        if med >= 5.0:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
        print('Media final: {}'.format(round(med, 1)))

notas = input('Digite as notas na mesma linha separadas por espaços: ').split()
notas = [float(i) for i in notas]
media(notas)
