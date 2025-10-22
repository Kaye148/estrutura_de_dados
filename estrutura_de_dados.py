from dataclasses import dataclass

@dataclass
class pessoa:
    nome:str
    idade:int
    cpf:str

@dataclass
class Pet:
    nome:str
    idade:int
    peso:float

#Exemplo de uso da classe
pessoa1= pessoa(nome="marta",idade=20 ,cpf="20.111.222.333.44")
pet1 = Pet("totó", 4, 3.5)

print(f"nome:{pessoa1.nome},\nidade: {pessoa1.idade},\ncpf:{pessoa1.cpf}")

print(f"nome:{pet1.nome}\nidade: {pet1.idade}\npeso{pet1.peso}")