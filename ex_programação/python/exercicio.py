p = float(input('Digite seu peso: '))
a = float(input('Digite a sua altura: '))
imc = float(p/(a**2))
print('O seu IMC é equivalente {}.'.format(imc))
if imc>18.0 and imc<25.0:
    print('Você está saudável!!')
if imc<18.0:
    print('Você está abaixo do peso ideal...')
if imc>25.0:
    print('Você está com sobrepeso...')
