print("************************************")
print("* Bem vindo ao jogo de adivinhação *")
print("************************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")

chute = int(chute_str)

print("Você digitou: ", chute)

acertou = chute == numero_secreto
maior   = chute >  numero_secreto
menor   = chute <  numero_secreto

if acertou:
    print("Você acertou !")
else:
    if maior:
        print("Você errou ! O seu chute foi maior que o número secreto.")
    elif menor:
        print("Você errou ! O seu chute foi menor que o número secreto.")

print("Fim do jogo ")