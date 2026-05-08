import customtkinter as ctk
from funcoes import converter, falar

# A aparecia da janela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Convertor para Audio 2.0")
app.geometry("800x500")

# titulo na janela
label = ctk.CTkLabel(
    master=app,
    text="Bem-Vindo ao conversor de texto em audio",
    font=("Helvetica", 20)
)
label.pack(pady=20)

# descricao da box
descricao = ctk.CTkLabel(
    master=app,
    text="Digite o texto abaixo:",
    font=("Helvetica", 15)
)
descricao.pack(pady=5)

# entrada onde vai se digitar o texto
caixa_texto = ctk.CTkTextbox(
    master=app,
    width=400,
    height=200,
    corner_radius=10
)

caixa_texto.pack(pady=10)

# caso não fique nada marcado idioma o idioma padrão será portugues
idioma = ctk.StringVar(value="pt")  # padrão, varialvel de controle

frame = ctk.CTkFrame(
    master=app,
    fg_color="transparent"
)
frame.pack(pady=10)

radio_pt = ctk.CTkRadioButton(
    master=frame,
    text="Português",
    variable=idioma,
    value="pt"
)
radio_pt.pack(side="left", padx=20)

radio_en = ctk.CTkRadioButton(
    master=frame,
    text="Inglês",
    variable=idioma,
    value="en"
)
radio_en.pack(side="left", padx=20)

radio_es = ctk.CTkRadioButton(
    master=frame,
    text="Espanhol",
    variable=idioma,
    value="es"
)
radio_es.pack(side="left", padx=20)

# funcão para disparar a conversao que puxa a funcao converter em funcoes.py com gTTS, e cria o audio, basicamente o coração fica aqui


def disparar_conversao():
    # "1.0" → início do texto (linha 1, posição 0) "end-1c" → até o final, ignorando o último “\n” automático
    texto_usuario = caixa_texto.get("1.0", "end-1c")
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

botao_falar = ctk.CTkButton(
    master=app,
    text="Falar",
    command=falar,
)

botao_falar.pack(pady=5)

app.mainloop()
