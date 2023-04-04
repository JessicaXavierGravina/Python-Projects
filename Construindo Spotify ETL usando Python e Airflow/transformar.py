import Extract
import pandas as pd


# Conjunto de verificações de qualidade de dados necessários para executar antes do carregamento
def Data_Quality(load_df):
    # Verifica se o DataFrame está vazio
    if load_df.empty:
        print('No Songs Extracted')
        return False


    #Aplica chaves primárias já que não precisa de duplicatas
    if pd.Series(load_df['played_at']).is_unique:
        pass
    else:
        # A razão para usar a exceção é encerrar imediatamente o programa e evitar processamento adicional
        raise Exception("Primary Key Exception,Data Might Contain duplicates")

    # Verifica nulos em nosso quadro de dados
    if load_df.isnull().values.any():
        raise Exception("Valores nulos encontrados")


# escreve algumas consultas de transformação para obter a contagem do artista
def Transform_df(load_df):
    # Aplicando lógica de transformação
    Transformed_df = load_df.groupby(['timestamp', 'artist_name'], as_index=False).count()
    Transformed_df.rename(columns={'played_at': 'count'}, inplace=True)

    # Cria uma chave primária com base no carimbo de data/hora e no nome do artista
    Transformed_df["ID"] = Transformed_df['timestamp'].astype(str) + "-" + Transformed_df["artist_name"]

    return Transformed_df[['ID', 'timestamp', 'artist_name', 'count']]


if __name__ == "__main__":
    # Importando o song_df do extrair.py
    load_df = extrair.return_dataframe()
    Data_Quality(load_df)
    # chamando a transformação
    Transformed_df = Transform_df(load_df)
    print(Transformed_df)