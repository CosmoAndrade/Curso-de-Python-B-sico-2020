def minha_func():
    print ('Esta é minha função')

minha_func ()


def minha_func(saudacao):
    print (saudacao)


minha_func('Olá!')
minha_func('Olá tudo bem!')
minha_func('Olá como vai!')

def minha_func(num1 , num2):
    return num1 + num2
    
print (minha_func(5,8))


def minha_func(*args):
    print (args)

minha_func('azul', 'verde','roxo', 'amarelo')



def minha_func(**kwargs):
    print (kwargs)

minha_func(nome='Cosmo',idade=35)

