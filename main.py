from usuario import Usuario
from gerente import Gerente

admim = Usuario('999', 'administrador','21/12/1980')
print(admim.contador, admim.nome, admim.data_nascimento)


manager = Gerente('000','Pedro Lucas','21/12/1978')
print (manager.contador)
manager.correr(12)