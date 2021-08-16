#Calcular quantos anos terá no ano "x"
try:
    nascimento_ano = int(input('Em qual ano você nasceu ?'))
    idade = int(input('Digite uma idade: '))
    resultado = nascimento_ano + idade
    print(f'Em {resultado} você tera {idade} anos')
except:
    print('Digite um valor valido')


