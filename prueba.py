import pandas as pd 

data_train = pd.read_csv('filter_dc3/datosEntrenamiento.csv')

print(data_train.head())

tipo= type(data_train)
print(tipo)



