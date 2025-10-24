import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    cpf: str
    telefone: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")

    def dados_sms_marketing(self):
        print(f"Telefone: {self.telefone}")



lista_cliente = []
lista_telefone = []

for i in range(3):
    dados_cliente = Cliente (nome=input("digite seu nome: "),
                            cpf=input("informe seu cpf: "),
                            telefone=input("digite seu telefone: "))
    lista_cliente.append(dados_cliente)
    lista_telefone.append(dados_cliente)

print("\n")

for Cliente in lista_cliente:
    Cliente.mostrar_dados()
    Cliente.dados_sms_marketing()
