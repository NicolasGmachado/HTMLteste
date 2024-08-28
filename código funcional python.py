# manipulação de datas 
import datetime
from datetime import datetime
from collections import defaultdict

# representa data e valor da venda 
class Venda:
    def __init__(self, data, valor):
        self.data = data
        self.valor = valor

# armazana vendas e clientes
class SistemaDeVendas:
    def __init__(self):
        self.vendas = []
        self.clientes = set()
   
    def registrarVenda(self, data, cpfCliente, valor):
        venda = Venda(data, valor)
        self.vendas.append(venda)
        self.clientes.add(cpfCliente)
   
    def vendasDiarias(self):
        vendasPorDia = defaultdict(float)
        for venda in self.vendas:
            vendasPorDia[venda.data] += venda.valor
        return vendasPorDia
    
    def vendasSemanais(self):
        vendasPorSemana = defaultdict(float)
        for venda in self.vendas:
            semana = venda.data.isocalendar()[1]
            vendasPorSemana[semana] += venda.valor
        return vendasPorSemana
   
    def vendasMensais(self):
        vendasPorMes = defaultdict(float)
        for venda in self.vendas:
            mes = venda.data.month
            vendasPorMes[mes] += venda.valor
        return vendasPorMes
   
    def mediaVendasDiarias(self):
        vendasPorDia = self.vendasDiarias()
        return sum(vendasPorDia.values()) / len(vendasPorDia) if vendasPorDia else 0
   
    def mediaVendasSemanais(self):
        vendasPorSemana = self.vendasSemanais()
        return sum(vendasPorSemana.values()) / len(vendasPorSemana) if vendasPorSemana else 0
   
    def mediaVendasMensais(self):
        vendasPorMes = self.vendasMensais()
        return sum(vendasPorMes.values()) / len(vendasPorMes) if vendasPorMes else 0
   
    def totalVendas(self):
        return sum(venda.valor for venda in self.vendas)
   
    def totalClientes(self):
        return len(self.clientes)
   
    def maiorDiaDeVendas(self):
        vendasPorDia = self.vendasDiarias()
        if not vendasPorDia:
            return None, 0
        maiorDia = max(vendasPorDia, key=vendasPorDia.get)
        return maiorDia, vendasPorDia[maiorDia]

# exibição de opçãoes para o usuário inserir valores
def menu():
    print("Sistema de Controle de Vendas")
    print("1. Registrar venda")
    print("2. Ver média de vendas diárias")
    print("3. Ver média de vendas semanais")
    print("4. Ver média de vendas mensais")
    print("5. Ver total de vendas")
    print("6. Ver número total de clientes")
    print("7. Ver maior dia de vendas")
    print("8. Sair")

# Função para ter a data da venda do usuário
def obterData():
    while True:
        dataStr = input("Digite a data da venda (DD/MM/AAAA): ")
        try:
            data = datetime.strptime(dataStr, "%d/%m/%Y")
            return data
        except ValueError:
            print("Data inválida. Tente novamente.")

# Função para obter o valor da venda do usuário
def obterValor():
    while True:
        try:
            valor = float(input("Digite o valor da venda: "))
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")

# Função principal que controla o fluxo do programa
def main():
    sistema = SistemaDeVendas()
   
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
       
        if opcao == "1":
            data = obterData()
            cpfCliente = input("Digite o CPF do cliente: ")
            valor = obterValor()
            sistema.registrarVenda(data, cpfCliente, valor)
            print("Venda registrada com sucesso!")
       
        elif opcao == "2":
            print("Média de vendas diárias:", sistema.mediaVendasDiarias())
       
        elif opcao == "3":
            print("Média de vendas semanais:", sistema.mediaVendasSemanais())
       
        elif opcao == "4":
            print("Média de vendas mensais:", sistema.mediaVendasMensais())
       
        elif opcao == "5":
            print("Total de vendas:", sistema.totalVendas())
       
        elif opcao == "6":
            print("Número total de clientes:", sistema.totalClientes())
       
        elif opcao == "7":
            maiorDia, valor = sistema.maiorDiaDeVendas()
            if maiorDia:
                print("Maior dia de vendas:", maiorDia, "com valor de R$", valor)
            else:
                print("Nenhuma venda registrada ainda.")
       
        elif opcao == "8":
            print("Saindo do sistema. Até mais!")
            break
       
        else:
            print("Opção inválida. Tente novamente.")

def inicio():
    main()
