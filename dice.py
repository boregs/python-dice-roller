import random as rng

chosenDice = "D20"

def printButtonPressed(button_pressed):
    global chosenDice
    chosenDice = button_pressed
    print(f"Dado escolhido: {chosenDice}")

def rolar_dado_atual(labelResult):
    global chosenDice
    lados = int(chosenDice.replace("D", ""))
    resultado = rng.randint(1, lados)

    labelResult.configure(text=str(resultado))