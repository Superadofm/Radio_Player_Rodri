import os
import requests
import subprocess
import time
import threading
import http.server
import socketserver

# Petit serveur HTTP factice pour Render
PORT = 10000
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"AutoDJ running...")

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Fake server running on port {PORT}")
        httpd.serve_forever()

# Lancer le serveur dans un thread séparé
threading.Thread(target=run_server, daemon=True).start()


# Liste des URLs des musiques extraites de la playlist.m3u (directement ou à partir de GitHub)
urls = [
    "https://superadofm.github.io/Radio_Player_Rodri/Musiques/Benjamin_Orth_-_Where_You_Are_Now.mp3",
    "https://superadofm.github.io/Radio_Player_Rodri/Musiques/Ghost_k_-_Stop_(One_More_Time_Remix_2011).mp3",
    "https://superadofm.github.io/Radio_Player_Rodri/Musiques/JeffSpeed68_-_2000_Lichtjahre.mp3",
    "https://superadofm.github.io/Radio_Player_Rodri/Musiques/JeffSpeed68_-_Compassion.mp3",
    "https://superadofm.github.io/Radio_Player_Rodri/Musiques/JeffSpeed68_-_Dance_or_Die.mp3",
    "https://superadofm.github.io/Radio_Player_Rodri/Musiques/JeffSpeed68_-_Drunk_With_You.mp3",
    "https://superadofm.github.io/Radio_Player_Rodri/Musiques/JeffSpeed68_-_Girls_like_you.mp3",
    "https://superadofm.github.io/Radio_Player_Rodri/Musiques/JeffSpeed68_-_I_don_t_Want_to_go_To_Sleep.mp3",
    "https://superadofm.github.io/Radio_Player_Rodri/Musiques/JeffSpeed68_-_Reckless.mp3",
    "https://superadofm.github.io/Radio_Player_Rodri/Musiques/TheDICE_-_Again_and_Again.mp3",
    "https://superadofm.github.io/Radio_Player_Rodri/Musiques/VJ_Memes_-_Soul_Searching.mp3",
    "https://superadofm.github.io/Radio_Player_Rodri/Musiques/mactonite_-_Your_Heart.mp3",
    "https://superadofm.github.io/Radio_Player_Rodri/Musiques/milkdaddy_-_Popping_Over_Here.mp3",
    "https://superadofm.github.io/Radio_Player_Rodri/Musiques/stevieb357_-_Give_It_Up.mp3",
    "https://superadofm.github.io/Radio_Player_Rodri/Musiques/stevieb357_-_Slow_Motion_Dream.mp3"
]

# Dossier de téléchargement
download_dir = "musiques/"

# Créer le dossier s'il n'existe pas
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Télécharger les fichiers audio
def download_audio(url):
    response = requests.get(url)
    file_name = os.path.join(download_dir, os.path.basename(url))
    with open(file_name, 'wb') as f:
        f.write(response.content)

# Télécharger toutes les musiques
for url in urls:
    download_audio(url)

print("Téléchargement terminé.")

# Chemin vers le GIF à utiliser en fond
input_gif = "https://superadofm.github.io/Radio_Player_Rodri/background.gif"  # Mets ici le chemin vers ton GIF

# URL de diffusion YouTube
youtube_url = "rtmp://a.rtmp.youtube.com/live2/q0m7-ev92-uh81-juw8-ctb8"  # Remplace par ta clé de flux YouTube

# Fonction pour exécuter le flux avec FFmpeg
def start_stream():
    # Commande FFmpeg pour diffuser la musique et le GIF en boucle
    ffmpeg_command = [
        'ffmpeg',
        '-re',  # Lire le fichier à la vitesse originale
        '-loop', '1',  # Pour boucler le GIF en arrière-plan
        '-i', input_gif,  # GIF comme vidéo en entrée
        '-c:v', 'libx264',  # Encoder la vidéo en H.264
        '-preset', 'veryfast',  # Préréglage pour une meilleure performance
        '-c:a', 'aac',  # Encoder l'audio en AAC
        '-b:a', '192k',  # Définir le bitrate audio
        '-f', 'flv',  # Format de sortie pour RTMP
        youtube_url  # URL YouTube Live pour diffuser
    ]

    while True:
        for audio_file in os.listdir(download_dir):
            if audio_file.endswith('.mp3'):
                audio_path = os.path.join(download_dir, audio_file)
                # Commande FFmpeg pour envoyer l'audio et le GIF à YouTube
                ffmpeg_command_audio = [
                    'ffmpeg',
                    '-re',  # Lire le fichier à la vitesse originale
                    '-i', audio_path,  # Fichier audio
                    '-i', input_gif,  # Fichier GIF
                    '-c:v', 'libx264',  # Encoder la vidéo en H.264
                    '-preset', 'veryfast',  # Préréglage pour une meilleure performance
                    '-c:a', 'aac',  # Encoder l'audio en AAC
                    '-b:a', '192k',  # Définir le bitrate audio
                    '-f', 'flv',  # Format de sortie pour RTMP
                    youtube_url  # URL YouTube Live pour diffuser
                ]
                # Exécuter la commande
                subprocess.run(ffmpeg_command_audio)

# Exécuter le flux en boucle
start_stream()
