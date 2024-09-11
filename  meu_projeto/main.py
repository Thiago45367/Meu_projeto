import os
from models.pessoa import Pessoa
from models.enums.sexo import Sexo

os.system("cls || clear")

aluno = Pessoa("Marta", 22, Sexo.FEMININO)
print(aluno)