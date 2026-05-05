import customtkinter as ctk
from funcoes import converter


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Convertor para Audio 2.0 👍")
app.geometry("800x400")

label = ctk.CTkLabel(
    app, text="Bem-Vindo ao convertor de texto 👉 audio", font=("Helvetica", 20))
label.pack(pady=20)

entry = ctk.CTkEntry(
    master=app,
    placeholder_text="Digitar um texto para tranformar em audio...",
    width=400,
    height=200,
    corner_radius=10
)

entry.pack(pady=10, padx=10)

idioma = ctk.StringVar(value="off")


def checkbox_event():
    print(f"Checkbox is {idioma.get()}")


checkbox = ctk.CTkCheckBox(
    master=app,
    text="inglês",
    command=checkbox_event,
    variable=idioma,
    onvalue="es",
    offvalue="off"
)
checkbox.pack(pady=10)

# função para disparar a conversao:


def disparar_conversao():
    texto_usuario = entry.get()
    idioma_selecionado = idioma.get()

    if texto_usuario:
        if idioma_selecionado == "off":
            idioma_selecionado = "pt"  # lingua padrão caso n selecione nada
        converter(texto_usuario, idioma_selecionado, 'meu_audio')


botao_converter = ctk.CTkButton(
    master=app, text="Converter", command=disparar_conversao)
botao_converter.pack(pady=5)


app.mainloop()
