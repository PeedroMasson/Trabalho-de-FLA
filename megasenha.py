import random
n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)       #Aqui usamos random para sortear os números da senha.
n4 = random.randint(0, 9)
n5 = random.randint(0, 9)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
aux = 1
r1 = 0
r2 = 0      #Aqui definimos o aux para a contagem while e também as vriáveis que conterão as respostas (-1, +1 e 0).
r3 = 0
r4 = 0
r5 = 0
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while aux <= 10:
    aux += 1	
    perg1 = int(input("Digite um número que você pensa ser o primeiro (de 0 a 9): "))
    perg2 = int(input("Digite um número que você pensa ser o segundo (de 0 a 9): "))            #Aqui, já dentro do while, perguntamos os números que o usuário deve colocar.
    perg3 = int(input("Digite um número que você pensa ser o terceiro (de 0 a 9): "))
    perg4 = int(input("Digite um número que você pensa ser o quarto (de 0 a 9): "))
    perg5 = int(input("Digite um número que você pensa ser o quinto e último (de 0 a 9): "))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if perg1 == n1:
        r1 = 1
    if perg1 != n1:
        r1 = -1
    if perg1 == n2 or perg1 == n3 or perg1 == n4 or perg1 == n5:
        r1 = 0
    if perg2 == n2:
        r2 = 1
    if perg2 != n2:
        r2 = -1
    if perg2 == n1 or perg2 == n3 or perg2 == n4 or perg2 == n5:
        r2 = 0
    if perg3 == n3:
        r3 = 1
    if perg3 != n3:                                                         #Aqui temos os ifs que verificarão os números colocados pelo usuário pelo usuário.
        r3 = -1
    if perg3 == n1 or perg3 == n2 or perg3 == n4 or perg3 == n5:
        r3 = 0
    if perg4 == n4:
        r4 = 1
    if perg4 != n4:
        r4 = -1
    if perg4 == n1 or perg4 == n2 or perg4 == n3 or perg4 == n5:
        r4 = 0
    if perg5 == n5:
        r5 = 1
    if perg5 != n5:
        r5 = -1
    if perg5 == n1 or perg5 == n2 or perg5 == n3 or perg5 == n4:
        r5 = 0
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        print(r1, r2, r3, r4, r5)	
    if r1 == +1 and r2 == +1 and r3 == +1 and r4 == +1 and r5 == +1:        #No fim, temos o print que mostra os resultados dos números postos pelo usuário.
        print("Você acertou todos os digitos, parabéns!")                   #Também, a verificação se os números estão todos certos e o print que mostra a mensagem de vitória.
        break
