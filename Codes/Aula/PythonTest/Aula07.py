#Desafio 04
#Faça um programa que leias algo pela teclado e mostra na tela o seu tipo primitivo e todas as informações possivel sobre ele 


#a = input('Digite algo: ')
#print('O tipo primitivo desse valor é ', type(a))#Define o valor primitivo coletado pelo input, por padrão sempre sera str, pois input so coleta str, porem se definir o valor sera diferente
#print('So tem espaços? ' , a.isspace())#Define se o valor escrito é apenas espaços
#print('São somente numeros? ' , a.isnumeric())#Define se o valor escrito é apenas numeros
#print('São somente alfabetico? ' , a.isalpha())#Define se o valor escrito é apenas numerico
#print('São somente alfanumericos? ', a .isalnum())#Define se o valor escrito é alphanumerico
#print('Esta em MAIUSCULAS? ', a.isupper())#Define se o valor escrito esta em maisculo
#print('Esta em minusculas? ', a .islower())#Define se o valor escrito esta em minisculo
#print('Esta captalizada? ', a.istitle())#Define se o valor esta captalizado, ou seja não possui apenas letras minisculas ou maiusculas, sendo uma mescla


#Operadores aritimeticos 

# ' == ' =  Operação que mostra a igualdade, sendo que 1 simbulo de igual é apenas atribuição

# ' + ' =  Adição
# ' - ' =  Subtração
# ' * ' =  Multiplicação
# ' / ' =  Divisão
# ' ** ' = Potencia
# ' // ' = Divisão inteira, dividir sem usa virgula
# ' % ' = Resto da divisão, o que sobra da divisão inteira 
# ' Raiz Quadrada ' = valor**(1/2) == Raiz quadrada

#Ordem de precedencia (serão executados primeiro)

#1º - ()
#2º - **
#3º - * - / - // - %
#4º - + - -

#Operadores mais funções

#print('='*20)

#No console ira apresentar o '=' vinte vezes 

#Operadores 

#nome = input('Qual seu nome? ')
#print('Prazer em te conhecer {:> / < / ^}!'.format(nome))#Ira escrever o 'nome' com 20 espaços, uma adição pode ser colocar um '=', aonde ele colcocara o nome completando 
#os espaços que sobram juntos com os caracteres do '='
# > -  Aloca a variavel na Direita
# < -  Aloca a variavel na Esquerda
# ^ -  Aloca a variavel no Centro

#n1 = int(input('Digite um numero: '))
#n2 = int(input('Digite outro numero: '))
#s = n1 + n2
#m = n1*n2
#d = n1/n2
#di = n1//n2
#e = n1 ** n2

#print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f}'.format(s,m,d), end='')# ':.3f' Definiu a variavel que esta apresentando, para uma com apenas 3 casas flutuantes(decimais)
#print('A divisão inteira é {} e a potencia é {:}'.format(di,e))# "end=''" atua como uam função que impede a quebra de linha de dois 'prints', '\n' atua como uma quabra de linha  

#Desafio 005
#Faça um programa que leia um numero inteiro e mostro na tela o seu sucessor e seu antecessor

#num1 = int(input('digite um numero: '))

#print('O antecessor deste numero é {}'.format(num1-1), end=' >>>> ')
#print('Já o sucessor deste numero é {}'.format(num1+1))

#Desafio 06
#Faça um programa que leia um numero e mostro o seu dobro, triplo e rais quadrada

#num1 = int(input('Digite um valor: '))
#print('O seu Dobro é : {}'.format(num1*2))
#print('O seu triplo é: {}'.format(num1*3))
#print('A sua Raiz quadrada é: {}'.format(num1**(1/2)))

#Desafio 07
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media 

#n1 = float(input('Digite a primeira nota do aluno: '))
#n2 = float(input('Digite a segudna nota do aluno: '))

#print('A media do aluno é: {:.2f}'.format((n1+n2)/2))

#Desafio 08
#Escreva um programa que liai um valor em metro e o exiba convertido em centimetros e milimetros 

#m = float(input('Digite quantos metros deseja saber: '))

#print('O valor em centimetros é: {}'.format(m*100))
#print('O valor em Milimetros é: {}'.format(m*1000))

#Desafio 09
#Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

#n = int(input('Digite um numero para a tabuada: '))
#print('A tabuada do {} é:'.format(n))
#print('{} x 1 = {}'.format(n, n*1))
#print('{} x 2 = {}'.format(n, n*2))
#print('{} x 3 = {}'.format(n, n*3))
#print('{} x 4 = {}'.format(n, n*4))
#print('{} x 5 = {}'.format(n, n*5))
#print('{} x 6 = {}'.format(n, n*6))
#print('{} x 7 = {}'.format(n, n*7))
#print('{} x 8 = {}'.format(n, n*8))
#print('{} x 9 = {}'.format(n, n*9))
#print('{} x 10 = {}'.format(n, n*10))

#Desafio 10
#Crie um programa que liai quanto dinheiro uma pessoa tem na carteira e mostra quantos Dólares ela pode comprar 
#Considere 
#US$1.00 = R$3.27


