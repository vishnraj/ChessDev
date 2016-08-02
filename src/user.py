import pygame, chessboard

pygame.init()

def movement_whitePlayer(white, event, grid, selection, screen, board, clearBoard, black, players):
	whitePieces = white.sprites()

	if len(selection) != 0 and event.type == pygame.MOUSEBUTTONUP:
		futs = None
		for s in grid:
			if s.rect.collidepoint(pygame.mouse.get_pos()):
				futs = s
		movingPiece = selection.pop()
		oldx = movingPiece.xpos
		oldy = movingPiece.ypos
		olds = None
		king = None
		for square in grid:
			if square.xpos == oldx and square.ypos == oldy:
				olds = square
		if olds != None:
			movingPiece.move(futs.xpos, futs.ypos, white, black, olds, futs, grid, False)
		for piece in whitePieces:
			if type(piece) == chessboard.King:
				king = piece
		if king.check(white, black, grid):
			movingPiece.set(oldx, oldy)
			olds.occupant = movingPiece
		if movingPiece.xpos != oldx or movingPiece.ypos != oldy:
			for otherPiece in black.sprites():
				if type(otherPiece) == chessboard.Pawn:
					if otherPiece.switch:
						otherPiece.switch = False
			futs.occupant = movingPiece
			if type(movingPiece) == chessboard.Pawn:
				if movingPiece.ypos == 40:
					text = pygame.font.Font(None, 25)
					prompt = text.render("To Promote Pawn: Press 1 for Queen, 2 for Bishop, 3 for Rook, or 4 for Knight", 1, (0, 0, 255))
					players.clear(board, clearBoard)
					players.draw(board)
					screen.blit(board, (0, 0))
					select = False
					while not select:
						screen.blit(prompt, (0, 320))
						pygame.display.update()
						pygame.event.pump()
						keys = pygame.key.get_pressed()
						if keys[pygame.K_1]:
							movingPiecexpos = movingPiece.xpos
							movingPieceypos = movingPiece.ypos
							movingPiece.kill()
							white_queen = chessboard.Queen('whitequeen.jpg', movingPiecexpos, movingPieceypos, 'white')
							white.add(white_queen)
							players.add(white_queen)
							futs.occupant = white_queen
							select = True
						elif keys[pygame.K_2]:
							movingPiecexpos = movingPiece.xpos
							movingPieceypos = movingPiece.ypos
							movingPiece.kill()
							white_bishop = chessboard.Bishop('whitebishop.png', movingPiecexpos, movingPieceypos, 'white')
							white.add(white_bishop)
							players.add(white_bishop)
							futs.occupant = white_bishop
							select = True
						elif keys[pygame.K_3]:
							movingPiecexpos = movingPiece.xpos
							movingPieceypos = movingPiece.ypos
							movingPiece.kill()
							white_rook = chessboard.Rook('whiterook.png', movingPiecexpos, movingPieceypos, 'white')
							white.add(white_rook)
							players.add(white_rook)
							futs.occupant = white_rook
							select = True
						elif keys[pygame.K_4]:
							movingPiecexpos = movingPiece.xpos
							movingPieceypos = movingPiece.ypos
							movingPiece.kill()
							white_knight = chessboard.Knight('whiteknight.png', movingPiecexpos, movingPieceypos, 'white')
							white.add(white_knight)
							players.add(white_knight)
							futs.occupant = white_knight
							select = True
			players.clear(board, clearBoard)
			players.draw(board)
			screen.blit(board, (0, 0))
			pygame.display.update()
			return False

	for chessPiece in whitePieces:
		currentPiece = chessPiece
		currentMouse_pos = pygame.mouse.get_pos()
		if currentPiece.rect.collidepoint(currentMouse_pos):
			if type(currentPiece) == chessboard.Pawn:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if len(selection) != 0:	
						selection.pop()
					selection.append(currentPiece)	
			if type(currentPiece) == chessboard.Knight:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if len(selection) != 0:	
						selection.pop()
					selection.append(currentPiece)
			if type(currentPiece) == chessboard.Bishop:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if len(selection) != 0:	
						selection.pop()
					selection.append(currentPiece)
			if type(currentPiece) == chessboard.Rook:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if len(selection) != 0:	
						selection.pop()
					selection.append(currentPiece)
			if type(currentPiece) == chessboard.Queen:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if len(selection) != 0:	
						selection.pop()
					selection.append(currentPiece)
			if type(currentPiece) == chessboard.King:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if len(selection) != 0:	
						selection.pop()
					selection.append(currentPiece)
	return True

def movement_blackPlayer(black, event, grid, selection, screen, board, clearBoard, white, players):
	blackPieces = black.sprites()

	if len(selection) != 0 and event.type == pygame.MOUSEBUTTONUP:
		futs = None
		for s in grid:
			if s.rect.collidepoint(pygame.mouse.get_pos()):
				futs = s
		movingPiece = selection.pop()
		oldx = movingPiece.xpos
		oldy = movingPiece.ypos
		olds = None
		king = None
		for square in grid:
			if square.xpos == oldx and square.ypos == oldy:
				olds = square
		if olds != None:
			movingPiece.move(futs.xpos, futs.ypos, black, white, olds, futs, grid, False)
		for piece in blackPieces:
			if type(piece) == chessboard.King:
				king = piece
		if king.check(black, white, grid):
			movingPiece.set(oldx, oldy)
			olds.occupant = movingPiece
		if movingPiece.xpos != oldx or movingPiece.ypos != oldy:
			for otherPiece in white.sprites():
				if type(otherPiece) == chessboard.Pawn:
					if otherPiece.switch:
						otherPiece.switch = False
			futs.occupant = movingPiece
			if type(movingPiece) == chessboard.Pawn:
				if movingPiece.ypos == 600:
					text = pygame.font.Font(None, 25)
					prompt = text.render("To Promote Pawn: Press 1 for Queen, 2 for Bishop, 3 for Rook, or 4 for Knight", 1, (0, 0, 255))
					players.clear(board, clearBoard)
					players.draw(board)
					screen.blit(board, (0, 0))
					select = False
					while not select:
						screen.blit(prompt, (0, 320))
						pygame.display.update()
						pygame.event.pump()
						keys = pygame.key.get_pressed()
						if keys[pygame.K_1]:
							movingPiecexpos = movingPiece.xpos
							movingPieceypos = movingPiece.ypos
							movingPiece.kill()
							black_queen = chessboard.Queen('blackqueen.png', movingPiecexpos, movingPieceypos, 'black')
							black.add(black_queen)
							players.add(black_queen)
							futs.occupant = black_queen
							select = True
						elif keys[pygame.K_2]:
							movingPiecexpos = movingPiece.xpos
							movingPieceypos = movingPiece.ypos
							movingPiece.kill()
							black_bishop = chessboard.Bishop('blackbishop.png', movingPiecexpos, movingPieceypos, 'black')
							black.add(black_bishop)
							players.add(black_bishop)
							futs.occupant = black_bishop
							select = True
						elif keys[pygame.K_3]:
							movingPiecexpos = movingPiece.xpos
							movingPieceypos = movingPiece.ypos
							movingPiece.kill()
							black_rook = chessboard.Rook('blackrook.png', movingPiecexpos, movingPieceypos, 'black')
							black.add(black_rook)
							players.add(black_rook)
							futs.occupant = black_rook
							select = True
						elif keys[pygame.K_4]:
							movingPiecexpos = movingPiece.xpos
							movingPieceypos = movingPiece.ypos
							movingPiece.kill()
							black_knight = chessboard.Knight('blackknight.gif', movingPiecexpos, movingPieceypos, 'black')
							black.add(black_knight)
							players.add(black_knight)
							futs.occupant = black_knight
							select = True
			players.clear(board, clearBoard)
			players.draw(board)
			screen.blit(board, (0, 0))
			pygame.display.update()
			return True

	for chessPiece in blackPieces:
		currentPiece = chessPiece
		currentMouse_pos = pygame.mouse.get_pos()
		if currentPiece.rect.collidepoint(currentMouse_pos):
			if type(currentPiece) == chessboard.Pawn:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if len(selection) != 0:	
						selection.pop()
					selection.append(currentPiece)	
			if type(currentPiece) == chessboard.Knight:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if len(selection) != 0:	
						selection.pop()
					selection.append(currentPiece)
			if type(currentPiece) == chessboard.Bishop:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if len(selection) != 0:	
						selection.pop()
					selection.append(currentPiece)
			if type(currentPiece) == chessboard.Rook:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if len(selection) != 0:	
						selection.pop()
					selection.append(currentPiece)
			if type(currentPiece) == chessboard.Queen:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if len(selection) != 0:	
						selection.pop()
					selection.append(currentPiece)
			if type(currentPiece) == chessboard.King:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if len(selection) != 0:	
						selection.pop()
					selection.append(currentPiece)
	return False