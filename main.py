from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
tempo=None

# ------    ---------------------- TIMER RESET ------------------------------- #
def resetar():
    global reps
    window.after_cancel(tempo)
    canvas.itemconfig(timer,text="00:00")
    forma.config(text="Timer")
    certinhos.config(text="")
    botao_reset.config(state=DISABLED)
    reps=0
    botao_start.config(state=ACTIVE)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def startar():
    global reps, timer
    botao_reset.config(state=ACTIVE)
    botao_start.config(state=DISABLED)
    worksec = WORK_MIN * 1
    restsec = SHORT_BREAK_MIN * 60
    long_rest = LONG_BREAK_MIN * 60
    time.sleep(1)
    if reps % 2 == 0 or reps == 0:
        forma.config(text="trabalha", fg=PINK)
        countdown(5)
    if not reps % 2 == 0:
        forma.config(text="descansa", fg=GREEN)
        countdown(restsec)
    elif reps == 6:
        forma.config(text="cansadinha è?", fg=RED)
        countdown(long_rest)
    elif reps > 6:
        canvas.itemconfig(timer, text="00:00")
        forma.config(text="Timer")
        reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps, numero_certinhos, certo, tempo
    contmin = math.floor(count / 60)
    contsec = count % 60
    if contsec % 60 == 0:
        contsec = "00"
    if 10 > int(contsec) % 60 > 0:
        contsec = f"0{contsec}"
    canvas.itemconfig(timer, text=f"{contmin}:{contsec}")
    if count > 0:
        tempo=window.after(1000, countdown, count - 1)
    if count == 0 and reps % 2 == 0 or reps == 0 and count == 0:
        certo = certo + "✅"
    certinhos.config(text=certo)
    certinhos.grid(column=2, row=4)
    if count == 0 and reps < 6:
        reps = reps + 1
        window.attributes('-topmost',1)
        startar()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
forma = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
forma.grid(column=2, row=1)

botao_start = Button(text="Start", borderwidth=2, width=10, highlightthickness=0, command=startar)  # inserir commando
botao_start.grid(column=1, row=3)

botao_reset = Button(text="Reset", borderwidth=2, width=10, state=DISABLED, highlightthickness=0, command=resetar)
botao_reset.grid(column=3, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
imagem = PhotoImage(file=r'C:\Users\Alean\TurtleArt\tomato.png')
canvas.create_image(100, 112, image=imagem)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
certo = ""
certinhos = Label(text=certo, font=("Arial", 15, "bold"))
numero_certinhos = 0

window.mainloop()
