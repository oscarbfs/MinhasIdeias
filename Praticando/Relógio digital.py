from tkinter import *
import time


def relogio_digital():
    tempo = time.strftime("%H:%M:%S")
    mostrador.config(text=tempo)
    mostrador.after(200, relogio_digital)


# Janela de aplicação
janela = Tk()
janela.title("Relogio Digital")
janela.geometry("420x150")
janela.resizable(0, 0)

mostrador = Label(janela, font=("Boulder", 68, "bold"), bg="#000000", fg="white", bd=25)
mostrador.grid(row=8, column=1)

relogio_digital()
janela.mainloop()
