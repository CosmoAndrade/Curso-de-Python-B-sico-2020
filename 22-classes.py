class MyClass:
    x = 5

print(MyClass)

p1 = MyClass()
print(p1.x)

class Pessoa:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Lucas", 14)
print(p1.nome)
print(p1.idade)


class Pessoa:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print ('Olá meu nome é ', self.nome)

        
p1 = Pessoa("Lucas", 14)
print (p1.saudacao())