import random
namn = input("Vad heter du? ")
print(f"Hej {namn} och välkommen till spelet!")
svar = str(random.randint(1, 10))
gissning = input("Gissa ett tal mellan 1 och 10: ")
if gissning == svar:
    print("Rätt!")
else:
    print(f"Tyvärr, det var {svar}.")