import customtkinter as ctk
from funcoes import converter

# A aparecia da janela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Convertor para Audio 2.0 👍")
app.geometry("800x500")

# titulo na janela
label = ctk.CTkLabel(
    app, text="Bem-Vindo ao convertor de texto 👉 audio", font=("Helvetica", 20))
label.pack(pady=20)

# entrada onde vai se digitar o texto
entry = ctk.CTkEntry(
    master=app,
    placeholder_text="Digitar um texto para tranformar em audio...",
    width=400,
    height=200,
    corner_radius=10
)

entry.pack(pady=10, padx=10)

# caso não fique nada marcado idioma o idioma padrão será portugues
idioma = ctk.StringVar(value="pt")  # padrão

# apenas pra ver no terminal se está funcionando os botoes de seleção ex: Idioma selecionado: es


def radio_event():
    print(f"Idioma selecionado: {idioma.get()}")


# seleção em portugues
radio_pt = ctk.CTkRadioButton(
    master=app,
    text="Português",
    variable=idioma,
    value="pt",
    command=radio_event
)
radio_pt.pack(pady=5)

# selecao em ingles
radio_en = ctk.CTkRadioButton(
    master=app,
    text="Inglês",
    variable=idioma,
    value="en",
    command=radio_event
)
radio_en.pack(pady=5)

# seleção em ingles
radio_es = ctk.CTkRadioButton(
    master=app,
    text="Espanhol",
    variable=idioma,
    value="es",
    command=radio_event
)
radio_es.pack(pady=5)

# função para disparar a conversao:

# funcão para disparar a conversao que puxa a funcao converter em funcoes.py com gTTS, e cria o audio, basicamente o coração fica aqui


def disparar_conversao():
    texto_usuario = entry.get()
    idioma_selecionado = idioma.get()

    if texto_usuario:
        converter(texto_usuario, idioma_selecionado, 'meu_audio')


# botao de converter que puxa a funcao disparar_conversao
botao_converter = ctk.CTkButton(
    master=app, text="Converter", command=disparar_conversao)
botao_converter.pack(pady=5)


app.mainloop()
