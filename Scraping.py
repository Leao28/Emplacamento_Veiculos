# import python libraries
import tabula
import pandas as pd
import numpy as np
import warnings
import Dict_and_List
warnings.filterwarnings("ignore")

##--------------------------------------------------------------------------------------------##
# PDF data scraping with tabula
Ano = 2021
df_1 = tabula.read_pdf(f'Dados/{Ano}/Jan_Fev_{Ano}.pdf', pages = '11-18')
df_2 = tabula.read_pdf(f'Dados/{Ano}/Mar_Abr_{Ano}.pdf', pages = '11-18')
df_3 = tabula.read_pdf(f'Dados/{Ano}/Mai_Jun_{Ano}.pdf', pages = '11-18')
df_4 = tabula.read_pdf(f'Dados/{Ano}/Jul_Ago_{Ano}.pdf', pages = '11-18')
df_5 = tabula.read_pdf(f'Dados/{Ano}/Set_Out_{Ano}.pdf', pages = '11-18')
df_6 = tabula.read_pdf(f'Dados/{Ano}/Nov_Dez_{Ano}.pdf', pages = '11-18')

# Checking the number of Dataframes that were recognized
print('\nO scraping de dados foi concluido com sucesso.')
print('\nTotal de Tabelas: \nJaneiro/Fevereiro - {};\nMarço/Abril - {}; \nMaio/Junho - {}; \nJulho/Agosto - {}; \nSetembro/Outubro - {}; \nNovembro/Dezembro - {}'
.format(str(len(df_1)), str(len(df_2)), str(len(df_3)), str(len(df_4)), str(len(df_5)), str(len(df_6))))

##--------------------------------------------------------------------------------------------##
# Write functions
# Remove unnecessary columns
def preparar_coluna(tabela):
    global dataframe
    for i in range(len(tabela)):
        if len(tabela[i].columns) == 2:
            tabela[i].drop(columns = ['Unnamed: 0'], inplace = True)
            tabela[i].columns = ['Dados']
        elif len(tabela[i].columns) == 3:
            tabela[i].drop(columns = ['Unnamed: 0', 'Unnamed: 1'], inplace = True)
            tabela[i].columns = ['Dados']
    dataframe = tabela.copy()


# Concatenate dataframe list
def concatenar(tabela, ano):
    global dataframe
    dataframe = pd.concat(tabela)
    dataframe.index = range(dataframe.shape[0])

    dataframe['Dados'] = dataframe['Dados'].str.replace(ano , 'Ano')
    dataframe['Dados'] = dataframe['Dados'].str.replace(' =', '')
    dataframe = dataframe[['Dados']]


# Set the category in which the vehicle is
def definir_categorias(tabela):
    global dataframe
    dataframe['Parametro_1'] = pd.to_numeric(tabela['Dados'].str[:1], errors = 'coerce')
    dataframe['Categoria'] = pd.isnull(tabela['Parametro_1'])

    j = 0
    for i in range(len(dataframe)):
        if i == 0:
            k = 0
        else:
            k = i - 1
        if dataframe.Categoria[i] == False:
            dataframe.Categoria[i] = Dict_and_List.Lista_Categorias[j]
        else:
            dataframe.Categoria[i] = ''
        if pd.isnull(dataframe['Parametro_1'][i]) == True and pd.isnull(dataframe['Parametro_1'][k]) == False:
            j = j + 1
        
    dataframe.dropna(inplace = True)
    dataframe['Dados'].replace(Dict_and_List.Dicionario, regex = True, inplace = True)
    dataframe.index = range(dataframe.shape[0])


# Explode one column into new columns
def expandir_dados(tabela, mes_1, mes_2):
    global dataframe
    if len(dataframe['Dados'].str.split(' ', expand=True).columns) == 4:
        dataframe[['Coluna_1', 'Coluna_2', mes_1, mes_2]] = tabela['Dados'].str.split(' ', expand=True)
    elif len(dataframe['Dados'].str.split(' ', expand=True).columns) == 5:
        dataframe[['Coluna_1', 'Coluna_2', mes_1, mes_2, 'Coluna_3']] = tabela['Dados'].str.split(' ', expand=True)
        dataframe.drop(columns = ['Coluna_3'], inplace = True)
        
    dataframe[['Fabricante', 'Modelo']] = dataframe['Coluna_2'].str.split('/', expand=True)


    dataframe['Fabricante'] = dataframe['Fabricante'].str.replace('_', ' ')

    dataframe['Modelo'] = dataframe['Modelo'].str.replace('_', ' ')
    dataframe['Modelo'] = dataframe['Modelo'].str.replace('+', '/')

    dataframe[mes_1] = dataframe[mes_1].str.replace('.', '').astype(int)
    dataframe[mes_2] = dataframe[mes_2].str.replace('.', '').astype(int)


# Setting the 'Engine Type' and 'Year' columns
def ajustes_finais(tabela, mes_1, mes_2, ano):
    global dataframe
    tabela['Motor'] = ''
    for i in range(len(tabela)):
        if tabela['Modelo'].iloc[i] in Dict_and_List.Lista_Eletricos:
            tabela['Motor'].iloc[i] = 'Elétrico'
        elif tabela['Modelo'].iloc[i] in Dict_and_List.Lista_Hibridos:
            tabela['Motor'].iloc[i] = 'Termico ou Hibrido'
        else:
            tabela['Motor'].iloc[i] = 'Termico'

    dataframe['Ano'] = ano

    dataframe.drop(columns = ['Dados', 'Parametro_1', 'Coluna_1', 'Coluna_2',], inplace = True)
    dataframe = dataframe[['Fabricante', 'Modelo', 'Categoria', 'Motor', 'Ano', mes_1, mes_2]]
    dataframe.drop(dataframe[dataframe.Categoria == 'Furgoes'].index, inplace = True )
    dataframe.index = range(dataframe.shape[0])


# Creating a function that returns the other functions
def scraping(dataframe_original, mes_1, mes_2, ano):
    global dataframe
    preparar_coluna(dataframe_original)
    concatenar(dataframe, ano)
    definir_categorias(dataframe)
    expandir_dados(dataframe, mes_1, mes_2)
    ajustes_finais(dataframe, mes_1, mes_2, ano)
    dataframe_original = dataframe.copy()
    del dataframe
    return dataframe_original

##--------------------------------------------------------------------------------------------##
# Handling the PDF scraping data
# Running the scraping function to each PDF data
df_1 = scraping(df_1, mes_1 = 'Janeiro', mes_2 = 'Fevereiro', ano = f'{Ano}')
df_2 = scraping(df_2, mes_1 = 'Março', mes_2 = 'Abril', ano = f'{Ano}')
df_3 = scraping(df_3, mes_1 = 'Maio', mes_2 = 'Junho', ano = f'{Ano}')
df_4 = scraping(df_4, mes_1 = 'Julho', mes_2 = 'Agosto', ano = f'{Ano}')
df_5 = scraping(df_5, mes_1 = 'Setembro', mes_2 = 'Outubro', ano = f'{Ano}')
df_6 = scraping(df_6, mes_1 = 'Novembro', mes_2 = 'Dezembro', ano = f'{Ano}')
print('\nAs funções foram executadas com sucesso.')

# Merging into a single DataFrame
df_horizontal = df_1.merge(df_2, on=['Fabricante', 'Modelo', 'Categoria', 'Motor', 'Ano'], how = 'outer').\
    merge(df_3, on=['Fabricante', 'Modelo', 'Categoria', 'Motor', 'Ano'], how = 'outer').\
        merge(df_4, on=['Fabricante', 'Modelo', 'Categoria', 'Motor', 'Ano'], how = 'outer').\
            merge(df_5, on=['Fabricante', 'Modelo', 'Categoria', 'Motor', 'Ano'], how = 'outer').\
                merge(df_6, on=['Fabricante', 'Modelo', 'Categoria', 'Motor', 'Ano'], how = 'outer')

# Changing column type from float to int
df_horizontal[Dict_and_List.Lista_Meses] = df_horizontal[Dict_and_List.Lista_Meses].fillna(0).astype(int)

# Converting columns to rows
df_vertical = pd.melt(df_horizontal, id_vars = ['Fabricante', 'Modelo', 'Categoria', 'Motor', 'Ano'],\
    value_vars = Dict_and_List.Lista_Meses, var_name = 'Mês', value_name = 'Qtd Emplacamentos')

# Sorting dataframe data
df_horizontal.sort_values(by = ['Fabricante'], inplace = True, ignore_index = True)
df_vertical.sort_values(by = ['Fabricante', 'Modelo'], inplace = True, ignore_index = True)

# Exporting DataFrames in .csv
df_horizontal.to_csv(f'Output/DataFrame_Horizontal_{Ano}.csv', sep = ';', encoding = 'UTF-8', index = False)
df_vertical.to_csv(f'Output/DataFrame_Vertical_{Ano}.csv', sep = ';', encoding = 'UTF-8', index = False)
print('\nOs DataFrames foram importados com sucesso.\n')
