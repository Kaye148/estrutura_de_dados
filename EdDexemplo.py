import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    idade: int

    def mostar_dadaos(self):
        print(f"Nome:{self.nome}")
        print(f"idade:{self.idade}")
        
print("===Solicitendo Dados===")
cliente1 = Cliente(nome=(input("informe seu nome: ")),
                   idade=(input("informe sua idade: ")))

print("(❁´◡`❁)———————————————————————————————————(❁´◡`❁)")

cliente2 = Cliente(nome=(input("informe seu nome: ")),
                   idade=(input("informe sua idade: ")))

print("\n==Exibindo Dados==")
cliente1.mostar_dadaos()
print("===☆*: .｡. o(≧▽≦)o .｡.:*☆===")
cliente2.mostar_dadaos()
