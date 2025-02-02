from flask import Flask, Response
import subprocess
import requests

app = Flask(__name__)

# URL du fichier playlist.txt sur GitHub
PLAYLIST_URL = "https://raw.githubusercontent.com/Superadofm/Radio_Player_Rodri/main/playlist.txt"

def download_playlist():
    """ Télécharge et retourne la playlist en concaténant les fichiers. """
    response = requests.get(PLAYLIST_URL)
    if response.status_code == 200:
        lines = response.text.strip().split("\n")
        file_list = "|".join(lines)  # Concaténer les fichiers MP3
        return f"concat:{file_list}"
    else:
        return None

def generate_stream():
    """ Génère un flux audio depuis la playlist avec lecture en boucle """
    playlist = download_playlist()
    if not playlist:
        return None  # Erreur si la playlist ne peut pas être téléchargée
    
    command = [
        "ffmpeg",
        "-stream_loop", "-1",  # 🔄 Joue la playlist en boucle
        "-re",
        "-i", playlist,
        "-c:a", "aac",
        "-b:a", "128k",
        "-f", "mp3",
        "pipe:1"
    ]
    
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
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
  
