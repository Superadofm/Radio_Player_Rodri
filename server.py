import subprocess
import requests
from flask import Flask, Response

app = Flask(__name__)

# URL de la playlist mise à jour sur GitHub
playlist_url = "https://raw.githubusercontent.com/Superadofm/Radio_Player_Rodri/main/playlist.txt"

def get_playlist():
    """ Récupère les URLs des musiques depuis la playlist """
    response = requests.get(playlist_url)
    if response.status_code == 200:
        # Retourner chaque ligne de la playlist qui est déjà une URL complète
        return [line.strip() for line in response.text.splitlines() if line.strip()]
    else:
        print("Erreur lors du chargement de la playlist.")
        return []

def generate_stream():
    """ Génère un flux audio à partir des fichiers dans la playlist """
    playlist = get_playlist()

    if not playlist:
        return None  # Si la playlist est vide ou ne se charge pas
    
    # Créer la commande ffmpeg avec la playlist
    input_files = []
    for song in playlist:
        input_files.append("-i")
        input_files.append(song)

    # Ajouter les options ffmpeg pour la lecture en boucle
    command = [
        "ffmpeg",
        "-stream_loop", "-1",  # Lire en boucle
        "-re"  # Lire à la vitesse du flux
    ] + input_files + [
        "-c:a", "aac",
        "-b:a", "128k",
        "-f", "mp3",  # Format MP3 pour le flux
        "pipe:1"  # Sortie vers stdout
    ]

    # Lancer la commande ffmpeg
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process.stdout

@app.route('/stream')
def stream():
    audio_stream = generate_stream()
    if audio_stream:
        return Response(audio_stream, mimetype="audio/mp3")
    else:
        return "Erreur : Impossible de charger la playlist.", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
