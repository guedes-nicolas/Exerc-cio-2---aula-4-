print()
banco = []
dadosrange = 3
menoridade = 0
menorID = 0

for i in range(dadosrange):
    pessoa = []
    pessoa.append (input('Digite um nome: '))
    pessoa.append (int(input('Digite uma idade: ')))
    banco.append(pessoa)

for i in range (dadosrange):
    if banco[i][1] < 18:
        menoridade = banco[i][1]
        menorID = i

print(f'A pessoa com menor idade é {banco[menorID][0]}')