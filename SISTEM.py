import json
import time
import os


def adicionar_cliente(clientes, nome, telefone):
    clientes[nome] = telefone

def remover_cliente(clientes, nome):
    if nome in clientes:
        del clientes[nome]

def visualizar_clientes(clientes):
    for nome, telefone in clientes.items():
        print(f'{nome}: {telefone}')
    print()
    print('Pressione enter para continuar')
    input()

def salvar_clientes(clientes, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(clientes, arquivo)

def carregar_clientes(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return json.load(arquivo)
        
def gerenciar_clientes(clientes, nome_arquivo=None):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1 - Adicionar Cliente')
        print('2 - Remover Cliente')
        print('3 - Visualizar clientes')
        print('4 - Salvar e Sair')
        print('5 - Sair sem Salvar')
        escolha = input('Escolha uma opção: ')
        if escolha == '1':
            nome = input('Digite o nome do Cliente : ')
            telefone = input('Digite o Telefone : ')
            adicionar_cliente(clientes, nome, telefone)
        elif escolha == '2':
            nome = input('Digite o nome do Cliente: ')
            remover_cliente(clientes, nome)
        elif escolha == '3':
            visualizar_clientes(clientes)
        elif escolha == '4':
            if nome_arquivo is None:
                nome_arquivo = input('Digite o Nome do Arquivo: ')
            if not nome_arquivo.endswith('.json'):
                nome_arquivo += '.json'
            salvar_clientes(clientes, nome_arquivo)
            break
        elif escolha == '5':
            break
        else:
            print('Opção Inválida')
            time.sleep(1)
            
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1 - Criar uma nova lista de clientes')
        print('2 - Carregar uma lista existente')
        print('3 - Sair')
        escolha = input('Escolha uma opção: ')
        if escolha == '1':
            clientes = {}
            gerenciar_clientes(clientes)
        elif escolha == '2':
            print('lista de clientes')
            arquivos = [arquivo for arquivo in os.listdir() if arquivo.endswith('.json')]
            if not arquivos:
                print('Nenhum arquivo encontrado.')
                time.sleep(2)
                continue
            for i, arquivo in enumerate(arquivos):
                print(f'{i + 1} - {arquivo}')
            escolha = int(input('Escolha um arquivo: (0 se não quiser escolher nenhum) '))
            if escolha == 0:
                continue
            if escolha < 0 or escolha > len(arquivos):
                print('Opção inválida')
                time.sleep(1)
                continue
            clientes = carregar_clientes(arquivos[escolha - 1])
            gerenciar_clientes(clientes, arquivos[escolha - 1])
        elif escolha == '3':
            break
        else:
            print('Opção Inválida')
            time.sleep(1)
        
    
if __name__ == '__main__':
    main()