import subprocess
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Bienvenue sur la radio en ligne !"

@app.route("/start-stream")
def start_stream():
    playlist_url = "https://superadofm.github.io/Radio_Player_Rodri/playlist.m3u"
    gif_url = "https://superadofm.github.io/Radio_Player_Rodri/background.gif"
    
    # Commande FFmpeg pour lire la playlist en boucle et le GIF en fond
    command = [
        "ffmpeg", 
        "-re", 
        "-f", "concat", 
        "-safe", "0", 
        "-protocol_whitelist", "file,http,https,tcp,tls", 
        "-i", playlist_url,  # Utilisation du lien direct vers la playlist
        "-re", 
        "-stream_loop", "-1", 
        "-i", gif_url,  # Utilisation du lien direct vers le GIF
        "-filter_complex", "[1:v]scale=1280:720[bg];[0:a]anull[a]",
        "-map", "[bg]",
        "-map", "[a]",
        "-c:v", "libx264",
        "-preset", "medium",  # Réglage normal pour la vitesse
        "-b:v", "2500k", 
        "-c:a", "aac", 
        "-b:a", "128k", 
        "-f", "flv", 
        "rtmp://a.rtmp.youtube.com/live2/YOUR-STREAM-KEY"  # Remplace avec ta clé de stream YouTube
    ]
    
    print("Démarrage de la diffusion en direct...")
    # Exécution de la commande FFmpeg dans un processus séparé
    subprocess.Popen(command)  # Utilisation de Popen pour éviter de bloquer le thread principal

    return jsonify({"status": "Démarrage de la diffusion en direct", "message": "Stream lancé avec succès."})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    
