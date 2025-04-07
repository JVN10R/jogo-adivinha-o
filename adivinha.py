import random
print("===jogo da adivinhação===")
numero_secreto= random.randint(1,10)
tentativas=0

while True:
    chute= input("chuta um número entre 1 e 10:")

    if not chute.isdigit():
        print("Só vale número, hein!")
        continue

    chute=int(chute)
    tentativas += 1

    if chute ==numero_secreto:
        print(f"Acertou!Era{numero_secreto}. Tentativas:{tentativas}")
        break
    elif chute <numero_secreto:
        print("Muito baixo")
    else:
        print("Muito alto")

  