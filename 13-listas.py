lista = ["maçã", "banana", "cereja"]
print (lista)

# Você acessa os itens da lista consultando o número do índice:
print (lista[1])

# Ao especificar um intervalo, o valor retornado será uma nova lista com os 
# itens especificados.
frutas = ["maçã", "banana", "cereja", "laranja", "kiwi", "melão", "manga"]
print (frutas[2:5])
print (frutas[:4])
print (frutas[2:])

# Alterar valor do item
# Para alterar o valor de um item específico, consulte o número do índice:
lista = ['maçã', 'banana', 'cereja']
lista [1] = 'uva'
print (lista)

# Para adicionar um item ao final da lista, use o método append() :
lista = ['maçã', 'banana', 'cereja']
lista.append ('abacaxi')
print (lista)

# use o método insert () :
frutas = ['maçã', 'banana', 'cereja', 'abacaxi']
frutas.insert (2, 'laranja')
print (frutas)

# O remove () método remove o item especificado:

frutas = ['maçã', 'banana', 'cereja', 'abacaxi']
frutas.remove ('cereja')
print (frutas)


# O pop () método remove o índice especificado (ou o último item se o índice 
# não for especificado

frutas = ['maçã', 'banana', 'abacaxi' ]
frutas.pop ()
print (frutas)

# A del palavra-chave remove o índice especificado:

frutas = ['maçã', 'banana', 'abacaxi' ]
del frutas[0]
print (frutas)

# O clear () método esvazia a lista:

frutas = ['maçã', 'banana', 'abacaxi' ]
frutas.clear()
print (frutas)









