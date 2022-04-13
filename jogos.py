import forca
import adivinhacao


def escolhe_jogo():
    print("************************************")
    print("******  Escolha o seu jogo    ******")
    print("************************************")

    print("(1) Forca (2) Adivinhaçao")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        print("Você escolheu o jogo da Forca")
        forca.jogar()
    elif jogo == 2:
        print("Você escolheu o jogo de adivinhação")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()
