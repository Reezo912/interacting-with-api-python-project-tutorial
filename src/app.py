import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt


# load the .env file variables
load_dotenv()

# Accedo a .env y paso las credenciales a la API de spotify
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
spotify = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Key del artista
artist_URI = 'spotify:artist:0Repe2EiNjaFAFIukrroUM'

# Almaceno las canciones de la respuesta en una variable
response = spotify.artist_top_tracks(artist_URI)

'''if response != 200:
    print('Error al obtener respuesta')
else:
    print('Se ha obtenido respuesta satisfactoria')'''
tracks = response['tracks']

# Creo una lista de las 10 primeras canciones
primeras_10_canciones = tracks[:10]

tracks_db = []

# Extraigo los datos que me importan de las primeras 10 canciones y las introduzco en una lista
for track in primeras_10_canciones:
    data = {
        "nombre": track['name'],
        "duracion": track['duration_ms'],
        "popularidad": track['popularity']
    }
    tracks_db.append(data)

# Convierto los datos en un DataFrame
df_tracks = pd.DataFrame(tracks_db)

# Me aseguro de que estan ordenadas por popularidad en orden  descendente
df_tracks_popularity = df_tracks.sort_values(by = 'popularidad', ascending=False)

# Imprimir las 3 primeras canciones del top 10
print(df_tracks_popularity.head(3))

# Crear el grafico
plt.scatter(df_tracks_popularity['duracion'], df_tracks_popularity['popularidad'] , color = 'black', marker = 'o')
plt.title('Relacion entre popularidad y duracion')
plt.xlabel('Duracion')
plt.ylabel('popularidad')

# Mostrar grafico
plt.show()