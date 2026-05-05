from gtts import gTTS



def converter(texto, idioma, nome_arquivo):
    audio = gTTS(text=texto, lang=idioma, slow=False)


    audio.save(nome_arquivo + ".mp3")


    print("Áudio salvo como: " + nome_arquivo + ".mp3")