from customtkinter import *
import dice

app = CTk(fg_color="#020103")
app.geometry("800x500")
app.title("Tem Dado em Casa?")
app.grid()
app.grid_columnconfigure(0, weight=3)
app.grid_columnconfigure(1, weight=1) 
app.grid_rowconfigure(0, weight=1)

btnsFrame = CTkFrame(master=app, fg_color="transparent")
btnsFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

resultsFrame = CTkFrame(master=app, fg_color="transparent")
resultsFrame.grid(row=0, column=0, sticky="nsew")

rollbtnFrame = CTkFrame(master=app, fg_color="transparent")
rollbtnFrame.grid(row=1, column=0, sticky="nsew")

resultsFrame.grid_columnconfigure(0, weight=1)
resultsFrame.grid_rowconfigure(0, weight=1)

rollbtnFrame.grid_columnconfigure(0, weight=1)
rollbtnFrame.grid_rowconfigure(0, weight=1)


diceResult = CTkLabel(master=resultsFrame, text="Tem Dado em Casa?", 
                      anchor="center", font=("Arial", 26, "bold"))
diceResult.grid(pady=10, padx=10)

rollbtn = CTkButton(master=rollbtnFrame, text="Rolar Dado", 
                    width=500, height=55, 
                    fg_color="#0a0b24", hover_color="#211e46",
                    command=lambda: dice.rolar_dado_atual(diceResult))
rollbtn.grid(row=1, column=0, padx=10, pady=10)

label_tipos = CTkLabel(master=btnsFrame, text="Tipos de Dado", font=("Arial", 16, "bold"))
label_tipos.pack(pady=20)
dados_rpg = ["D4", "D6", "D8", "D10", "D12", "D20"]
for tipo in dados_rpg:
    btn = CTkButton(master=btnsFrame, text=tipo, width=60, height=55, 
                    fg_color="#0a0b24", hover_color="#211e46", 
                    command=lambda t=tipo: dice.printButtonPressed(t))
    btn.pack(padx=10, fill="x")


app.mainloop()