from usuario import Usuario

class Gerente(Usuario):
    def __init__(self, codigo, nome, data_nascimento):
        Usuario.__init__(self,codigo,nome,data_nascimento)


    def correr(self, metros):
        if self.data_nascimento == '21/12/1980':
            print ('Apto a correr')
        else:
            print ('Inapto a correr')


