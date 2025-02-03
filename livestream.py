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
        "-f", "concat", "-safe", "0",  # Lecture séquentielle de la playlist
        "-protocol_whitelist", "file,http,https,tcp,tls",  # Autoriser les URLs GitHub Pages
        "-i", "https://superadofm.github.io/Radio_Player_Rodri/playlist.m3u",  # Playlist GitHub
        "-re",
        "-stream_loop", "-1",  # Boucle infinie pour le GIF
        "-i", "https://superadofm.github.io/Radio_Player_Rodri/background.gif",  # GIF GitHub
        "-filter_complex", "[1:v]scale=1280:720[bg];[0:a]anull[a]",
        "-map", "[bg]",
        "-map", "[a]",
        "-c:v", "libx264",
        "-preset", "medium",
        "-b:v", "2500k",
        "-c:a", "aac",
        "-b:a", "128k",
        "-f", "flv",
        "rtmp://a.rtmp.youtube.com/live2/q0m7-ev92-uh81-juw8-ctb8"  # Remplace par ta clé YouTube
    ]
    
    
    print("Démarrage de la diffusion en direct...")
    subprocess.run(command)

if __name__ == "__main__":
    start_stream()
