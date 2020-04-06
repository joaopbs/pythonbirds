

class Pessoa:
    def __init__(self,nome=None,idade=35):
        self.idade = idade
        self.nome = None

    def cumprimentar (self):
      return 'Olá'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print((p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'João'
    print(p.nome)