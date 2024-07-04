import pandas as pd
import openpyxl
from openpyxl.styles import Alignment


class p_excel:
    def __init__(self, filename):
        self.filename = filename
        self.df = pd.read_excel(self.filename)


    def b_col(self,n_col : str): #Buscar Coluna
        return self.df[n_col]
 
    def e_col(self,n_col:str ,date: list): #Editar uma Coluna
        self.df[n_col] = date
        self.df.to_excel('dados1.xlsx', index=False, sheet_name='Pessoas')
        return True
    
    def n_col(self,n_col:str,date: list): #Adiciona nova Coluna
        if n_col not in self.df.head():
            self.df[n_col] = date
            self.df.to_excel('dados1.xlsx', index=False, sheet_name='Pessoas')
            return True
        return False



if __name__ == "__main__":
    excel = p_excel('dados.xlsx')
    print(excel.b_col('codigos'))
    print(excel.b_col('valor')) 

    excel.n_col('n_valor',[10.2,13.2,14.5,16.7,18.9])
    print(excel.b_col('n_valor')) 

    excel.e_col('n_valor',[20.2,23.2,24.5,26.7,28.9])
    print(excel.b_col('n_valor')) 