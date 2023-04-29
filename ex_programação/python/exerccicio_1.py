um = float(input('Digite um número: '))
dois = float(input("Digite outro número: "))
soma = float(um + dois)
sub = float(um - dois)
mult = float(um * dois)
div = float(um / dois)
a = input('Você quer: ')
if a == "somar":
   e = print('o resultado é {}.'.format(soma))
elif a == "subtrair":
   e = print('O resultado é {}.'.format(sub))
elif a == "multiplicar":
   e = print('O resultado é {}.'.format(mult))
elif a == "dividir":
   e = print('O resultado é {}.'.format(div))
b = input('Você quer adicionar mais um valor? ')
if b == "sim" or "ok" or "afirmativo":
    c = float(input('Digite o valor: '))
    d =input('Você quer: ')
if d == "somar":
    r=float((e + c))
    print('o resultado é {}.'.format(r))
elif d == "subtrair":
    s=float((e - c))
    print('O resultado é {}.'.format(s))
elif d == "multiplicar":
    t=float((e * c))
    print('O resultado é {}.'.format(t))
elif d == "dividir":
    u=float((e / c))
    print('O resultado é {}.'.format(u))
elif b == "Não" or "Nah" or "Negativo":
    print('OK! Agradecemos a preferência!')

