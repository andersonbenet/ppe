class Usuario:

    contador = 999

    def __init__(self, codigo, nome, data_nascimento):
        self.__codigo = Usuario.contador + 1
        self.nome = nome
        self.data_nascimento = data_nascimento
        Usuario.contador = self.__codigo


    def __correr(self, metros):
        print ('Estou correndo {metros} metros')
