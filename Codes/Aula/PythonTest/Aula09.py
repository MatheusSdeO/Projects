# Manipulando textos 

# frase = 'Curson em Video Python'

# Fatiamento 
# Pegar uma letra da variavel 
# Ex: frase[9] -  pegar o valor que esta na nona casa 
# Ex: frase[9:13] - Pega os valores entre o parametro dado, porem ira excluir o ultimo, ou seja ele pega os valores de 9-12 
# Ex: frase[9:21:2] - pega os valores mostrando apenas de 2 em dois 
# Ex: frase[:5] - é a mesma coisa que escrever frase[0:5], pois sem nada de parametro ele sempre começara no 0 
# Ex: frase[15:] - é como se indicasse que não si ate onde ir, por isso o sistema interpreta para ir ate o final 
# Ex: frase[9::3] - Nesta sintaxe ele ira fazer: ira do 9 ate o ultimo caractere pulando de 3 em 3 casas 

# Função len(frase)
# Mostra o comprimento da frase que sera alocado dentro da memoria (espaços contam caracteres tambem)

# Função frase.count('o')
# Função para contar quantas letras tem dentro da frase - Necessita especificar a letra dentro do parametro 
# Se utilizar a função frase.count('o', o, 13) -  Ja utiliza o Fatiamento, onde ira contar do 0-12

# Função frase.find('deo')
# Ira mostrar o momento que o parametro começou 
# Se colocar dentro do find uma str que não existe, retorna o valor -1, pois ele não encontrou 

# 'Curso' in frase
# Esta função ira dizer se existe o parametro especificado dentro da variavel

# Tranformação 

# Função frase.replace('Python', 'Android')
# Ira substituir o primeiero parametro pelo segundo especificado, com a variavel declarada ficando 'Curso em Video Android'

# Função frase.upper()
# Ira trasnformar todas as letras em minusculas para maiusculas 

# Função frase.lower()
# Ira transformar tudo que é maiusculo em minisculo 

# Função frase.capitalize()
# ira jogar todos os caracteres para minusculo e apenas a primeira letra ficara como maiusculo
# Vai ficar no terminal assim: Curso em video python

# Função frase.title()
# ira mostrar quantas palavras tem nessa variavel, Vai seguir a mesma função que a capitalize porem agora de palavra por palavra 
# Ele ira ler os espaços e fazer q quebra de palavras
# Vai ficar no terminal assim: Curso Em Video Python

# Nova variavel frase = '   Aprenda Python  '

# Função frase.strip()
# Ira remover todos os espaços inuteis da variavel fazendo com que o A fique como caracter 0 e a variavel tenha apenas tamanho de 13

# Função frase.rstrip()
# Remove apenas os ultimos espaços inuteis, pois junto ao r começa da direita 

# Função frase.lstrip()
# Remove apenas os primeiros espaços inuteis, pois junto ao l começa da esquerda

# Divisão 

# Variavel frase = 'Curso em Video Python'

# Função frase.split()
# Esta função ira criar uma 'Divisão', ou seja ira criar uma index para cara palavra, na frase com 20 caracteres, ficando Curso - 4, em - 1, Video - 4, Python - 5
# Colocando cada palavra dentro de uma "nova" lista 

# Junção

# Função '-'.join(frase)
# Ira juntar todos os elementos de frase e ira separar elas pelo '-'
# No terminal fica Curson-em-Video-Python

# Utilizar as 3 """  """, pode ser usado para colocar textos grandes

#frase = 'Curso em Video Python'
#print(frase[1:15:2])

# Desafio 22
# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# 1º - O nome com todas as letras em maiusculas
# 2º - O nome com todas minusculas
# 3º - Quantas letras ao todo(Sem consideras espaços)
# 4º - Quantas letras tem o primeiro nome

n = input('Qual o seu nome? ')
print('O seu nome com todas as letras maiusculas é {}'.format(n.upper()))
print('O seu nome com todas as letras minusculas é {}'.format(n.lower()))
print('Seu nome tem esse numero de letras {}'.format(len(n)))
print('Seu primeiro nome tem esse numero de letras {}'.format(n.split()))