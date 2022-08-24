import os
import dao_game
import players

class main():
    
    #dados = dao_game.ConsultPlayer()
    team = None  
    
    print(os.system("cls"))
    
    arquivo = 'list_players.txt'
    if not players.arquivo_on(arquivo):
        players.create_arquivo(arquivo)
        
    #print(players.read_player(arquivo))
    #name = str(input("Escreva seu nome: "))
    #players.add_player_arq(arquivo, name.upper(), ano) 
    #print(players.read_player(arquivo))
    
    while True:
        team = players.menu(['Seleção de 1958','Seleção de 1962','Seleção de 1970',
                 'Seleção de 1994','Seleção de 2002','Seleção de 2022'])
        if team == 1:
            #obj = dados.open_csv("players1958.csv")
            name = str(input("Escreva seu nome: "))
            players.add_player_arq(arquivo, name.upper(), 1958)
            players.ask_player("players1958.csv")
            
        elif team == 2:
            #obj = dados.open_csv("players1962.csv")
            name = str(input("Escreva seu nome: "))
            players.add_player_arq(arquivo, name.upper(), 1962)
            players.ask_player("players1962.csv")
            
        elif team == 3:
            #obj = dados.open_csv("players1970.csv")
            name = str(input("Escreva seu nome: "))
            players.add_player_arq(arquivo, name.upper(), 1970)
            players.ask_player("players1970.csv")
            
        elif team == 4:
            #obj = dados.open_csv("players1994.csv")
            name = str(input("Escreva seu nome: "))
            players.add_player_arq(arquivo, name.upper(), 1994)
            players.ask_player("players1994.csv")
            
        elif team == 5:
            #obj = dados.open_csv("players2002.csv")
            name = str(input("Escreva seu nome: "))
            players.add_player_arq(arquivo, name.upper(), 2002)
            players.ask_player("players2002.csv")
            
        elif team == 6:
            #obj = dados.open_csv("players2022.csv")
            name = str(input("Escreva seu nome: "))
            players.add_player_arq(arquivo, name.upper(), 2022)
            players.ask_player("players2022.csv")
            
        else:
            print('ERRO! Digite uma opção válida!')
            break 
            
    
    
        #name_player = str(input("Escreva o nome do jogador: "))
        #dados.consult_row(name_player.upper())
        #opc = int(input("Deseja continuar? Sim[1] ou Não[0]"))
        