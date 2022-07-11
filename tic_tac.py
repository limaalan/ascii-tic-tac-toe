import time
import jogador


class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [' 'for _ in range(9)] # lista de 9 elementos representado as posições do tabuleiro
        self.ganhador_atual = None 
    
    def imprime_tabuleiro(self):
        # tabuleiro[0:3] = tabuleiro [0] [1] [2]
        for linha in [self.tabuleiro[i*3:(i+1)*3] for i in range(3)]:
            print ('| ' + ' | '.join(linha) + ' |')

            # basicamente printa '| ' seguido das 3 posições da linha do tabuleiro
            # separadas por '|' e outra ' |' no final
            # nesse formato : | 1 | 2 | 3 |


    @staticmethod
    def imprime_numeros_tabuleiro():
        # imprime as posições do tabuleiro

        numeros_tabuleiro = [[str(i) for i in range (j*3, (j+1)*3)] for j in range(3)]
        
        for linha in numeros_tabuleiro:
             print ('| ' + ' | '.join(linha) + ' |')    

        #for j in range 3
        #   for i = j*3 in range (j+1)*3
        #       numeros_tabuleiro = str(i)

    
    def movimentos_validos(self):
        #retorna uma lista com os índices de movimentos válidos
        movimentos= []
        for (i, posicao) in enumerate(self.tabuleiro):
            if (posicao==' '):
                movimentos.append(i)
        return movimentos

    def posicao_livre(self):
        return ' ' in self.tabuleiro

    def num_posicoes_livres(self):
        return self.tabuleiro.count(' ')

    def realiza_jogada(self,posicao,letra):
        if self.tabuleiro[posicao]==' ':
            self.tabuleiro[posicao]=letra
            if self.ganhador(posicao,letra):
                self.ganhador_atual=letra
            return True
        return False

    def ganhador(self, posicao,letra):
        #checando as linhas
        indice_linha = posicao//3
        #0 - 2 = 0
        #3 - 5 = 1
        #6 - 8 = 2
        #Exemplo : posicao = 2
        #indice_linha = 0
        #linha = self.tabuleiro[0:3]
        #Ou seja, dado uma posição ele pega toda a linha daquela posição
        linha=self.tabuleiro[indice_linha*3 : (indice_linha+1)* 3]
        if all (p==letra for p in linha):
            return True

        #for i in linha :
        #    if i!= letra:
        #        return False
        #return True 

        #checando as colunas 
        #0 , 3 , 6 = 0
        #1 , 4 , 7 = 1
        #2 , 5 , 8 = 2
        indice_coluna = posicao%3 #descobre a qual coluna pertece a posição
        coluna = [self.tabuleiro[(i*3)+indice_coluna] for i in range(3) ]
        # indice_columa= 0 + i=0 * 3 = 0 
        # indice_columa= 0 + i=1 * 3 = 3 
        # indice_columa= 0 + i=2 * 3 = 6 

        if all (p==letra for p in coluna):
            return True

        #checando diagonais :
        # Observe que no tabuleiro, somente as posições de índice par fazem parte das diagonais
        # Portanto, se a posição for par, precisamos apenas checar entre as duas diagoais se elas criam uma linha.
        if posicao%2 ==0: 
            diagonal1=[self.tabuleiro[i] for i in [0,4,8]]
            if all (p==letra for p in diagonal1):
                return True
            diagonal2=[self.tabuleiro[i] for i in [2,4,6]]
            if all (p==letra for p in diagonal2):
                return True
        return False


def jogar(jogo,x_jogador,o_jogador,imprimir_jogo=True):
    if imprimir_jogo:
        jogo.imprime_numeros_tabuleiro()
    letra = 'X' # jogador que faz a primeira jogada

    while jogo.posicao_livre():
        if letra=='O':
            posicao=o_jogador.obtem_movimento(jogo)
        else :
            posicao=x_jogador.obtem_movimento(jogo)

        if jogo.realiza_jogada(posicao,letra):
            if imprimir_jogo:
                print(f'Jogador {letra} fez uma jogada na posição {posicao}')
                jogo.imprime_tabuleiro()
                print('') # quebra de linha

            if jogo.ganhador_atual:
                if imprimir_jogo :
                    print(letra+" ganhou!")
                return letra # retona o jogador que ganhou 

            if letra=='X': # troca a vez dos jogadores
                letra='O'
            else:
                letra='X'
            
            if imprimir_jogo:
                time.sleep(1)

            #letra = 'O' if letra == 'X' else 'X' #mesma coisa que o código acima
    if imprimir_jogo:
        print("Jogo empatou!")
    return None # quer dizer que acabou as posições livres e não há ganhador


if __name__=='__main__':
    rodadas = 25
    x=0
    o=0
    empate=0
    opcao='c'
    print("Bem vindo ao jogo da velha! ")
    while (opcao!='sair'):
        
        print("1- Player vs Player")
        print("2- Player vs IA impossível")
        print("3- Aleatório vs IA impossível")
        print("Entre sua opção ou 'sair':")
        opcao = input()

        if (opcao == '1'):
            x_jogador=jogador.JogadorHumano('X')
            o_jogador=jogador.JogadorHumano('O')
            t=JogoDaVelha()
            jogar(t,x_jogador,o_jogador,imprimir_jogo=False)
        elif (opcao=='2'):
            x_jogador=jogador.JogadorHumano('X')
            o_jogador=jogador.JogadorComputadorIA('O')
            t=JogoDaVelha()
            jogar(t,x_jogador,o_jogador,imprimir_jogo=True)
        elif (opcao=='3'):
            vezes = int(input ("Insira a quantidade de jogos a simular:"))
            for i in range ( vezes):
                x_jogador=jogador.JogadorComputador('X')
                o_jogador=jogador.JogadorComputadorIA('O')
                t = JogoDaVelha()
                resultado = jogar(t,x_jogador,o_jogador,False)
                if resultado =='X':
                    x+=1
                elif resultado =='O':
                    o+=1
                else :
                    empate +=1
                print(f"Jogo {i+1} resultado {resultado if resultado !=None else 'Empate'}: ")
    
            print(f"X ganhou {x} vezes, O ganhou {o} vezes e o jogo empatou {empate} vezes.")


        elif (opcao!='sair'):
            print("Opcao inválida !")
       