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


command = [
        "ffmpeg",
        "-re",  # Lecture en temps réel
        "-f", "concat", "-safe", "0", "-i", "https://superadofm.github.io/Radio_Player_Rodri/playlist.m3u",  # Lecture des musiques depuis la playlist
        "-re",  # Lecture en temps réel du GIF
        "-stream_loop", "-1", "-i", "https://superadofm.github.io/Radio_Player_Rodri/background.gif",  # Boucle infinie sur le GIF
        "-filter_complex", "[1:v]scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2[bg];[0:a]asetpts=PTS-STARTPTS[a]",  
        "-map", "[bg]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "ultrafast", "-b:v", "2500k",  # Réglage vidéo
        "-c:a", "aac", "-b:a", "128k", "-ar", "44100",  # Réglage audio
        "-pix_fmt", "yuv420p",
        "-f", "flv",
        "rtmp://a.rtmp.youtube.com/live2/YOUR-STREAM-KEY"  # Remplace YOUR-STREAM-KEY par ta clé
    ]
    
    print("Démarrage de la diffusion en direct...")
    subprocess.run(command)

if __name__ == "__main__":
    start_stream()
