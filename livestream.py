import subprocess

def start_stream():
    # Commande FFmpeg pour diffuser en direct sur YouTube
    command = [
        "ffmpeg",
        "-re",  # Lecture en temps réel du flux audio
        "-i", "https://stream.zeno.fm/hg9eg9q5quzuv",  # Flux Zeno.fm
        "-stream_loop", "-1",  # Boucle infinie du GIF
        "-i", "https://superadofm.github.io/Radio_Player_Rodri/background.gif",
        "-filter_complex", "[1:v]scale=1280:720[bg];[0:a]anull[a]",
        "-map", "[bg]",  # Vidéo = GIF en boucle
        "-map", "0:a",  # Audio = Flux Zeno.fm
        "-c:v", "libx264",
        "-preset", "medium",  # Qualité vidéo normale
        "-b:v", "2500k",
        "-c:a", "aac",
        "-b:a", "128k",
        "-f", "flv",
        "rtmp://a.rtmp.youtube.com/live2/q0m7-ev92-uh81-juw8-ctb8"  # Remplace par ta clé de stream YouTube
    ]
    
    print("🎥 Démarrage de la diffusion en direct sur YouTube...")
    subprocess.run(command)

if __name__ == "__main__":
    start_stream()
    
