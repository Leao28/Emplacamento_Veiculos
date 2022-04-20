# import python library
import pandas as pd

# creating the list comprising the years of interest
Periodo = [*range(2016, 2023, 1)]

# creating a list with the dataframes
lista_DataFrames = []
for i in range(len(Periodo)):
    df = pd.read_csv(f'Output/DataFrame_Vertical_{Periodo[i]}.csv', sep = ';', encoding = 'utf-8')
    lista_DataFrames.append(df)

#concatenating the list into a dataframe
df = pd.concat(lista_DataFrames)
df.index = range(df.shape[0])

# Exporting DataFrames in .csv
df.to_csv(f'Output/DataFrame_Emplacamentos.csv', sep = ';', encoding = 'UTF-8', index = False)
print('\nO DataFrame foi importado com sucesso.\n')