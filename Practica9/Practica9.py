# Ariadne Selena Romero Rivero #1957540
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generar_nube_palabras(data: pd.DataFrame) -> None: 
    # Combinar los valores de la columna en un solo string
    texto = ' '.join(data["Name"].dropna().astype(str).tolist())

    # Crear la nube de palabras
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto)

    # Mostrar la nube
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Nube de palabras - {"Name"}', fontsize=20)
    plt.show()

def main():
    data = pd.read_csv("videogamesales/videogamesales_clean.csv")
    generar_nube_palabras(data)

if __name__ == "__main__":
    main()