import math
import random 
import math

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

    
class JogadorComputadorIA(Jogador):
    def __init__(self,letra):
        super().__init__(letra)
    
    def obtem_movimento(self, jogo):
    
        if (len(jogo.movimentos_validos())==9): # primeiro movimento aleatório
            posicao= random.choice(jogo.movimentos_validos())
        else :
            #obtém o melhor movimento pelo algoritmo de minimax 
            posicao= self.minimax(jogo,self.letra)['posicao']
        
        return posicao 
    
    def minimax(self,estado,jogador):
        maximizador = self.letra
        outro_jogador = 'O' if jogador=='X' else 'X'

        if estado.ganhador_atual==outro_jogador:
            return {'posicao':None,
            'pontuacao': (1*(estado.num_posicoes_livres()+1) if outro_jogador==maximizador else (-1*( estado.num_posicoes_livres()+1)) )
            } # fórmula = 1* movimentos restantes, pois queremos ganhar o mais cedo possível
        elif estado.posicao_livre()==0 :
            return {'posicao':None,'pontuacao':0} # caso não exista mais movimentos possíveis
        
        if jogador == maximizador:
            melhor={'posicao':None, 'pontuacao':-math.inf} # para o maximizador, qualquer jogada é melhor que - infinito
        else :
            melhor={'posicao':None, 'pontuacao':math.inf} # para o minimizador, qualquer jogada é melhor que + infinito 
        
        for movimento_possivel in estado.movimentos_validos():
            #Recursão : realiza jogada e alterna jogador 
            estado.realiza_jogada(movimento_possivel,jogador)
            pontuacao_simulada = self.minimax(estado, outro_jogador)

            estado.tabuleiro [movimento_possivel]=' '
            estado.ganhador_atual = None
            pontuacao_simulada ['posicao']= movimento_possivel

            # Escolhe o melhor movimento 

            if (jogador == maximizador):
                if (pontuacao_simulada['pontuacao'] > melhor['pontuacao']):
                    melhor = pontuacao_simulada
            else :
                if (pontuacao_simulada['pontuacao'] < melhor['pontuacao']):
                    melhor = pontuacao_simulada

        return melhor



