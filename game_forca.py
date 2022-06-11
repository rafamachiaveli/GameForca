# Importando pacote
import random

# Criando a parte visual do boneco
board = ['''
>>>>>>>>>>Jogo da Forca<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Criando classe
class Hangman:

    # Metodo Construtor
    def __init__(self, word):
        self.word = word
        # Criando duas listas vazias
        self.missed_letters = []
        self.guessed_letters = []

    # Metodo para adivinhar a letra
    def guess(self, letter):
        # Se a letra estiver dentro da palavra e a letra não estiver
        # na lista de letras corretas ele ira fazer um append
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        # Se a letra nao estiver na palavra e nao estiver na lista de
        # palavras erradas, ira adicionar na lista de palavra erradas
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    # Metodo para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letters) == 6)

    # Metodo para verificar se o jogador venceu com base nos espacos sobrando
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Metodo para nao mostrar a letra no board
    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    # Metodo para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.missed_letters)])
        print('\nPalavra: ' + self.hide_word())
        print('\nLetras erradas: ', )
        for letter in self.missed_letters:
            print(letter, )
        print()
        print('Letras corretas: ', )
        for letter in self.guessed_letters:
            print(letter, )
        print()


# Método para ler uma palavra de forma aleatoria do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Metodo Main - Execução do Programa
def main():
    # Criando instancia do objeto
    game = Hangman(rand_word())

    # Enquanto o jogo nao tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        user_input = input('\nDigite uma letra: ')
        game.guess(user_input)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()