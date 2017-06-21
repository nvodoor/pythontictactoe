board = [[0,0,0],[0,0,0],[0,0,0]]

def playerone(move):

	if move == 1:
		board[0][0] = 'X'
		print board
	if move == 2:
		board[0][1] = 'X'
		print board
	if move == 3:
		board[0][2] = 'X'
	if move == 4:
		board[1][0] = 'X'
	if move == 5:
		board[1][1] = 'X'
	if move == 6:
		board[1][2] = 'X'
	if move == 7:
		board[2][0] = 'X'
	if move == 8:
		board[2][1] = 'X'
	if move == 9:
		board[2][2] = 'X'

def playertwo(move):

	if move == 1:
		board[0][0] = 'O'
	if move == 2:
		board[0][1] = 'O'
	if move == 3:
		board[0][2] = 'O'
	if move == 4:
		board[1][0] = 'O'
	if move == 5:
		board[1][1] = 'O'
	if move == 6:
		board[1][2] = 'O'
	if move == 7:
		board[2][0] = 'O'
	if move == 8:
		board[2][1] = 'O'
	if move == 9:
		board[2][2] = 'O'


victory = False
count = 1

def victorycondition():

	if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
		print "Player One has won. Good game."
		return True

	if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
		print "Player Two has won. Good game."
		return True

	if board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
		print "Player One has won. Good game."
		return True

	if board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
		print "Player Two has won. Good game."
		return True
	
	if board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
		print "Player One has won. Good game."
		return True

	if board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
		print "Player Two has won. Good game."
		return True

	if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
		print "Player One has won. Good game."
		return True

	if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
		print "Player Two has won. Good game."
		return True

	if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
		print "Player One has won. Good game."
		return True

	if board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
		print "Player Two has won. Good game."
		return True

	if board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
		print "Player One has won. Good game."
		return True

	if board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
		print "Player Two has won. Good game."
		return True

	if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
		print "Player One has won. Good game."
		return True

	if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
		print "Player Two has won. Good game."
		return True

	if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
		print "Player One has won. Good game."
		return True

	if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
		print "Player Two has won. Good game."
		return True

numbercheck = [1,2,3,4,5,6,7,8,9]

while victory == False:
	choice = input("Where would you like to place your tic?")
	newgame = "no"

	if count == 1:
		board = [[0,0,0],[0,0,0],[0,0,0]]

	if count == 10:
		gameover = raw_input("Game is over. Max turns reached. Would you like to play again?")
		if gameover == 'yes':
			count = 0
		else:
			victory = True

	if count % 2 > 0:
		for num in numbercheck:
			if num == choice:
				playerone(choice)
				if victorycondition() == True:
					tryagain = raw_input("Would you like to play again?")
					if tryagain == 'yes':
						count = 1
						newgame = "yes"
					else:
						victory = True
				if count > 0:
					print board			


	if count % 2 == 0:
		for num in numbercheck:
			if num == choice:
				playertwo(choice)
				if victorycondition() == True:
					tryagain = raw_input("Would you like to play again?")
					if tryagain == 'yes':
						count = 1
						newgame = "yes"
					else:
						victory = True
				if count > 0:
					print board

	if newgame == "no":
		count += 1
	else:
		newgame = "no"



print "Thanks for playing."