import random
from unidecode import unidecode

#SISTEMA DE JOGO MULTIPLAYER
#SISTEMA DE DIFICULDADE
#

class ForcaJogo:
    def __init__(self):
        self.vidaMaxima = 6
        self.palavra = self.palavraRandom()
        self.letraAdivinhada = []
        self.vidas = self.vidaMaxima

    def palavraRandom(self):
        with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
            palavras = [linha.strip() for linha in arquivo]
        return random.choice(palavras)

    def adivinharLetra(self, letra):
        return letra in self.letraAdivinhada

    def mostrarPalavra(self):
        palavraMostrada = [letra if letra in self.letraAdivinhada else "_" for letra in self.palavra]
        print(" ".join(palavraMostrada))

    def validarEntrada(self, letra):
        if len(letra) != 1 or not letra.isalpha():
            return False

        if letra in self.letraAdivinhada:
            print(f"A letra '{letra}' já foi adivinhada anteriormente.")
            return False
        return True

    def jogarNovamente(self):
        while True:
            jogarDnovo = input("Quer jogar novamente? [S/N]: ").strip().upper()
            if jogarDnovo in ["SIM", "sim", "S", "s"]:
                return True
            elif jogarDnovo in ["NAO", "NÃO", "N", "n", "Ñ"]:
                return False
            else:
                print("DSCLP, EU NÃO FALO A LINGUA DOS BURReS...")

    def jogar(self):
        print("* * * FORCA NÃO BINARIE * * *\n"
              "só os paiaçu maluco HAHAHAHAHH")
        while self.vidas > 0:
            self.mostrarPalavra()
            letra = input("Digite uma letra: ").upper()

            if not self.validarEntrada(letra):
                print(f"Entrada Inválida")
                continue

            self.letraAdivinhada.append(letra)

            if letra not in self.palavra:
                self.vidas -= 1
                print(f"A letra {letra} não esta na palavra. Restam {self.vidas} vidas.")

            if all(c in self.letraAdivinhada for c in self.palavra):
                self.mostrarPalavra()
                print(f"Parabens!!! A palavra era: {self.palavra}")
                break

        if self.vidas == 0:
            print(f"Você perdeu, seu burro!!!\nA palavra era {self.palavra}")


if __name__ == "__main__":
    while True:
        jogo = ForcaJogo()
        jogo.jogar()

        if not jogo.jogarNovamente():
            print("PDP ENTÃO, ES DE VDD EU SEI QUEM SÃO. FALSE!!!!")
            break
