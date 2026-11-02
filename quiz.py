import random
namn = input("Vad heter du? ")
print(f"Hej {namn} och välkommen till spelet!")
svar = str(random.randint(1, 10))
for i in range(3):
    gissning = input(f"Försök {i+1}: Gissa talet: ")
    if gissning == svar:
        print("Rätt gissat!")
        break
    else:
        print("Fel gissat.")