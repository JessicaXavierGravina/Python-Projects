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

# Conectando ao banco de dados
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('my_played_tracks.sqlite')
    cursor = conn.cursor()
    print("Banco de dados aberto com sucesso")

# Deleta as tabelas
    cursor.execute('DROP TABLE my_played_tracks')
    cursor.execute('DROP TABLE fav_artist')

    conn.close()
    print("Banco de dados fechado com sucesso")