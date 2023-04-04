import pandas as pd
import requests
from datetime import datetime
import datetime
import pandas as pd
import requests
from datetime import datetime
import datetime

USER_ID = "YOUR_USERNAME_HERE"
TOKEN = "YOUR_TOKEN_HERE"
print('started')


# Cria uma função para ser usada em outros arquivos python
def return_dataframe():
    input_variables = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=TOKEN)
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    # Baixar todas as músicas que você ouviu nas últimas 24 horas
    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?limit=50&after={time}".format(
        time=yesterday_unix_timestamp), headers=input_variables)

    data = r.json()
    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    # Extrai apenas os bits de dados relevantes do objeto json
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    # Prepara um dicionário e o transforma em um dataframe do pandas
    song_dict = {
        "song_name": song_names,
        "artist_name": artist_names,
        "played_at": played_at_list,
        "timestamp": timestamps
    }
    song_df = pd.DataFrame(song_dict, columns=["song_name", "artist_name", "played_at", "timestamp"])
    return song_df


def Data_Quality(load_df):
    # Verifica se o DataFrame está vazio
    if load_df.empty:
        print('No Songs Extracted')
        return False

    # Aplica chaves primárias já que não sera preciso de duplicatas
    if pd.Series(load_df['played_at']).is_unique:
        pass
    else:
        # encerrar imediatamente o programa para evitar processamento adicional
        raise Exception("Primary Key Exception,Data Might Contain duplicates")

    # Verifica nulos no quadro de dados
    if load_df.isnull().values.any():
        raise Exception("Null values found")


# Escreve consultas de transformação para obter a contagem do artista
def Transform_df(load_df):
    # Aplica a lógica de transformação
    Transformed_df = load_df.groupby(['timestamp', 'artist_name'], as_index=False).count()
    Transformed_df.rename(columns={'played_at': 'count'}, inplace=True)

    # Cria uma chave primária com base no carimbo de data/hora e no nome do artista
    Transformed_df["ID"] = Transformed_df['timestamp'].astype(str) + "-" + Transformed_df["artist_name"]

    return Transformed_df[['ID', 'timestamp', 'artist_name', 'count']]


def spotify_etl():
    # Importando o song_df do Extract.py
    load_df = return_dataframe()
    Data_Quality(load_df)
    # chamando a transformação
    Transformed_df = Transform_df(load_df)
    print(load_df)
    return (load_df)


spotify_etl()