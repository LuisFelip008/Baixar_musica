import os
from yt_dlp import YoutubeDL

# Configurações
pendrive_path = r"D:\trap"  # Caminho do pendrive
urls_input = input("Digite os links do YouTube (separados por espaço ou vírgula): ")

# Divide os links em uma lista, removendo espaços extras
urls = [url.strip() for url in urls_input.replace(',', ' ').split() if url.strip()]

# Verifica se pelo menos um link foi fornecido
if not urls:
    print("Nenhum link fornecido!")
    exit()

# Cria a pasta no pendrive se não existir
if not os.path.exists(pendrive_path):
    os.makedirs(pendrive_path)
    print(f"Pasta {pendrive_path} criada no pendrive.")

# Configurações do yt-dlp para baixar como MP3
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(pendrive_path, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg_location': r"C:\Users\luisf\Downloads\ffmpeg\bin\ffmpeg.exe",  # Caminho exato do ffmpeg
    'ignoreerrors': True  # Ignora erros em vídeos indisponíveis
}

# Baixa as músicas
try:
    with YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            print(f"Baixando: {url}")
            ydl.download([url])
    print("Todos os downloads concluídos com sucesso!")
except Exception as e:
    print(f"Erro ao baixar: {e}")#