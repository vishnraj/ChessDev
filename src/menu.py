import sys, pygame, game

pygame.init()

def main():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen = pygame.display.set_mode((640, 640))
		board = pygame.image.load('chessboard.gif').convert()
		board = pygame.transform.scale(board, (640, 640))
		clearBoard = pygame.image.load('chessboard.gif').convert()
		clearBoard = pygame.transform.scale(board, (640, 640))
		fontObject = pygame.font.Font(None, 30)
		title = fontObject.render("Welcome to A Chess Tutorial by Vishnu Rajendran", True, (0, 255, 0))
		quitButton = fontObject.render("QUIT", True, (255, 0, 0))
		playComputer = fontObject.render("Play Computer", True, (255, 0, 0))
		twoPlayer = fontObject.render("Two Player", True, (255, 0, 0))
		twoPlayerRect = pygame.Rect([240, 240, 160, 80])
		playComputerRect = pygame.Rect([240, 320, 160, 80])
		quitRect = pygame.Rect([240, 400, 160, 80])
		pygame.draw.ellipse(board, (0, 0, 255), twoPlayerRect)
		pygame.draw.ellipse(board, (0, 0, 255), quitRect)
		pygame.draw.ellipse(board, (0, 0, 255), playComputerRect)
		screen.blit(board, (0, 0))
		screen.blit(twoPlayer, (265, 265))
		screen.blit(playComputer, (250, 345))
		screen.blit(quitButton, (295, 425))
		screen.blit(title, (80, 0))
		pygame.display.update()
		if twoPlayerRect.collidepoint(pygame.mouse.get_pos()):
			twoPlayer = fontObject.render("Two Player", True, (0, 255, 0))
			screen.blit(twoPlayer, (265, 265))
			pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN:
				game.main(True, False, False, False)
		elif playComputerRect.collidepoint(pygame.mouse.get_pos()):
			playComputer = fontObject.render("Play Computer", True, (0, 255, 0))
			screen.blit(playComputer, (250, 345))
			pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN:
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							sys.exit()
					board = clearBoard
					whiteButton = fontObject.render("Play as White", True, (255, 0, 0))
					blackButton = fontObject.render("Play as Black", True, (255, 0, 0))
					whiteButtonRect = pygame.Rect([240, 240, 160, 80])
					blackButtonRect = pygame.Rect([240, 400, 160, 80])
					pygame.draw.ellipse(board, (0, 0, 255), whiteButtonRect)
					pygame.draw.ellipse(board, (0, 0, 255), blackButtonRect)
					screen.blit(board, (0, 0))
					screen.blit(whiteButton, (255, 265))
					screen.blit(blackButton, (255, 425))
					pygame.display.update()
					if whiteButtonRect.collidepoint(pygame.mouse.get_pos()):
						whiteButton = fontObject.render("Play as White", True, (0, 255, 0))
						screen.blit(whiteButton, (255, 265))
						pygame.display.update()
						if event.type == pygame.MOUSEBUTTONDOWN:
							game.main(False, True, True, False) 
					elif blackButtonRect.collidepoint(pygame.mouse.get_pos()):
						blackButton = fontObject.render("Play as Black", True, (0, 255, 0))
						screen.blit(blackButton, (255, 425))
						pygame.display.update()
						if event.type == pygame.MOUSEBUTTONDOWN:
							game.main(False, True, False, True)
		elif quitRect.collidepoint(pygame.mouse.get_pos()):
			quitButton = fontObject.render("QUIT", True, (0, 255, 0))
			screen.blit(quitButton, (295, 425))
			pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN:
				sys.exit()
if __name__== '__main__':
	main()