notaTrabalhos = float(input())
notaProva = float(input())

media = (notaTrabalhos + notaProva) / 2

if media<6:
    print(f'reprovado')
elif media<10:
    print(f'aprovado')
else:
    print(f'talvez com a sub')
