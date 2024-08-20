from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def descargarVideoComoMP3(url, download_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        print(f"Descargando: {yt.title}")
        audio_file = stream.download(output_path=download_path)
        
        base, ext = os.path.splitext(audio_file)
        mp3_file = base + '.mp3'
        
        audio_clip = AudioFileClip(audio_file)
        audio_clip.write_audiofile(mp3_file)
        audio_clip.close()
        
        os.remove(audio_file)  # Elimina el video, si se quiere conservar solo hay que borrar o comentar esta linea
        
        print(f"Descargado y convertido: {yt.title}")
    except Exception as e:
        print(f"Fallo al descargar {url}: {e}")

def main():
    # Lista de URLs de YouTube
    video_urls = [

        #Colocar las URL de los videos de YouTube en este array
    ]
    
    # Directorio de descarga
    download_path = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(download_path, exist_ok=True)
    
    for url in video_urls:
        try:
            descargarVideoComoMP3(url, download_path)
        except Exception as e:
            print(f"Fallo al descargar {url}: {e}")
            continue
        
    print("Todas las descargas completadas!")

if __name__ == "__main__":
    main()
