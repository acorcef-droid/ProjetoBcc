from gtts import gTTS
import os

def converter(texto, idioma, nome_arquivo):
    audio = gTTS(text=texto, lang=idioma)
    
    audio.save(nome_arquivo + ".mp3")

def falar():
    
    # Verifica se o arquivo existe antes de tentar abrir
    if os.path.exists("meu_audio.mp3"):
        os.system(f"start meu_audio.mp3")
