import customtkinter as ctk
from funcoes import converter

# A aparecia da janela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Convertor para Audio 2.0")
app.geometry("800x500")

# titulo na janela
label = ctk.CTkLabel(
    # 20 é o tamanho da fonte
    app, text="Bem-Vindo ao conversor de texto 👉 audio", font=("Helvetica", 20))
label.pack(pady=20)

# descricao da box
descricao = ctk.CTkLabel(app, text="Digite o texto abaixo:")
descricao.pack(pady=5)

# entrada onde vai se digitar o texto
caixa_texto = ctk.CTkTextbox(
    master=app,
    width=400,
    height=200,
    corner_radius=10
)

caixa_texto.pack(pady=10, padx=10)

# caso não fique nada marcado idioma o idioma padrão será portugues
idioma = ctk.StringVar(value="pt")  # padrão

# apenas pra ver no terminal se está funcionando os botoes de seleção ex: Idioma selecionado: es


def terminal_info():
    print(f"Idioma selecionado: {idioma.get()}")


# seleção em portugues
radio_pt = ctk.CTkRadioButton(
    master=app,
    text="Português",
    variable=idioma,
    value="pt",
    command=terminal_info
)
radio_pt.pack(pady=5)

# selecao em ingles
radio_en = ctk.CTkRadioButton(
    master=app,
    text="Inglês",
    variable=idioma,
    value="en",
    command=terminal_info
)
radio_en.pack(pady=5)

# seleção em ingles
radio_es = ctk.CTkRadioButton(
    master=app,
    text="Espanhol",
    variable=idioma,
    value="es",
    command=terminal_info
)
radio_es.pack(pady=5)

# função para disparar a conversao:

# funcão para disparar a conversao que puxa a funcao converter em funcoes.py com gTTS, e cria o audio, basicamente o coração fica aqui


def disparar_conversao():
    texto_usuario = caixa_texto.get("1.0", "end-1c")#"1.0" → início do texto (linha 1, posição 0) "end-1c" → até o final, ignorando o último “\n” automático
    idioma_selecionado = idioma.get()

    if texto_usuario:
        converter(texto_usuario, idioma_selecionado, 'meu_audio')


# botao de converter que puxa a funcao disparar_conversao
botao_converter = ctk.CTkButton(
    master=app, 
    text="Converter",
    command=disparar_conversao
    )
botao_converter.pack(pady=5)


app.mainloop()
