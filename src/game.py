import sys, pygame, chessboard, user, menu, AI

pygame.init()

def main(twoPlayer, playComputer, White, Black):
	black_player = chessboard.setBlack()
	white_player = chessboard.setWhite()
	players = chessboard.Players()
	for sprites in black_player.sprites():
		players.add(sprites)
	for sprites in white_player.sprites():
		players.add(sprites)
	black_pieces = black_player.sprites()
	white_pieces = white_player.sprites()
	Pieces = black_pieces + white_pieces 
	blackPiece = []
	whitePiece = []

	screen = pygame.display.set_mode((640, 640))
	gridsquare = chessboard.convert(pygame.Surface((80, 80)).convert_alpha())
	board = pygame.image.load('chessboard.gif').convert()
	board = pygame.transform.scale(board, (640, 640))
	
	clearBoard = pygame.image.load('chessboard.gif').convert()
	clearBoard = pygame.transform.scale(clearBoard, (640, 640))
	
	players.draw(board)
	screen.blit(board, (0, 0))
	grid = []
	newPiece = None
	for y in range(0, 640, 80):
		for x in range(0, 640, 80):
			occupied = False
			for piece in Pieces:
				if piece.xpos == x + 40 and piece.ypos == y + 40:
					occupied = True
					newPiece = piece
			if occupied:
				s = chessboard.Square(gridsquare, x, y, newPiece)
				#screen.blit(s.image, (x, y))
				grid.append(s)
			else:
				s = chessboard.Square(gridsquare, x, y, None)
				#screen.blit(s.image, (x, y))
				grid.append(s)
	pygame.display.update()
	checkmate = False
	stalemate = False
	turn = True
	whiteKing = None
	blackKing = None
	whiteCount = 0
	blackCount = 0
	
	while True:
		while not checkmate and not stalemate:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit() 
			
			if twoPlayer:
				while turn and not checkmate and not stalemate:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							sys.exit() 
					turn = user.movement_whitePlayer(white_player, event, grid, whitePiece, screen, board, clearBoard, black_player, players)

				black_pieces = black_player.sprites()
				if len(black_pieces) == 1:
					whiteCount += 1
			
				for black_piece in black_player:
					if type(black_piece) == chessboard.King:
						blackKing = black_piece		

				checkmate = blackKing.checkmate(black_player, white_player, grid)	
				stalemate = blackKing.stalemate(black_player, white_player, grid)	
				if whiteCount == 50:
					stalemate = True

				elif len(white_pieces) == 1 and len(black_pieces) == 1:
					stalemate = True

				while not turn and not checkmate and not stalemate:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							sys.exit()
					turn = user.movement_blackPlayer(black_player, event, grid, blackPiece, screen, board, clearBoard, white_player, players)
					
				white_pieces = white_player.sprites()
				if len(white_pieces) == 1:
					blackCount += 1

				for white_piece in white_player:
					if type(white_piece) == chessboard.King:
						whiteKing = white_piece

				if not checkmate and not stalemate: 
					checkmate = whiteKing.checkmate(white_player, black_player, grid)
					stalemate = whiteKing.stalemate(white_player, black_player, grid)
				if blackCount == 50:
					stalemate = True

				elif len(white_pieces) == 1 and len(black_pieces) == 1:
					stalemate = True
			
			elif playComputer:
				if White:
					while turn and not checkmate and not stalemate:
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								sys.exit()
						turn = user.movement_whitePlayer(white_player, event, grid, whitePiece, screen, board, clearBoard, black_player, players)

					black_pieces = black_player.sprites()
					if len(black_pieces) == 1:
						whiteCount += 1
			
					for black_piece in black_player:
						if type(black_piece) == chessboard.King:
							blackKing = black_piece		

					checkmate = blackKing.checkmate(black_player, white_player, grid)	
					stalemate = blackKing.stalemate(black_player, white_player, grid)	
					if whiteCount == 50:
						stalemate = True

					elif len(white_pieces) == 1 and len(black_pieces) == 1:
						stalemate = True

					if not turn and not checkmate and not stalemate:
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								sys.exit()
						turn = AI.movement_blackPlayer(black_player, event, grid, screen, board, clearBoard, white_player, players)

					white_pieces = white_player.sprites()
					if len(white_pieces) == 1:
						blackCount += 1

					for white_piece in white_player:
						if type(white_piece) == chessboard.King:
							whiteKing = white_piece

					if not checkmate and not stalemate: 
						checkmate = whiteKing.checkmate(white_player, black_player, grid)
						stalemate = whiteKing.stalemate(white_player, black_player, grid)
					if blackCount == 50:
						stalemate = True

					elif len(white_pieces) == 1 and len(black_pieces) == 1:
						stalemate = True

					#turn = True
				
				elif Black:
					if turn and not checkmate and not stalemate:
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								sys.exit()
						turn = AI.movement_whitePlayer(white_player, event, grid, screen, board, clearBoard, black_player, players)

					black_pieces = black_player.sprites()
					if len(black_pieces) == 1:
						whiteCount += 1
			
					for black_piece in black_player:
						if type(black_piece) == chessboard.King:
							blackKing = black_piece		

					checkmate = blackKing.checkmate(black_player, white_player, grid)	
					stalemate = blackKing.stalemate(black_player, white_player, grid)	
					if whiteCount == 50:
						stalemate = True

					elif len(white_pieces) == 1 and len(black_pieces) == 1:
						stalemate = True

					while not turn and not checkmate and not stalemate:
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								sys.exit()
						turn = user.movement_blackPlayer(black_player, event, grid, blackPiece, screen, board, clearBoard, white_player, players)

					white_pieces = white_player.sprites()
					if len(white_pieces) == 1:
						blackCount += 1

					for white_piece in white_player:
						if type(white_piece) == chessboard.King:
							whiteKing = white_piece

					if not checkmate and not stalemate: 
						checkmate = whiteKing.checkmate(white_player, black_player, grid)
						stalemate = whiteKing.stalemate(white_player, black_player, grid)
					if blackCount == 50:
						stalemate = True

					elif len(white_pieces) == 1 and len(black_pieces) == 1:
						stalemate = True

		text = pygame.font.Font(None, 25)
		prompt = None
		if blackKing.checkmate(black_player, white_player, grid):
			prompt = text.render("White Won: Press Y to play again, Press N for menu", True, (0, 0, 255))
		elif whiteKing.checkmate(white_player, black_player, grid):
			prompt = text.render("Black Won: Press Y to play again, Press N for menu", True, (0, 0, 255))
		elif stalemate:
			prompt = text.render("Draw: Press Y to play again, Press N for menu", True, (0, 0, 255))
		players.clear(board, clearBoard)
		players.draw(board)
		screen.blit(board, (0, 0))
		select = False
		while not select:
			screen.blit(prompt, (0, 320))
			pygame.display.update()
			pygame.event.pump()
			keys = pygame.key.get_pressed()
			if keys[pygame.K_y]:
				players.clear(board, clearBoard)
				players.empty()
				black_player = chessboard.setBlack()
				white_player = chessboard.setWhite()
				for sprites in black_player.sprites():
					players.add(sprites)
				for sprites in white_player.sprites():
					players.add(sprites)
				black_pieces = black_player.sprites()
				white_pieces = white_player.sprites()
				Pieces = black_pieces + white_pieces 
				blackPiece = []
				whitePiece = []
				players.draw(board)
				screen.blit(board, (0, 0))
				grid = []
				newPiece = None
				for y in range(0, 640, 80):
					for x in range(0, 640, 80):
						occupied = False
						for piece in Pieces:
							if piece.xpos == x + 40 and piece.ypos == y + 40:
								occupied = True
								newPiece = piece
						if occupied:
							s = chessboard.Square(gridsquare, x, y, newPiece)
							#screen.blit(s.image, (x, y))
							grid.append(s)
						else:
							s = chessboard.Square(gridsquare, x, y, None)
							#screen.blit(s.image, (x, y))
							grid.append(s)
				pygame.display.update()
				checkmate = False
				stalemate = False
				turn = True
				whiteKing = None
				blackKing = None
				whiteCount = 0
				blackCount = 0
				select = True
			elif keys[pygame.K_n]:
				menu.main()
if __name__ == '__main__': 
	main()