import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome:str
    idade:int
    peso:float
    altura:float

pessoa1= Pessoa(nome=input("digite seu nome: "),
                 idade=int(input("digite sua idade: ")),
                 peso=float(input("digite seu peso: ")),
                 altura=float(input("digte sua altura: ")))

print("\n=Exibindo dados=")
print(f"nome: {pessoa1.nome} \nidade: {pessoa1.idade} \npeso: {pessoa1.peso} \naltura: {pessoa1.altura}")

