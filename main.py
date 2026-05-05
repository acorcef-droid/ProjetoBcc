
import customtkinter as ctk
from gtts import gTTS

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Convertor para Audio 2.0 👍")
app.geometry("800x400")

label = ctk.CTkLabel(app, text="Bem-Vindo ao convertor de texto 👉 audio", font=("Helvetica", 20))
label.pack(pady=20)

entry = ctk.CTkEntry(
    master=app,
    placeholder_text="Digitar um texto para tranformar em audio...",
    width=400,
    height=50,
    corner_radius=10
)

entry.pack(pady=10, padx=10)

idioma = ctk.StringVar(value="off")

def checkbox_event():
    print(f"Checkbox is {idioma.get()}")

checkbox = ctk.CTkCheckBox(
    master=app,
    text="Portugues",
    command=checkbox_event,
    variable=idioma,
    onvalue="pt",
    offvalue="off"
)
checkbox.pack(pady=10)

def converter(texto, idioma, nome_arquivo):
    audio = gTTS(text=texto, lang=idioma, slow=False)


    audio.save(nome_arquivo + ".mp3")


    print("Áudio salvo como: " + nome_arquivo + ".mp3")

def disparar_conversao():
    texto_usuario = entry.get()

    if texto_usuario:
        converter(texto_usuario, idioma,'meu_audio')

get_button = ctk.CTkButton(master=app, text="Converter", command=disparar_conversao)
get_button.pack(pady=5)



app.mainloop()