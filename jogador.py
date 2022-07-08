import math
import random 
from tic_tac import JogoDaVelha


class Jogador:
    def __init__(self,letra):
        self.letra = letra

    def obtem_movimento(self,jogo):
        pass

#herda a classe jogador
class JogadorComputador(Jogador):
    def __init__(self,letra):
        super().__init__(letra)
    
    def obtem_movimento(self, jogo):
        return random.choice(jogo.movimentos_validos())

class JogadorHumano(Jogador):
    def __init__(self,letra):
        super().__init__(letra)
    
    def obtem_movimento(self, jogo):
        posicao_valida = False
        val = None
        while not posicao_valida:
            posicao=input(f'vez do {self.letra}. Inisira uma posição (0-8):')

            try :
                val = int(posicao)
                if val not in jogo.movimentos_validos():
                    raise ValueError
                posicao_valida=True
            except ValueError:
                print('Posição inválida!.')
        
        return val