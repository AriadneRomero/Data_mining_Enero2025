# Ariadne Selena Romero Rivero #1957540 Practica#1 Mineria de datos

# import opendatasets as od
# dataset_link = "https://www.kaggle.com/datasets/gregorut/videogamesales"
# od.download(dataset_link)
# import os
# os.chdir("./videogamesales")
# os.listdir()

import pandas as pd
data = pd.read_csv("Practica1/videogamesales/vgsales.csv")

# Change Nan for Not specified in Publisher
data['Publisher'] = data['Publisher'].fillna('Not specified')

# Convert to datetime
data['Year'] = pd.to_datetime(data['Year'], format='%Y')

# DELETE null data
data.dropna(subset=['Year'], inplace=True)

print(data)
data.to_csv("videogamesales/videogamesales_clean.csv", index=False)