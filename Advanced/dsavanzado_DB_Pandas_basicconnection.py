import sqlite3
import pandas as pd


db_conexion = sqlite3.connect('C:/LMG/Nico/Curso Avanzado Python/Datasets/chinook.db')

df_cancionesxalbumSQL = pd.read_sql(
  "SELECT albums.Title,count(tracks.TrackId) as Songs  \
  FROM tracks\
  INNER JOIN albums ON tracks.AlbumId=albums.AlbumId   \
  GROUP by tracks.AlbumId" \
  , db_conexion
  )



print(df_cancionesxalbumSQL)