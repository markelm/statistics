import pandas as pd
import numpy as np
data = pd.read_csv('winequality.csv', header =(0), usecols = ['volatile acidity', 'quality'])
print('numero linhas: ', data.shape)
data.head(25)
data = data.drop_duplicates()
data.head(25)
print('numero linhas e colunas: ', data.shape)
#print(data)

df = pd.DataFrame(data)
meanX = df['volatile acidity'].mean()
print(f'\nMedia X (volatile acidity): {meanX}\n')
meanY = df['quality'].mean()
print(f'Media target_Y (quality): {meanY}\n')

std_devX = df['volatile acidity'].std();
print(f'Desvio Padrao X: (volatile acidity) {std_devX}\n')

std_devY = df['quality'].std();
print(f'Desvio Padrao target_Y: (quality) {std_devY}\n')

varX = df['volatile acidity'].var();
print(f'Variancia X: (volatile acidity) {varX}\n')

varY = df['quality'].var();
print(f'Variancia target_Y: (quality) {varY}\n')

medianX = df['volatile acidity'].median();
print(f'Mediana X (volatile acidity): {medianX}\n')

medianY = df['quality'].median();
print(f'Mediana target_Y (quality): {medianY}')

print('\n....::::Coeficientes de Correlacao entre as colunas::::....\n')
print(df.corr(method='kendall'))
