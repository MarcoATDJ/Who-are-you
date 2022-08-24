import pandas as pd


class ConsultPlayer():
    
    dados = None
    row_name = None    
    
    def open_csv(self, csv_file):
        try:
            self.dados = pd.read_csv(csv_file, sep=",",encoding="utf8")
        except:
            print(f"O arquivo CSV não foi aberto com sucesso!")
            return False
        else:
            print(f"O arquivo CSV foi aberto com sucesso")
            #self.print_csv()
            return True

    #def set_line(self, line_name):
        
    def print_csv(self):
        print(self.dados)
            
    def consult_row(self, name_player):
            if name_player in str(self.dados["Nome"].str.upper()):
                print(f'Jogador existe')
                indice = self.dados.index[self.dados["Nome"].str.upper() == name_player].to_list()
                print(indice)
                #print(f'{self.dados.index[self.dados["Nome"].str.upper() == name_player]}')
            else:
                print(f'Jogador não existe!')
                