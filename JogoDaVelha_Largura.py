import os
import random
os.system("")

class Jogada:
    def __init__(self, i, j, elemento, peso = 2):
        self.i = i
        self.j = j
        self.elemento = elemento
        self.peso = peso

    def __repr__(self):
        return "("+str(self.i)+' ,'+str(self.j)+' ,'+str(self.peso)+")"

class No:
    def __init__(self, data, parents = None, i = 0, j = 0, peso = None):
        self.parents = parents
        self.data = data
        self.i = i
        self.j = j
        self.peso = peso

    def __repr__(self):
        return str(self.data)+'\n'+str(self.parents)

def insert_tabuleiro(tabuleiro, i, j, jogador):
    novo_tabuleiro = list(tabuleiro)
    novo_tabuleiro[i][j] = jogador
    return novo_tabuleiro

def print_tabuleiro(tabuleiro):
    for i in range(0, len(tabuleiro)): print("\033[32m%s\033[0m" % tabuleiro[i])

#verificando se a jogada é possivel
def jogador_joga(tabuleiro, input):
    if input == "1":
        if tabuleiro[0][0] != "-":
            print("\033[31m\nJogada inválida!\033[0m")
            return 0
        else:
            tabuleiro[0][0] = peca_inimiga
    elif input == "2":
        if tabuleiro[0][1] != "-":
            print("\033[31m\nJogada inválida!\033[0m")
            return 0
        else:
            tabuleiro[0][1] = peca_inimiga
    elif input == "3":
        if tabuleiro[0][2] != "-":
            print("\033[31m\nJogada inválida!\033[0m")
            return 0
        else:
            tabuleiro[0][2] = peca_inimiga
    elif input == "4":
        if tabuleiro[1][0] != "-":
            print("\033[31m\nJogada inválida!\033[0m")
            return 0
        else:
            tabuleiro[1][0] = peca_inimiga
    elif input == "5":
        if tabuleiro[1][1] != "-":
            print("\033[31m\nJogada inválida!\033[0m")
            return 0
        else:
            tabuleiro[1][1] = peca_inimiga
    elif input == "6":
        if tabuleiro[1][2] != "-":
            print("\033[31m\nJogada inválida!\033[0m")
            return 0
        else:
            tabuleiro[1][2] = peca_inimiga
    elif input == "7":
        if tabuleiro[2][0] != "-":
            print("\033[31m\nJogada inválida!\033[0m")
            return 0
        else:
            tabuleiro[2][0] = peca_inimiga
    elif input == "8":
        if tabuleiro[2][1] != "-":
            print("\033[31m\nJogada inválida!\033[0m")
            return 0
        else:
            tabuleiro[2][1] = peca_inimiga
    elif input == "9":
        if tabuleiro[2][2] != "-":
            print("\033[31m\nJogada inválida!\033[0m")
            return 0
        else:
            tabuleiro[2][2] = peca_inimiga

#arvore de busca em largura
def computador_joga(tabuleiro):
    print("\033[34m\nTabuleiro anterior:\033[0m")
    jogadas: Jogada = []
    espacos_vazio = 0
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == '-':
                play = Jogada(i, j, peca)
                espacos_vazio += 1
                if (i == 0 and j == 0) or (i == 0 and j == 2) or (i == 2 and j == 0) or (i == 2 and j == 2): play.peso = 3
                elif (i == 1 and j == 1): play.peso = 4
                jogadas.append(play)
        print(tabuleiro[i])

    if espacos_vazio == 0: print("\nDeu empate!"); return 0

    jogadas_repesadas: No = []
    #nova raiz a partir do jogo zerado ou da jogada do adversário
    raiz = No(tabuleiro)

    print("\033[34m\nTabuleiro com jogada resultante:\033[0m")
    result_win = list(ganhou(tabuleiro, peca))
    if result_win != []:
        tabuleiro[result_win[0]][result_win[1]] = peca
        print_tabuleiro(tabuleiro)
        print("\033[32m\n\"%s\" foi vitorioso!\033[0m" %peca)
        return 1
    else:
        result_inimigo = list(ganhou(tabuleiro, peca_inimiga))
        if result_inimigo == []:
            for n in range(len(jogadas)):
                novo_filho = No(insert_tabuleiro(tabuleiro, jogadas[n].i, jogadas[n].j, jogadas[n].elemento), raiz, jogadas[n].i, jogadas[n].j, jogadas[n].peso)
                novo_filho.peso = linhas_possiveis(novo_filho.i, novo_filho.j, raiz.data, peca_inimiga, peca, novo_filho.peso)
                jogadas_repesadas.append(novo_filho)
                raiz.data[jogadas[n].i][jogadas[n].j] = '-'
            melhor_jogada = jogadas_repesadas[0]
            for i in range(len(jogadas_repesadas)):
                if jogadas_repesadas[i].peso > melhor_jogada.peso: 
                    melhor_jogada = jogadas_repesadas[i]
            tabuleiro[melhor_jogada.i][melhor_jogada.j] = peca
        else: tabuleiro[result_inimigo[0]][result_inimigo[1]] = peca
        print_tabuleiro(tabuleiro)

    espacos_vazio -= 1
    if espacos_vazio == 0:
        print("\nDeu empate!")
        return 0

#check de possiveis vitórias
def ganhou(tabuleiro, peca):
    # checando linhas
    for i in range(3):
        if (tabuleiro[i][0] == peca and tabuleiro[i][1] == peca and tabuleiro[i][2] == '-'): return [i, 2]
        elif(tabuleiro[i][0] == peca and tabuleiro[i][1] == '-' and tabuleiro[i][2] == peca): return [i, 1]
        elif(tabuleiro[i][0] == '-' and tabuleiro[i][1] == peca and tabuleiro[i][2] == peca): return [i, 0]
    # checando colunas
    for i in range(3):
        if (tabuleiro[0][i] == peca and tabuleiro[1][i] == peca and tabuleiro[2][i] == '-'): return [2, i]
        elif(tabuleiro[0][i] == peca and tabuleiro[1][i] == '-' and tabuleiro[2][i] == peca): return [1, i]
        elif(tabuleiro[0][i] == '-' and tabuleiro[1][i] == peca and tabuleiro[2][i] == peca): return [0, i]

    if (tabuleiro[0][0] == peca and tabuleiro[1][1] == peca and tabuleiro[2][2] == '-'): return [2, 2]
    elif(tabuleiro[0][0] == peca and tabuleiro[1][1] == '-' and tabuleiro[2][2] == peca): return [1, 1]
    elif(tabuleiro[0][0] == '-' and tabuleiro[1][1] == peca and tabuleiro[2][2] == peca): return [0, 0]
    elif (tabuleiro[0][2] == peca and tabuleiro[1][1] == peca and tabuleiro[2][0] == '-'): return [2, 0]
    elif(tabuleiro[0][2] == peca and tabuleiro[1][1] == '-' and tabuleiro[2][0] == peca): return [1, 1]
    elif(tabuleiro[0][2] == '-' and tabuleiro[1][1] == peca and tabuleiro[2][0] == peca): return [0, 2]
    else: return []


#verificando se o jogador ganhou o jogo
def jogador_ganhou(tabuleiro, peca):
    # checando linhas
    for i in range(3):
        if (tabuleiro[i][0] == peca and tabuleiro[i][1] == peca and tabuleiro[i][2] == peca): return 1
    # checando colunas
    for i in range(3):
        if (tabuleiro[0][i] == peca and tabuleiro[1][i] == peca and tabuleiro[2][i] == peca): return 1

    if (tabuleiro[0][0] == peca and tabuleiro[1][1] == peca and tabuleiro[2][2] == peca): return 1
    elif (tabuleiro[0][2] == peca and tabuleiro[1][1] == peca and tabuleiro[2][0] == peca): return 1
    else: return 0

#Repesagem de jogada verificando as linhas possiveis de serem formadas
def linhas_possiveis(i, j, tabuleiro, peca_inimiga, peca, peso):
    # primeira linha, primeira coluna (0,0)
    if i == 0 and j == 0:
        if tabuleiro[0][1] == peca_inimiga or tabuleiro[0][2] == peca_inimiga: peso -= 1
        if tabuleiro[1][0] == peca_inimiga or tabuleiro[2][0] == peca_inimiga: peso -= 1
        if tabuleiro[1][1] == peca_inimiga or tabuleiro[2][2] == peca_inimiga: peso -= 1
        if tabuleiro[0][1] == peca or tabuleiro[0][2] == peca: peso += 1
        if tabuleiro[1][0] == peca or tabuleiro[2][0] == peca: peso += 1
        if tabuleiro[1][1] == peca or tabuleiro[2][2] == peca: peso += 1
    # primeira linha, segunda coluna (0,1)
    elif i == 0 and j == 1:
        if tabuleiro[0][0] == peca_inimiga or tabuleiro[0][2] == peca_inimiga: peso -= 1
        if tabuleiro[1][1] == peca_inimiga or tabuleiro[2][1] == peca_inimiga: peso -= 1
        if tabuleiro[0][0] == peca or tabuleiro[0][2] == peca: peso += 1
        if tabuleiro[1][1] == peca or tabuleiro[2][1] == peca: peso += 1
    # primeira linha, terceira coluna (0,2)
    elif i == 0 and j == 2:
        if tabuleiro[0][0] == peca_inimiga or tabuleiro[0][1] == peca_inimiga: peso -= 1
        if tabuleiro[1][2] == peca_inimiga or tabuleiro[2][2] == peca_inimiga: peso -= 1
        if tabuleiro[1][1] == peca_inimiga or tabuleiro[2][0] == peca_inimiga: peso -= 1
        if tabuleiro[0][0] == peca or tabuleiro[0][1] == peca: peso += 1
        if tabuleiro[1][2] == peca or tabuleiro[2][2] == peca: peso += 1
        if tabuleiro[1][1] == peca or tabuleiro[2][0] == peca: peso += 1
        # caso especial
        if tabuleiro[1][1] == peca_inimiga and tabuleiro[2][2] == peca_inimiga: peso += 4
    # segunda linha, primeira coluna (1,0)
    elif i == 1 and j == 0:
        if tabuleiro[0][0] == peca_inimiga or tabuleiro[2][0] == peca_inimiga: peso -= 1
        if tabuleiro[1][1] == peca_inimiga or tabuleiro[1][2] == peca_inimiga: peso -= 1
        if tabuleiro[0][0] == peca or tabuleiro[2][2] == peca: peso += 1
        if tabuleiro[1][1] == peca or tabuleiro[1][2] == peca: peso += 1
    # segunda linha, terceira coluna (1,2)
    elif i == 1 and j == 2:
        if tabuleiro[0][2] == peca_inimiga or tabuleiro[2][2] == peca_inimiga: peso -= 1
        if tabuleiro[1][1] == peca_inimiga or tabuleiro[1][0] == peca_inimiga: peso -= 1
        if tabuleiro[0][2] == peca or tabuleiro[2][2] == peca: peso += 1
        if tabuleiro[1][1] == peca or tabuleiro[1][0] == peca: peso += 1
    # terceira linha, primeira coluna (2,0)
    elif i == 2 and j == 0:
        if tabuleiro[1][0] == peca_inimiga or tabuleiro[0][0] == peca_inimiga: peso -= 1
        if tabuleiro[2][1] == peca_inimiga or tabuleiro[2][2] == peca_inimiga: peso -= 1
        if tabuleiro[1][1] == peca_inimiga or tabuleiro[0][2] == peca_inimiga: peso -= 1
        if tabuleiro[1][0] == peca or tabuleiro[0][0] == peca: peso += 1
        if tabuleiro[2][1] == peca or tabuleiro[2][2] == peca: peso += 1
        if tabuleiro[1][1] == peca or tabuleiro[0][2] == peca: peso += 1
        # caso especial
        if tabuleiro[1][1] == peca_inimiga and tabuleiro[2][2] == peca_inimiga: peso += 3
    # terceira linha, segunda coluna (2,1)
    elif i == 2 and j == 1:
        if tabuleiro[2][0] == peca_inimiga or tabuleiro[2][2] == peca_inimiga: peso -= 1
        if tabuleiro[1][1] == peca_inimiga or tabuleiro[0][1] == peca_inimiga: peso -= 1
        if tabuleiro[2][0] == peca or tabuleiro[2][2] == peca: peso += 1
        if tabuleiro[1][1] == peca or tabuleiro[0][1] == peca: peso += 1
    # terceira linha, terceira coluna (2,2)
    elif i == 2 and j == 2:
        if tabuleiro[2][1] == peca_inimiga or tabuleiro[2][0] == peca_inimiga: peso -= 1
        if tabuleiro[0][2] == peca_inimiga or tabuleiro[1][2] == peca_inimiga: peso -= 1
        if tabuleiro[1][1] == peca_inimiga or tabuleiro[0][0] == peca_inimiga: peso -= 1
        if tabuleiro[2][1] == peca or tabuleiro[2][0] == peca: peso += 1
        if tabuleiro[0][2] == peca or tabuleiro[1][2] == peca: peso += 1
        if tabuleiro[1][1] == peca or tabuleiro[0][0] == peca: peso += 1
    #meio (1,1)
    else:
        if tabuleiro[0][1] == peca_inimiga or tabuleiro[2][1] == peca_inimiga: peso -= 1
        if tabuleiro[2][0] == peca_inimiga or tabuleiro[0][2] == peca_inimiga: peso -= 1
        if tabuleiro[1][0] == peca_inimiga or tabuleiro[1][2] == peca_inimiga: peso -= 1
        if tabuleiro[0][0] == peca_inimiga or tabuleiro[2][2] == peca_inimiga: peso -= 1
        if tabuleiro[0][1] == peca or tabuleiro[2][1] == peca: peso += 1
        if tabuleiro[2][0] == peca or tabuleiro[0][2] == peca: peso += 1
        if tabuleiro[1][0] == peca or tabuleiro[1][2] == peca: peso += 1
        if tabuleiro[0][0] == peca or tabuleiro[2][2] == peca: peso += 1
    return peso

while True:
    peca_inimiga: str
    opcao = input("\n\033[35m  #-o-x- Jogo da Velha -x-o-#\n\033[34m[1] - Jogar contra o computador;\n[2] - Requisitar melhor jogada de um cenário específico;\n[end] - Finalizar o programa.\nInforme sua escolha:\033[0m ")
    tabuleiro = [['-', '-', '-'],
                ['-', '-', '-'],
                ['-', '-', '-']]

    if opcao == '1':
        peca_inimiga = input("\033[34mInforme a sua peça (o ou x): " + "\033[0m").upper()
        
        #setando peça do computador e verificando se a peça informada é válida
        if peca_inimiga == 'X':
            peca = 'O'
        elif peca_inimiga != 'O':
            print("\033[31m\nPeça inválida.\033[0m")
            continue
        else:
            peca = 'X'
            
        #escolhendo quem joga primeiro
        vez = random.randint(0, 1)
        while True:
            if vez == 0:
                print("\nComputador joga:")
                result = computador_joga(tabuleiro)
                if result == 0 or result == 1:
                    break
                vez = 1
            else:
                print("\033[34m\nVocê joga:\033[0m\n")
                k = 1
                for i in range(3):
                    for j in range(3):
                        if tabuleiro[i][j] == '-':
                            if k % 3 != 0: print("\033[0m%s\033[0m" %k, end = "\033[34m | \033[0m")
                            else:
                                print("\033[0m%s\033[0m" %k)
                                if k < 9: print('\033[34m--+---+---\033[0m')
                        else:
                            if k % 3 != 0: print("\033[0m%s\033[0m" %tabuleiro[i][j], end = "\033[34m | \033[0m")
                            else:
                                print("\033[0m%s\033[0m" %tabuleiro[i][j])
                                if k < 9:
                                    print('\033[34m--+---+---\033[0m')
                        k += 1
                validas = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                while True:
                    entrada_jogador = input("\n\033[34mSelecione uma posição para jogar:\033[0m ")
                    #verificando se a jogada do jogador é válida (é uma posição válida)
                    if entrada_jogador not in validas:
                        if entrada_jogador == 'end': exit()
                        print("\033[31mEntrada inválida.\033[0m Tente de novo (ou insira 'end' para sair do programa)")
                    else:
                        valid = jogador_joga(tabuleiro, entrada_jogador)
                        if valid == 0:
                            continue
                        result = jogador_ganhou(tabuleiro, peca_inimiga)
                        print_tabuleiro(tabuleiro)
                        if result != 0:
                            print("\032[32mParabéns, você ganhou! Fez o IMPOSSÍVEL!\033[0m")
                            exit()
                        vez = 0
                        break
    elif opcao == '2':
        tab = input("\033[34m\n[-] - Espaço vazio;\n[o, O] - Bola;\n[x, X] - Xis.\nInforme o estado inicial do tabuleiro (ex.: x---x---o): " + "\033[0m").upper()
        k = 0
        bolas = 0
        xis = 0
        invalid = False
        
        #verificando se a entrada do tabuleiro é válida
        for i in range(len(tab)):
            if (tab[i] != 'X' and tab[i] != 'O' and tab[i] != '-') or len(tab) != 9:
                invalid=True
                break
        if invalid:
            print("\033[31m\nEntrada inválida do tabuleiro.\033[0m")
        else:
            for i in range(3):
                for j in range(3):
                    if tab[k] == 'O':
                        bolas += 1
                    elif tab[k] == 'X':
                        xis += 1
                    tabuleiro[i][j] = tab[k]
                    k += 1
            else:
                peca = input("\033[34mInforme a peça aliada (o ou x): " + "\033[0m").upper()
                #setando peça do usuário e verificando se a peça informada é válida
                if peca == 'X': 
                    xis += 1
                    peca_inimiga = 'O'
                elif peca != 'O':
                    print("\033[31m\nPeça inválida.\033[0m")
                    continue
                else: 
                    bolas += 1
                    peca_inimiga = 'X'
                if abs(bolas - xis) > 1:
                    print("\n\033[31mTabuleiro inválido, não há jogadas a se testar nessa situação.\033[0m")
                    continue
                computador_joga(tabuleiro)
    elif opcao == 'end': exit()
    else: print("\033[31mEntrada inválida.\033[0m Tente de novo (ou insira 'end' para sair do programa)")