import os
import dao_game

def arquivo_on(name_arq):
    try:
        arq = open(name_arq, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True

        
def create_arquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('ERRO ao abrir o arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
        

def read_player(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        print(arquivo.readlines())
        


def add_player_arq(arquivo, name='', year=0):
    #names_players = {name: name,
     #               edition: year}
    
    try:
        arquivo = open(arquivo, 'at')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        try:
            arquivo.write(f'\n{name};{year}')
        except:
            print('ERRO ao registrar jogador!')
        else:
            print(f'Novo registro de {name} cadastrado.')
            arquivo.close()

def top(txt):
    print('-'*42)
    print(txt.center(42))
    print('-'*42)
    
def read_int(opcao):
    while True:
        try:
            opc = int(input(opcao))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return opc
        

       
def menu(list):
    print(os.system("cls"))
    top('ESCOLHA SUA SELEÇÃO!')
    cont = 1
    for item in list:
        print(f'{cont} - {item}')
        cont+=1
    print('-'*42)
    opc = read_int('Digite sua opção: ')
    return opc


def ask_player(year:str):
    
    dados = dao_game.ConsultPlayer()
    obj = dados.open_csv(year)
    opc = 1
    
    while opc != 0:
        name_player = str(input("Escreva o nome do jogador: "))
        dados.consult_row(name_player.upper())
        opc = int(input("Deseja continuar? Sim[1] ou Não[0]"))