#-----------------------Módulos---------------------------#
from random import choice

#-----------------------Funções---------------------------#
def printTabuleiro(tabuleiro):
	#Printa o tabuleiro do jogo (#).
	print('')
	print(' '*10 + otabuleiro['top-L'] + '|' + otabuleiro['top-M'] + '|' + otabuleiro['top-R'])
	print(' '*10 + '-+-+-')
	print(' '*10 + otabuleiro['mid-L'] + '|' + otabuleiro['mid-M'] + '|' + otabuleiro['mid-R'])
	print(' '*10 + '-+-+-')
	print(' '*10 + otabuleiro['low-L'] + '|' + otabuleiro['low-M'] + '|' + otabuleiro['low-R'])
	print('')

def validaMarcacao(selecionou):
	#Verifica se a posição escolhida é válida.
	if selecionou not in otabuleiro.keys():
		msg = f'O espaço {selecionou} é inválido!'
		return msg, False
	elif otabuleiro[selecionou] != ' ':
		msg = f'O espaço {selecionou} já está marcado!'
		return msg, False
	else:
		return '', True

def ganhador(ganhador):
	if vez != 'Computador':
		print(f"Parabéns {ganhador}! Você venceu!")
	else:
		print('Infelizmente o computador venceu!')

#-------------------------Main-----------------------------#
otabuleiro = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
			  'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
			  'low-L': ' ', 'low-M': ' ', 'low-R': ' '} #Tupla, abstração do tabuleiro (chave-valor = posição-marcação).
players = {} #Tupla dos jogadores (chave-valor = nome-marcador).

jogador1 = input('Digite o seu nome: ')
marca1 = input('Escolha (X) ou (O): ').upper()
players.setdefault(jogador1, marca1) #Adiciona o jogador 1 e seu respectivo marcador à tupla.
if marca1 == 'X':
	players.setdefault('Computador', 'O')
else:
	players.setdefault('Computador', 'X')
escolhidos = list(otabuleiro.keys())
vez = choice(list(players.keys())) #Escolhe randomicamente quem começará o jogo.
print(f"\nO primeiro jogador será {vez}({players[vez]}).")
printTabuleiro(otabuleiro)
for i in range(9):
	if vez == 'Computador':
		seleção = choice(escolhidos)
		print(f'Computador escolheu {seleção}!')
	else:
		seleção = input(f'{vez}({players[vez]}) escolha o espaço que deseja marcar: ')
		while True: #Enquanto a entrada não for válida, uma nova entrada será requerida.
			msg, valid = validaMarcacao(seleção)
			if valid:
				break
			else:
				seleção = input(f'{msg}, Escolha um espaço válido: ')
	del escolhidos[escolhidos.index(seleção)]
	otabuleiro[seleção] = players[vez] #Marca no tabuleiro a posição escolhida pelo jogador.
	printTabuleiro(otabuleiro)
	if i >= 4: #Verifica se algum jogador venceu.
		if otabuleiro['top-L'] == otabuleiro['top-M'] == otabuleiro['top-R'] != ' ':
			printTabuleiro(otabuleiro)
			ganhador(vez)
			break
		elif otabuleiro['mid-L'] == otabuleiro['mid-M'] == otabuleiro['mid-R'] != ' ':
			printTabuleiro(otabuleiro)
			ganhador(vez)
			break
		elif otabuleiro['low-L'] == otabuleiro['low-M'] == otabuleiro['low-R'] != ' ':
			printTabuleiro(otabuleiro)
			ganhador(vez)
			break
		elif otabuleiro['top-L'] == otabuleiro['mid-L'] == otabuleiro['low-L'] != ' ':
			printTabuleiro(otabuleiro)
			ganhador(vez)
			break
		elif otabuleiro['top-M'] == otabuleiro['mid-M'] == otabuleiro['low-M'] != ' ':
			printTabuleiro(otabuleiro)
			ganhador(vez)
			break
		elif otabuleiro['top-R'] == otabuleiro['mid-R'] == otabuleiro['low-R'] != ' ':
			printTabuleiro(otabuleiro)
			ganhador(vez)
			break
		elif otabuleiro['top-L'] == otabuleiro['mid-M'] == otabuleiro['low-R'] != ' ':
			printTabuleiro(otabuleiro)
			ganhador(vez)
			break
		elif otabuleiro['top-R'] == otabuleiro['mid-M'] == otabuleiro['low-L'] != ' ':
			printTabuleiro(otabuleiro)
			ganhador(vez)
			break
	if i == 8: #Se no ultimo loop ninguem ganhar, então deu velha.
		printTabuleiro(otabuleiro)
		print('VELHA! Infelizmente ninguém venceu! :-(')
	if vez == list(players.keys())[0]: #Muda a vez da jogada.
		vez = list(players.keys())[1]
	else:
		vez = list(players.keys())[0]

#--------------------------Fim-----------------------------#
