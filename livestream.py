import subprocess

def start_stream():
    # Commande FFmpeg sous forme de liste
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
        "-preset", "medium",  # Vitesse normale
        "-b:v", "2500k",
        "-c:a", "aac",
        "-b:a", "128k",
        "-f", "flv",
        "rtmp://a.rtmp.youtube.com/live2/q0m7-ev92-uh81-juw8-ctb8"  # Remplace par ta clé YouTube
    ]
    
    print("Démarrage de la diffusion en direct...")
    
    # Exécuter la commande
    subprocess.run(command)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    start_stream()
