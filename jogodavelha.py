X = input("Digite o nome do player 1(X): ")
O = input("Digite o nome do player2(O): ")
c1 = 1
c2 = 2
c3 = 3
c4 = 4                                          #Aqui pedimos o nome dos players e definimos as variáveis.
c5 = 5
c6 = 6
c7 = 7
c8 = 8
c9 = 9
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def tabuleiro():
    print (c1, "|", c2, "|", c3)
    print ("--+---+--")
    print (c4, "|", c5, "|", c6)                #Aqui definimos o tabuleiro
    print ("--+---+--")
    print (c7, "|", c8, "|", c9)
tabuleiro()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while(True):
    jog = int(input("Digite a casa na qual quer jogar: "))
    if jog == c1:
        c1 = "X"
    elif jog == c2:
        c2 = "X"
    elif jog == c3:
        c3 = "X"
    elif jog == c4:
        c4 = "X"
    elif jog == c5:
        c5 = "X"                                #Dentro do while, temos o pargunta da casa na qual o jogador quer jogar, também temos a subtituição da variável, colocando X na casa escolhida.
    elif jog == c6:
        c6 = "X"
    elif jog == c7:
        c7 = "X"
    elif jog == c8:
        c8 = "X"
    elif jog == c9:
        c9 = "X"
    else:
        print("Valor inválido! Você deve digitar uma casa existente!")
    tabuleiro()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    jog2 = int(input("Digite a proxima jogada: "))
    if jog2 == c1:
        c1 = "O"
    elif jog2 == c2:
        c2 = "O"
    elif jog2 == c3:
        c3 = "O"
    elif jog2 == c4:
        c4 = "O"
    elif jog2 == c5:
        c5 = "O"                                #Igualmente ao bloco anterior, temos a pergunta e a substituição da casa, mas agora por O.
    elif jog2 == c6:
        c6 = "O"
    elif jog2 == c7:
        c7 = "O"
    elif jog2 == c8:
        c8 = "O"
    elif jog2 == c8:
        c9 = "O"
    else:
        print("Valor inválido! Você deve digitar uma casa existente!")
    tabuleiro()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if c1 == "X" and c4 == c1 and c7 == c1:
        print ("O vencedor eh o " + str(X) + "!")
        break
    elif c1 == "O" and c4 == c1 and c7 == c1:
        print ("O vencedor eh o " + str(O) + "!")
        break
    elif c1 == "X" and c2 == c1 and c3 == c1:
        print ("O vencedor eh o " + str(X) + "!")
        break
    elif c1 == "O" and c2 == c1 and c3 == c1:
        print ("O vencedor eh o " + str(O) + "!")
        break
    elif c1 == "X" and c5 == c1 and c9 == c1:
        print ("O vencedor eh o " + str(X) + "!")
        break
    elif c1 == "O" and c5 == c1 and c9 == c1:
        print ("O vencedor eh o " + str(O) + "!")
        break
    elif c2 == "X" and c5 == c2 and c8 == c2:
        print ("O vencedor eh o " + str(X) + "!")
        break
    elif c2 == "O" and c5 == c2 and c8 == c2:
        print ("O vencedor eh o " + str(O) + "!")
        break                                                               #Por fim, temos a verificação de todas as posiveis vitórias de um dos players, seguido da mensagem da vitória.
    elif c4 == "X" and c5 == c4 and c6 == c4:
        print ("O vencedor eh o " + str(X) + "!")
        break
    elif c4 == "O" and c5 == c4 and c6 == c4:
        print ("O vencedor eh o " + str(O) + "!")
        break
    elif c7 == "X" and c8 == c7 and c9 == c7:
        print ("O vencedor eh o " + str(X) + "!")
        break
    elif c7 == "O" and c8 == c7 and c9 == c7:
        print ("O vencedor eh o " + str(O) + "!")
        break
    elif c7 == "X" and c5 == c7 and c3 == c7:
        print ("O vencedor eh o " + str(X) + "!")
        break
    elif c7 == "O" and c5 == c7 and c3 == c7:
        print ("O vencedor eh o " + str(O) + "!")
        break
    elif c9 == "X" and c6 == c9 and c3 == c9:
        print ("O vencedor eh o " + str(X) + "!")
        break
    elif c9 == "O" and c6 == c9 and c3 == c9:
        print ("O vencedor eh o " + str(O) + "!")
        break
