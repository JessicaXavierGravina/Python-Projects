import Extract
import Transform
import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"

if __name__ == "__main__":

    # Importando o song_df do extrair.py
    load_df = Extract.return_dataframe()
    if (Transform.Data_Quality(load_df) == False):
        raise ("Falha na validação de dados"")
    Transformed_df = Transform.Transform_df(load_df)
    # Os dois quadros de dados que precisam ser carregados no banco de dados

    # Carregando no banco de dados
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('my_played_tracks.sqlite')
    cursor = conn.cursor()

    # SQL Query para criar músicas tocadas
    sql_query_1 = """
    CREATE TABLE IF NOT EXISTS my_played_tracks(
        song_name VARCHAR(200),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        timestamp VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
    )
    """
    #  Consulta SQL para criar o artista mais ouvido
    sql_query_2 = """
    CREATE TABLE IF NOT EXISTS fav_artist(
        timestamp VARCHAR(200),
        ID VARCHAR(200),
        artist_name VARCHAR(200),
        count VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (ID)
    )
    """
    cursor.execute(sql_query_1)
    cursor.execute(sql_query_2)
    print("Banco de dados aberto com sucesso")

    # anexa novos dados para evitar duplicatas
    try:
        load_df.to_sql("my_played_tracks", engine, index=False, if_exists='append')
    except:
        print("Data already exists in the database")
    try:
        Transformed_df.to_sql("fav_artist", engine, index=False, if_exists='append')
    except:
        print("Os dados já existem no banco")

    # cursor.execute('DROP TABLE my_played_tracks')
    # cursor.execute('DROP TABLE fav_artist')

    conn.close()
    print("Banco de dados fechado!")