# JOGO DA FORCA
from time import sleep
import time

print('Bem-vindo ao jogo da forca')
sleep(1)
introducao = 'O jogo será conduzido da seguinte forma:\numa pessoa irá digitar a palavra secreta e a outra irá fazer suas tentativas digitando as letras\naté descobrir a palavra completa ou ser enforcada.'


def print_slowly(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

print_slowly(introducao, 0.02)
    
print()
print('BOA SORTE')
print('A pessoa que irá conduzir pode digitar')
while True:
    pal_sec = input('Palavra secreta: ').upper().strip()
    if pal_sec.isalpha() == False:
        print('Digite apenas letras sem espaço ou caracter diferente')
    else:
        break 
print(pal_sec)
sleep(2)
dica = input('Dê uma dica sobre a palavra:')
sleep(1)
for f in range(60):
    f = ''
    print(f)
quant_letr = 0
lista = []
traco = '_'
for y in pal_sec:
    quant_letr+=1
    lista.append(traco)
print('JOGO DA FORCA \nACERTE A PALAVRA ANTES DE SER ENFORCADO')
print(f'A dica para você é: {dica}')


digitadas = []
acertadas = []
tentativa = ''
print(' '.join(lista))
erros = 0


while True:
    senha = ''
    for x in lista:
        senha+=x

    if senha == pal_sec:
        print('Você acertou')
        print(f'A palavra secreta é:{senha}')
        break

    
    print()
    print('Você já digitou:')
    print(','.join(digitadas))
    print()
    tentativa = input('Digite uma letra: ')
    tentativa = tentativa.upper().strip()

    if tentativa in digitadas:
        print('Letra já digitada.')
        sleep(0.02)

    elif tentativa.isalpha() == False:
        print('Digite apenas letras')
        sleep(0.02)

    elif len(tentativa) > 1:
        print('Digite apenas um valor.')
        sleep(0.02)
    
    elif tentativa in pal_sec:
        cont = 0
        for letra in pal_sec:
            if tentativa == letra:
                lista[cont] = tentativa
            else:
                pass
            cont+=1
        acertadas.append(tentativa)
        digitadas.append(tentativa)
        sleep(0.02)
    
    else:
        digitadas.append(tentativa)
        erros +=1
        print('Você errou')
    print('X====:=\nX    :  ')
    print("X    O  " if erros>=1 else 'X')
    linha_2 = ''
    if erros ==2:
        linha_2 = '   | '
    elif erros == 3:
        linha_2 = '  \|  '
    elif erros >= 4:
        linha_2 = '  \|/'
    print(f'X {linha_2}')

    linha_3 = ''

    if erros >= 5:
        linha_3 += '    |  '
    print(f'X{linha_3}')
    linha_4 = ''
    if erros == 6:
        linha_4 += '   /   '
    elif erros == 7:
        linha_4 = '   / \  '
    print(f'X{linha_4}')
    print('X\n=================')
    if erros == 7:
        print('VOCÊ FOI ENFORCADO')
        print(f'A palavra secreta era {pal_sec}')
        break

    print(' '.join(lista))
    sleep(0.05)


    

    


        



