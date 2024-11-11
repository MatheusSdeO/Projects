# Modulos

# import ****** -  vai importar tudo da biblioteca 
# from ****** import *** -  posso estar escolhendo o valor para importar

# Bliblioteca Math
# Biblioteca para operados aritimeticos e muito mais 
# ceil - Função de arredondamento para cima
# floor - arredondamento para baixo
# trunc - Vai eliminar da vrigula para frente 
# pow - Vai realziar a potencia 
# sqrt - Calcula a raiz quadrada
# factorial - calculo de fatorial 

from math import sqrt, ceil
num =  int(input('Digite um numero: '))
print('A raiz quadrada é {}!'.format(ceil(sqrt(num))))

import random
num = random.randint(1, 10)
print(num) 

import emoji
print(emoji.emojize('O MAtheus é :Mrs._Claus:'))

# Desafio 16
# Crie um programa que lia um numero real e mostre a sua porção inteira 

from math import trunc
r = float(input('Digite um numero real: '))
print('O valor {}, tem a sua porção inteira em {}!'.format(r, trunc(r)))

# Desafio 17 
# Faça um programa que liai o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcula e mostre o comprimento da hipotenusa 

from math import sqrt, pow
c1 = int(input('Digite o valor do cateto oposto: '))
c2 = int(input("Digite o valor do cateto adjasente: "))
h = (c1**2) + (c2**2)
print('A hipotenusa deste trainagulo retangulo é {}'.format(sqrt(h)))

# Desafio 18
# Faça um programa que leia um agulo qualquer e mostre na tela o valor do seno,cosseno e tangente desse angulo 

from math import sqrt, pow
c1 = int(input('Digite o valor do cateto oposto: '))
c2 = int(input("Digite o valor do cateto adjasente: "))
h = (c1**2) + (c2**2)
print('A hipotenusa deste trainagulo retangulo é {}'.format(sqrt(h)))

print('Ja o valor do seno {}, já o seu cosseno é {}, e a sua tangente é {}'.format(c1/(sqrt(h)), c2/(sqrt(h)), c1/c2))

# Desafio 19
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ela, elndo o nome dele e escrevendo o nome escolhido 

import random

a1= input('Digite o nome do primeiro aluno: ')
a2= input('Digite o nome do segundo aluno: ')
a3= input('Digite o nome do terceiro aluno: ')
a4= input('Digite o nome do quarto aluno: ')

lista = [a1,a2,a3,a4]
r = random.choice(lista)

print('O aluno escolhido é: {}'.format(r))

# Desafio 20
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostra 
# a ordem sorteada

import random

a1= input('Digite o nome do primeiro aluno: ')
a2= input('Digite o nome do segundo aluno: ')
a3= input('Digite o nome do terceiro aluno: ')
a4= input('Digite o nome do quarto aluno: ')

lista = [a1,a2,a3,a4]
random.shuffle(lista)
print('A ordem dos alunos é: {}'.format(lista))

# Desafio 21
# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3

import pygame   
pygame.init()
pygame.mixer.music.load('Teste.OPUS')
pygame.mixer.music.play()
pygame.event.wait()