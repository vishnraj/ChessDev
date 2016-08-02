import  pygame, chessboard

pygame.init()

class Tree: 
	def __init__(self, node1=None, node2=None, node3=None, alpha=0, beta=100):
		self.node1 = node1
		self.node2 = node2
		self.node3 = node3
		self.alpha = alpha
		self.beta = beta
		self.parent = None
		self.value = None
		self.children = []
		self.fromLeft = None
	def append(self, tree, distance):
		if type(tree) == Tree:
			self.children.append(tree)
			tree.parent = self
			tree.fromLeft = distance
	
	def pop(self, distance=None):
		if distance == None:
			return self.children.pop()
		else:
			for child in self.children:
				if self.children.index(child) == distance:
					i = self.children.index(child)
					return self.children.pop(i) 

	def getChild(self, distance):
		return self.children[distance]

	def get_leftMost(self):
		return self.children[0]

	def allSet(self):
		for child in self.children:
			if child.value == None:
				return False
		return True 

	def getRoot(self, tree):
		if tree.parent == None:
			return self
		else:
			return self.getRoot(tree.parent)

def inColor(Color, pieceType):
	colorList = Color.sprites()
	for piece in colorList:
		if type(piece) == pieceType:
			return True
	return False

def num_inColor(Color, pieceType):
	colorList = Color.sprites()
	count = 0
	for piece in colorList:
		if type(piece) == pieceType:
			count += 1
	return count

def deepCopy(Color):
	if type(Color) == chessboard.whitePlayer:
		plyPlayer = chessboard.whitePlayer()
		for Piece in Color.sprites():
			Piecexpos = Piece.xpos
			Pieceypos = Piece.ypos
			if type(Piece) == chessboard.Pawn:
				white_pawn = chessboard.Pawn('whitepawn.png', Piecexpos, Pieceypos, 'white')
				if Piece.firstMove:
					white_pawn.firstMove = True
				else:
					white_pawn.firstMove = False
				if Piece.switch:
					white_pawn.switch = True
				else:
					white_pawn.switch = False
				plyPlayer.add(white_pawn)
			elif type(Piece) == chessboard.Knight:
				white_knight = chessboard.Knight('whiteknight.png', Piecexpos, Pieceypos, 'white')
				plyPlayer.add(white_knight)
			elif type(Piece) == chessboard.Bishop:
				white_bishop = chessboard.Bishop('whitebishop.png', Piecexpos, Pieceypos, 'white')
				plyPlayer.add(white_bishop)
			elif type(Piece) == chessboard.Rook:
				white_rook = chessboard.Rook('whiterook.png', Piecexpos, Pieceypos, 'white')
				if Piece.firstMove:
					white_rook.firstMove = True
				else:
					white_rook.firstMove = False
				plyPlayer.add(white_rook)
			elif type(Piece) == chessboard.Queen:
				white_queen = chessboard.Queen('whitequeen.jpg', Piecexpos, Pieceypos, 'white')
				plyPlayer.add(white_queen)
			elif type(Piece) == chessboard.King:
				white_king = chessboard.King('whiteking.png', Piecexpos, Pieceypos, 'white')
				if Piece.firstMove:
					white_king.firstMove = True
				else:
					white_rook.firstMove = False
				plyPlayer.add(white_king)
		
	elif type(Color) == chessboard.blackPlayer:
		plyPlayer = chessboard.blackPlayer()
		for Piece in Color.sprites():
			Piecexpos = Piece.xpos
			Pieceypos = Piece.ypos
			if type(Piece) == chessboard.Pawn:
				black_pawn = chessboard.Pawn('blackpawn.jpg', Piecexpos, Pieceypos, 'black')
				if Piece.firstMove:
					black_pawn.firstMove = True
				else:
					black_pawn.firstMove = False
				if Piece.switch:
					black_pawn.switch = True
				else:
					black_pawn.switch = False
				plyPlayer.add(black_pawn)
			elif type(Piece) == chessboard.Knight:
				black_knight = chessboard.Knight('blackknight.gif', Piecexpos, Pieceypos, 'black')
				plyPlayer.add(black_knight)
			elif type(Piece) == chessboard.Bishop:
				black_bishop = chessboard.Bishop('blackbishop.png', Piecexpos, Pieceypos, 'black')
				plyPlayer.add(black_bishop)
			elif type(Piece) == chessboard.Rook:
				black_rook = chessboard.Rook('blackrook.png', Piecexpos, Pieceypos, 'black')
				if Piece.firstMove:
					black_rook.firstMove = True
				else:
					black_rook.firstMove = False
				plyPlayer.add(black_rook)
			elif type(Piece) == chessboard.Queen:
				black_queen = chessboard.Queen('blackqueen.png', Piecexpos, Pieceypos, 'black')
				plyPlayer.add(black_queen)
			elif type(Piece) == chessboard.King:
				black_king = chessboard.King('blackking.png', Piecexpos, Pieceypos, 'black')
				if Piece.firstMove:
					black_king.firstMove = True
				else:
					black_king.firstMove = False
				plyPlayer.add(black_king)

	return plyPlayer
		

def possibleMoves(player, oppositePlayer, grid):
	Color = player
	oppositeColor = oppositePlayer
	Pieces = Color.sprites()
	Moves = Tree()
	distance = 0

	while len(Pieces) != 0:	
		piece = Pieces.pop()
		oldxpos = piece.xpos
		oldypos = piece.ypos
		oldSquare = chessboard.square_finder(piece.xpos, piece.ypos, grid)
		
		if type(piece) == chessboard.Pawn:
			Node = Tree(piece)
			Moves.append(Node, distance)
			index = 0
			if piece.color == "white":
				possible = False
				futureSquare = chessboard.square_finder(piece.xpos, piece.ypos - 160, grid)
				if futureSquare != None:
					possible = piece.move(piece.xpos, piece.ypos - 160, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					pawnMove = Tree(piece.xpos, piece.ypos - 160)
					Node.append(pawnMove, index)
					index += 1
				possible = False
				futureSquare = chessboard.square_finder(piece.xpos, piece.ypos - 80, grid)
				if futureSquare != None:
					possible = piece.move(piece.xpos, piece.ypos - 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					pawnMove = Tree(piece.xpos, piece.ypos - 80)
					Node.append(pawnMove, index)
					index += 1
				possible = False
				futureSquare = chessboard.square_finder(piece.xpos + 80, piece.ypos - 80, grid)
				if futureSquare != None:
					possible = piece.move(piece.xpos + 80, piece.ypos - 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					pawnMove = Tree(piece.xpos + 80, piece.ypos - 80)
					Node.append(pawnMove, index)
					index += 1
				possible = False
				futureSquare = chessboard.square_finder(piece.xpos - 80, piece.ypos - 80, grid)
				if futureSquare != None:
					possible = piece.move(piece.xpos - 80, piece.ypos - 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					pawnMove = Tree(piece.xpos - 80, piece.ypos - 80)
					Node.append(pawnMove, index)

			if piece.color == "black":
				possible = False
				futureSquare = chessboard.square_finder(piece.xpos, piece.ypos + 160, grid)
				if futureSquare != None:
					possible = piece.move(piece.xpos, piece.ypos + 160, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					pawnMove = Tree(piece.xpos, piece.ypos + 160)
					Node.append(pawnMove, index)
					index += 1
				possible = False
				futureSquare = chessboard.square_finder(piece.xpos, piece.ypos + 80, grid)
				if futureSquare != None:
					possible = piece.move(piece.xpos, piece.ypos + 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					pawnMove = Tree(piece.xpos, piece.ypos + 80)
					Node.append(pawnMove, index)
					index += 1
				possible = False
				futureSquare = chessboard.square_finder(piece.xpos + 80, piece.ypos + 80, grid)
				if futureSquare != None:
					possible = piece.move(piece.xpos + 80, piece.ypos + 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					pawnMove = Tree(piece.xpos + 80, piece.ypos + 80)
					Node.append(pawnMove, index)
					index += 1
				possible = False
				futureSquare = chessboard.square_finder(piece.xpos - 80, piece.ypos + 80, grid)
				if futureSquare != None:
					possible = piece.move(piece.xpos - 80, piece.ypos + 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					pawnMove = Tree(piece.xpos - 80, piece.ypos + 80)
					Node.append(pawnMove, index)

		elif type(piece) == chessboard.Knight:
			Node = Tree(piece)
			Moves.append(Node, distance)
			index = 0
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos + 80, piece.ypos + 160, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos + 80, piece.ypos + 160, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				knightMove = Tree(piece.xpos + 80, piece.ypos + 160)
				Node.append(knightMove, index)
				index += 1
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos + 80, piece.ypos - 160, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos + 80, piece.ypos - 160, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				knightMove = Tree(piece.xpos + 80, piece.ypos - 160)
				Node.append(knightMove, index)
				index += 1
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos - 80, piece.ypos + 160, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos - 80, piece.ypos + 160, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				pawnMove = Tree(piece.xpos - 80, piece.ypos + 160)
				Node.append(pawnMove, index)
				index += 1
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos - 80, piece.ypos - 160, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos - 80, piece.ypos - 160, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				knightMove = Tree(piece.xpos - 80, piece.ypos - 160)
				Node.append(knightMove, index)
				index += 1
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos + 160, piece.ypos + 80, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos + 160, piece.ypos + 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				knightMove = Tree(piece.xpos + 160, piece.ypos + 80)
				Node.append(knightMove, index)
				index += 1
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos + 160, piece.ypos - 80, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos + 160, piece.ypos - 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				knightMove = Tree(piece.xpos + 160, piece.ypos - 80)
				Node.append(knightMove, index)
				index += 1
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos - 160, piece.ypos - 80, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos - 160, piece.ypos - 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				knightMove = Tree(piece.xpos - 160, piece.ypos - 80)
				Node.append(knightMove, index)
				index += 1
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos - 160, piece.ypos + 80, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos - 160, piece.ypos + 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				knightMove = Tree(piece.xpos - 160, piece.ypos + 80)
				Node.append(knightMove, index)

		elif type(piece) == chessboard.Bishop:
			Node = Tree(piece)
			Moves.append(Node, distance)
			index = 0
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposx > 0 and squareposy > 0:
				squareposx -= 80
				squareposy -= 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					bishopMove = Tree(squareposx, squareposy)
					Node.append(bishopMove, index)
					index += 1
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposx > 0 and squareposy < 640:
				squareposx -= 80
				squareposy += 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					bishopMove = Tree(squareposx, squareposy)
					Node.append(bishopMove, index)
					index += 1
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposx < 640 and squareposy > 0:
				squareposx += 80
				squareposy -= 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					bishopMove = Tree(squareposx, squareposy)
					Node.append(bishopMove, index)
					index += 1
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposx < 640 and squareposy < 640:
				squareposx += 80
				squareposy += 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					bishopMove = Tree(squareposx, squareposy)
					Node.append(bishopMove, index)
					index += 1

		elif type(piece) == chessboard.Rook:
			Node = Tree(piece)
			Moves.append(Node, distance)
			index = 0
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposx > 0:
				squareposx -= 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					rookMove = Tree(squareposx, squareposy)
					Node.append(rookMove, index)
					index += 1
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposx < 640:
				squareposx += 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					rookMove = Tree(squareposx, squareposy)
					Node.append(rookMove, index)
					index += 1
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposy > 0:
				squareposy -= 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					rookMove = Tree(squareposx, squareposy)
					Node.append(rookMove, index)
					index += 1
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposy < 640:
				squareposy += 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					rookMove = Tree(squareposx, squareposy)
					Node.append(rookMove, index)
					index += 1

		elif type(piece) == chessboard.Queen:
			Node = Tree(piece)
			Moves.append(Node, distance)
			index = 0
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposx > 0:
				squareposx -= 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					rookMove = Tree(squareposx, squareposy)
					Node.append(rookMove, index)
					index += 1
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposx < 640:
				squareposx += 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					rookMove = Tree(squareposx, squareposy)
					Node.append(rookMove, index)
					index += 1
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposy > 0:
				squareposy -= 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					rookMove = Tree(squareposx, squareposy)
					Node.append(rookMove, index)
					index += 1
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposy < 640:
				squareposy += 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					rookMove = Tree(squareposx, squareposy)
					Node.append(rookMove, index)
					index += 1
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposx > 0 and squareposy > 0:
				squareposx -= 80
				squareposy -= 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					bishopMove = Tree(squareposx, squareposy)
					Node.append(bishopMove, index)
					index += 1
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposx > 0 and squareposy < 640:
				squareposx -= 80
				squareposy += 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					bishopMove = Tree(squareposx, squareposy)
					Node.append(bishopMove, index)
					index += 1
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposx < 640 and squareposy > 0:
				squareposx += 80
				squareposy -= 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					bishopMove = Tree(squareposx, squareposy)
					Node.append(bishopMove, index)
					index += 1
			squareposx = piece.xpos
			squareposy = piece.ypos
			while squareposx < 640 and squareposy < 640:
				squareposx += 80
				squareposy += 80
				possible = False
				futureSquare = chessboard.square_finder(squareposx, squareposy, grid)
				if futureSquare != None:
					possible = piece.move(squareposx, squareposy, Color, oppositeColor, oldSquare, futureSquare, grid, True)
					piece.set(oldxpos, oldypos)
					oldSquare.occupant = piece
				if possible:
					bishopMove = Tree(squareposx, squareposy)
					Node.append(bishopMove, index)
					index += 1

		elif type(piece) == chessboard.King:
			Node = Tree(piece)
			Moves.append(Node, distance)
			index = 0
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos + 80, piece.ypos, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos + 80, piece.ypos, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				kingMove = Tree(piece.xpos + 80, piece.ypos)
				Node.append(kingMove, index)
				index += 1
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos + 80, piece.ypos + 80, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos + 80, piece.ypos + 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				kingMove = Tree(piece.xpos + 80, piece.ypos + 80)
				Node.append(kingMove, index)
				index += 1
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos, piece.ypos + 80, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos, piece.ypos + 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				kingMove = Tree(piece.xpos, piece.ypos + 80)
				Node.append(kingMove, index)
				index += 1
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos, piece.ypos - 80, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos, piece.ypos - 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				kingMove = Tree(piece.xpos, piece.ypos - 80)
				Node.append(kingMove, index)
				index += 1
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos - 80, piece.ypos - 80, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos - 80, piece.ypos - 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				kingMove = Tree(piece.xpos - 80, piece.ypos - 80)
				Node.append(kingMove, index)
				index += 1
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos - 80, piece.ypos + 80, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos - 80, piece.ypos + 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				kingMove = Tree(piece.xpos - 80, piece.ypos + 80)
				Node.append(kingMove, index)
				index += 1
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos + 80, piece.ypos - 80, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos + 80, piece.ypos - 80, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				kingMove = Tree(piece.xpos + 80, piece.ypos - 80)
				Node.append(kingMove, index)
				index += 1
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos - 80, piece.ypos, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos - 80, piece.ypos, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				kingMove = Tree(piece.xpos - 80, piece.ypos)
				Node.append(kingMove, index)
				index += 1
			possible = False
			futureSquare = chessboard.square_finder(piece.xpos + 160, piece.ypos, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos + 160, piece.ypos, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				kingMove = Tree(piece.xpos + 160, piece.ypos)
				Node.append(kingMove, index)
				index += 1
			futureSquare = chessboard.square_finder(piece.xpos - 160, piece.ypos, grid)
			if futureSquare != None:
				possible = piece.move(piece.xpos - 160, piece.ypos, Color, oppositeColor, oldSquare, futureSquare, grid, True)
				piece.set(oldxpos, oldypos)
				oldSquare.occupant = piece
			if possible:
				kingMove = Tree(piece.xpos - 160, piece.ypos)
				Node.append(kingMove, index)
				index += 1

		distance += 1

	return Moves

def plyGenerator(Color, oppositeColor, moves):
	plyPlayer = deepCopy(Color)
	oppositePlayer = deepCopy(oppositeColor)
	Pieces = plyPlayer.sprites() + oppositePlayer.sprites()
	gridsquare = chessboard.convert(pygame.Surface((80, 80)).convert_alpha())
	boardState = []
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
				boardState.append(s)
			else:
				s = chessboard.Square(gridsquare, x, y, None)
				#screen.blit(s.image, (x, y))
				boardState.append(s)

	while len(moves.children) != 0:
		currentTree = moves.children[0]
		piece = currentTree.node1
		gridsquare = chessboard.convert(pygame.Surface((80, 80)).convert_alpha())
		realPiece = None
		for Piece in plyPlayer.sprites():
			if Piece.xpos == piece.xpos and Piece.ypos == piece.ypos:
				realPiece = Piece
		if realPiece != None:
			oldxpos = realPiece.xpos
			oldypos = realPiece.ypos
			if len(currentTree.children) != 0:
				currentMove = currentTree.children[0]
				moves.children[0].children.remove(currentTree.children[0])
				oldSquare = chessboard.square_finder(oldxpos, oldypos, boardState)
				futureSquare = chessboard.square_finder(currentMove.node1, currentMove.node2, boardState)
				if futureSquare != None and oldSquare != None:
					realPiece.move(currentMove.node1, currentMove.node2, plyPlayer, oppositePlayer, oldSquare, futureSquare, boardState, False)
					king = None
					for o in plyPlayer.sprites():
						if type(o) == chessboard.King:
							king = o
					if king.check(plyPlayer, oppositePlayer, boardState):
						realPiece.set(oldxpos, oldypos)
						oldSquare.occupant = realPiece
					if realPiece.xpos != oldxpos or realPiece.ypos != oldypos:
						futureSquare.occupant = realPiece
					else:
						realPiece.set(oldxpos, oldypos)
						oldSquare.occupant = realPiece
			
					if type(realPiece) == chessboard.Pawn:
						if realPiece.color == "white":
							if realPiece.ypos == 40:
								currentPiecexpos = realPiece.xpos
								currentPieceypos = realPiece.ypos
								moves.children.remove(currentTree)
								realPiece.kill()
								white_knight = chessboard.Knight('whiteknight.png', currentPiecexpos, currentPieceypos, 'white')
								plyPlayer.add(white_knight)
								futureSquare.occupant = white_knight
								otherKing = None
								for piece in oppositePlayer:
									if type(piece) == chessboard.King:
										otherKing = piece
								if not otherKing.checkmate(plyPlayer, oppositePlayer, boardState):
									white_knight.kill()
									white_queen = chessboard.Queen('whitequeen.jpg', currentPiecexpos, currentPieceypos, 'white')
									plyPlayer.add(white_queen)
									futureSquare.occupant = white_queen
									if otherKing.stalemate(plyPlayer, oppositePlayer, boardState):
										white_queen.kill()
										white_rook = chessboard.Rook('whiterook.png', currentPiecexpos, currentPieceypos, 'white')
										plyPlayer.add(white_rook)
										futureSquare.occupant = white_rook
										if otherKing.stalemate(plyPlayer, oppositePlayer, boardState):
											white_rook.kill()
											white_bishop = chessboard.Bishop('whitebishop.png', currentPiecexpos, currentPieceypos, 'white')
											plyPlayer.add(white_bishop)
											futureSquare.occupant = white_bishop
									
						if realPiece.color == "black":
							if realPiece.ypos == 600:
								currentPiecexpos = realPiece.xpos
								currentPieceypos = realPiece.ypos
								moves.children.remove(currentTree)
								realPiece.kill()
								black_knight = chessboard.Knight('blackknight.gif', currentPiecexpos, currentPieceypos, 'black')
								plyPlayer.add(black_knight)
								futureSquare.occupant = black_knight
								otherKing = None
								for piece in oppositePlayer:
									if type(piece) == chessboard.King:
										otherKing = piece
								if not otherKing.checkmate(plyPlayer, oppositePlayer, boardState):
									black_knight.kill()
									black_queen = chessboard.Queen('blackqueen.png', currentPiecexpos, currentPieceypos, 'black')
									plyPlayer.add(black_queen)
									futureSquare.occupant = black_queen
									if otherKing.stalemate(plyPlayer, oppositePlayer, boardState):
										black_queen.kill()
										black_rook = chessboard.Rook('blackrook.png', currentPiecexpos, currentPieceypos, 'black')
										plyPlayer.add(black_rook)
										futureSquare.occupant = black_rook
										if otherKing.stalemate(plyPlayer, oppositePlayer, boardState):
											black_rook.kill()
											black_bishop = chessboard.Bishop('blackbishop.png', currentPiecexpos, currentPieceypos, 'black')
											plyPlayer.add(black_bishop)
											futureSquare.occupant = black_bishop						
					
					if realPiece.xpos != oldxpos or realPiece.ypos != oldypos:
						ply = Tree(plyPlayer, oppositePlayer, boardState, 0, 100)
						return ply

			else:
				moves.children.remove(moves.children[0])
		else:
			moves.children.remove(moves.children[0])

	return None

def evaluation(Color, oppositeColor, grid):
	colorSprites = Color.sprites()
	opposite_colorSprites = oppositeColor.sprites()

	King = None
	for piece in colorSprites:
		if type(piece) == chessboard.King:
			King = piece
	
	otherKing = None
	for piece in opposite_colorSprites:
		if type(piece) == chessboard.King:
			otherKing = piece

	if otherKing.checkmate(oppositeColor, Color, grid):
		return 100

	elif King.checkmate(Color, oppositeColor, grid):
		return 0 

	elif King.stalemate(Color, oppositeColor, grid) or otherKing.stalemate(oppositeColor, Color, grid):
		return 50

	else:
		score = 50
		value = 1 - num_inColor(oppositeColor, chessboard.Queen)
		score += 40 * value
		value = 2 - num_inColor(oppositeColor, chessboard.Rook)
		score += 20 * value
		value = 2 - num_inColor(oppositeColor, chessboard.Bishop)
		score += 10 * value
		value = 2 - num_inColor(oppositeColor, chessboard.Knight)
		score += 10 * value
		value = 8 - num_inColor(oppositeColor, chessboard.Pawn)
		score += 1 * value

		value = 1 - num_inColor(Color, chessboard.Queen)
		score -= 40 * value
		value = 2 - num_inColor(Color, chessboard.Rook)
		score -= 20 * value
		value = 2 - num_inColor(Color, chessboard.Bishop)
		score -= 10 * value
		value = 2 - num_inColor(Color, chessboard.Knight)
		score -= 10 * value
		value = 8 - num_inColor(Color, chessboard.Pawn)
		score -= 1 * value

		otherQueen = None
		for piece in opposite_colorSprites:
			if type(piece) == chessboard.Queen:
				otherQueen = piece
				opposite_colorSprites.remove(piece)

		otherKnight1 = None
		found = False
		for piece in opposite_colorSprites:
			if not found:
				if type(piece) == chessboard.Knight:
					found = True
					otherKnight1 = piece
					opposite_colorSprites.remove(piece)	

		otherKnight2 = None
		found = False
		for piece in opposite_colorSprites:
			if not found:
				if type(piece) == chessboard.Knight:
					found = True
					otherKnight2 = piece
					opposite_colorSprites.remove(piece)		

		otherBishop1 = None
		found = False
		for piece in opposite_colorSprites:
			if not found:
				if type(piece) == chessboard.Bishop:
					found = True
					otherBishop1 = piece
					opposite_colorSprites.remove(piece)		

		otherBishop2 = None
		found = False
		for piece in opposite_colorSprites:
			if not found:
				if type(piece) == chessboard.Bishop:
					found = True
					otherBishop2 = piece
					opposite_colorSprites.remove(piece)

		otherRook1 = None
		found = False
		for piece in opposite_colorSprites:
			if not found:
				if type(piece) == chessboard.Rook:
					found = True
					otherRook1 = piece
					opposite_colorSprites.remove(piece)
			
		otherRook2 = None
		found = False
		for piece in opposite_colorSprites:
			if not found:
				if type(piece) == chessboard.Rook:
					found = True
					otherRook2 = piece
					opposite_colorSprites.remove(piece)

		if otherKing != None and otherQueen != None and otherRook1 != None and otherRook2 != None and otherBishop1 != None and otherBishop2 != None and otherKnight1 != None and otherKnight2 != None:

			if otherQueen.underAttack(oppositeColor, Color, grid) and otherKing.check(oppositeColor, Color, grid):
				score += 40

			elif otherKing.check(oppositeColor, Color, grid) and (otherRook1.underAttack(oppositeColor, Color, grid) or otherRook2.underAttack(oppositeColor, Color, grid)):
				score += 35

			elif otherKing.check(oppositeColor, Color, grid) and (otherBishop1.underAttack(oppositeColor, Color, grid) or otherBishop2.underAttack(oppositeColor, Color, grid)):
				score += 25

			elif otherKing.check(oppositeColor, Color, grid) and (otherKnight1.underAttack(oppositeColor, Color, grid) or otherKnight2.underAttack(oppositeColor, Color, grid)):
				score += 25

			elif otherQueen.underAttack(oppositeColor, Color, grid) and (otherRook1.underAttack(oppositeColor, Color, grid) or otherRook2.underAttack(oppositeColor, Color, grid)):
				score += 30

			elif otherQueen.underAttack(oppositeColor, Color, grid) and (otherBishop1.underAttack(oppositeColor, Color, grid) or otherBishop2.underAttack(oppositeColor, Color, grid)):
				score += 20

			elif otherQueen.underAttack(oppositeColor, Color, grid) and (otherKnight1.underAttack(oppositeColor, Color, grid) or otherKnight2.underAttack(oppositeColor, Color, grid)):
				score += 20

			elif otherRook1.underAttack(oppositeColor, Color, grid) and otherRook2.underAttack(oppositeColor, Color, grid):
				score += 30

			elif otherBishop1.underAttack(oppositeColor, Color, grid) and otherBishop2.underAttack(oppositeColor, Color, grid):
				score += 20 

			elif otherKnight1.underAttack(oppositeColor, Color, grid) and otherKnight2.underAttack(oppositeColor, Color, grid):
				score += 20

			elif (otherRook1.underAttack(oppositeColor, Color, grid) or otherRook2.underAttack(oppositeColor, Color, grid)) and (otherBishop1.underAttack(oppositeColor, Color, grid) or otherBishop2.underAttack(oppositeColor, Color, grid)):
				score += 20

			elif (otherRook1.underAttack(oppositeColor, Color, grid) or otherRook2.underAttack(oppositeColor, Color, grid)) and (otherKnight1.underAttack(oppositeColor, Color, grid) or otherKnight2.underAttack(oppositeColor, Color, grid)):
				score += 20 

			elif otherKing.check(oppositeColor, Color, grid):
				score += 12

			elif otherQueen.underAttack(oppositeColor, Color, grid):
				score += 10

			elif (otherRook1.underAttack(oppositeColor, Color, grid) or otherRook2.underAttack(oppositeColor, Color, grid)):
				score += 7

			elif (otherBishop1.underAttack(oppositeColor, Color, grid) or otherBishop2.underAttack(oppositeColor, Color, grid)):
				score += 5

			elif (otherKnight1.underAttack(oppositeColor, Color, grid) or otherKnight2.underAttack(oppositeColor, Color, grid)):
				score += 5


		return score

def minimax(tree, switch):
	if len(tree.get_leftMost().children) == 0:
		if not switch:
			maxi = tree.get_leftMost().value
			for child in tree.children:
				if child.value > maxi:
					maxi = child.value
			tree.value = maxi
			return maxi
		if switch:
			mini = tree.get_leftMost().value
			for child in tree.children:
				if child.value < mini:
					mini = child.value
			tree.value = mini
			return mini

	else:
		if switch:
			tree.value = minimax(tree.get_leftMost(), False)
		if not switch:
			tree.value = minimax(tree.get_leftMost(), True)

	if tree.parent != None:
		for child in tree.children:
			if child.value == None:
				if switch:
					tree.value = minimax(tree.getChild(child.fromLeft), False)
				if not switch:
					tree.value = minimax(tree.getChild(child.fromLeft), True)		
	else:
		for child in tree.children:
			if child.value == None:
				tree.value = minimax(tree.getChild(child.fromLeft), False)

		if tree.allSet():	
			maxi = tree.get_leftMost().value
			for child in tree.children:
				if child.value > maxi:
					maxi = child.value
			tree.value = maxi
			return maxi

	if tree.allSet():
		if not switch:
			maxi = tree.get_leftMost().value
			for child in tree.children:
				if child.value > maxi:
					maxi = child.value
			tree.value = maxi
			return maxi
		if switch:
			mini = tree.get_leftMost().value
			for child in tree.children:
				if child.value < mini:
					mini = child.value
			tree.value = mini
			return mini		

def alpha_betaPrune(currentTree, wholeTree, switch, depth):
	if depth == 3:
		print("hit depth 3")
		moves = possibleMoves(currentTree.node2, currentTree.node1, currentTree.node3)
		possiblePly = plyGenerator(currentTree.node2, currentTree.node1, moves)
		distance = 0
		if possiblePly != None:
			possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
			currentTree.append(possiblePly, distance)
			wholeTree = currentTree.getRoot(currentTree)
			minimax(wholeTree, True)
			if not switch:
				if currentTree.value != None:
					possiblePly.alpha = currentTree.value
					possiblePly.beta = currentTree.beta
				else:
					possiblePly.alpha = currentTree.alpha
					possiblePly.beta = currentTree.beta
			if switch:
				if currentTree.value != None:
					possiblePly.alpha = currentTree.alpha
					possiblePly.beta = currentTree.value
				else:
					possiblePly.alpha = currentTree.alpha
					possiblePly.beta = currentTree.beta
			wholeTree = currentTree.getRoot(currentTree)
			minimax(wholeTree, True)
		prune = False
		while possiblePly != None and not prune:
			print("still at depth 3")
			if not switch:
				if possiblePly.value > possiblePly.beta:
					prune = True
			if switch:
				if possiblePly.value < possiblePly.alpha:
					prune = True
			if not prune:
				possiblePly = plyGenerator(currentTree.node2, currentTree.node1, moves)
				distance += 1
				if possiblePly != None:
					possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
					currentTree.append(possiblePly, distance)
					if not switch:
						if currentTree.value != None:
							possiblePly.alpha = currentTree.value
							possiblePly.beta = currentTree.beta
						else:
							possiblePly.alpha = currentTree.alpha
							possiblePly.beta = currentTree.beta
					if switch:
						if currentTree.value != None:
							possiblePly.alpha = currentTree.alpha
							possiblePly.beta = currentTree.value
						else:
							possiblePly.alpha = currentTree.alpha
							possiblePly.beta = currentTree.beta
					wholeTree = currentTree.getRoot(currentTree)
					minimax(wholeTree, True)
		
		return wholeTree.value

	moves = possibleMoves(currentTree.node1, currentTree.node2, currentTree.node3)

	if depth == 0:
		possiblePly = plyGenerator(currentTree.node1, currentTree.node2, moves)
		if possiblePly != None:
			King = None
			for piece in possiblePly.node1:
				if type(piece) == chessboard.King:
					King = piece
			otherKing = None
			for piece in possiblePly.node2:
				if type(piece) == chessboard.King:
					otherKing = piece
			if King.checkmate(possiblePly.node1, possiblePly.node2, possiblePly.node3) or King.stalemate(possiblePly.node1, possiblePly.node2, possiblePly.node3):
				possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
				wholeTree = currentTree.getRoot(currentTree)
				minimax(wholeTree, True)
				return wholeTree.value
			if otherKing.checkmate(possiblePly.node2, possiblePly.node1, possiblePly.node3) or otherKing.stalemate(possiblePly.node2, possiblePly.node1, possiblePly.node3):
				possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
				wholeTree = currentTree.getRoot(currentTree)
				minimax(wholeTree, True)
				return wholeTree.value
			currentTree.append(possiblePly, 0)
			possiblePly.alpha = currentTree.alpha
			possiblePly.beta = currentTree.beta
			wholeTree = currentTree.getRoot(currentTree)
			depth += 1
			wholeTree.value = alpha_betaPrune(currentTree.get_leftMost(), wholeTree, False, depth)
			depth -= 1

	moves = possibleMoves(currentTree.node2, currentTree.node1, currentTree.node3)
	
	if depth > 0 and depth < 5:
		possiblePly = plyGenerator(currentTree.node2, currentTree.node1, moves)
		if possiblePly != None:
			King = None
			for piece in possiblePly.node1:
				if type(piece) == chessboard.King:
					King = piece
			otherKing = None
			for piece in possiblePly.node2:
				if type(piece) == chessboard.King:
					otherKing = piece
			if King.checkmate(possiblePly.node1, possiblePly.node2, possiblePly.node3) or King.stalemate(possiblePly.node1, possiblePly.node2, possiblePly.node3):
				possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
				wholeTree = currentTree.getRoot(currentTree)
				minimax(wholeTree, True)
				return wholeTree.value
			if otherKing.checkmate(possiblePly.node2, possiblePly.node1, possiblePly.node3) or otherKing.stalemate(possiblePly.node2, possiblePly.node1, possiblePly.node3):
				possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
				wholeTree = currentTree.getRoot(currentTree)
				minimax(wholeTree, True)
				return wholeTree.value
			
			currentTree.append(possiblePly, 0)
			if not switch:
				if currentTree.value != None:
					possiblePly.alpha = currentTree.value
					possiblePly.beta = currentTree.beta
				else:
					possiblePly.alpha = currentTree.alpha
					possiblePly.beta = currentTree.beta
			if switch:
				if currentTree.value != None:
					possiblePly.alpha = currentTree.alpha
					possiblePly.beta = currentTree.value
				else:
					possiblePly.alpha = currentTree.alpha
					possiblePly.beta = currentTree.beta

			wholeTree = currentTree.getRoot(currentTree)

			if switch:
				depth += 1
				wholeTree.value = alpha_betaPrune(currentTree.get_leftMost(), wholeTree, False, depth)
				print("return to depth 2")
				depth -= 1
			if not switch:
				depth += 1
				wholeTree.value = alpha_betaPrune(currentTree.get_leftMost(), wholeTree, True, depth)	
				print("return to depth 2")
				depth -= 1	

	if currentTree.parent != None:
		possiblePly = plyGenerator(currentTree.node2, currentTree.node1, moves)
		distance = 1
		if possiblePly != None:
			King = None
			for piece in possiblePly.node1:
				if type(piece) == chessboard.King:
					King = piece
			otherKing = None
			for piece in possiblePly.node2:
				if type(piece) == chessboard.King:
					otherKing = piece
			if King.checkmate(possiblePly.node1, possiblePly.node2, possiblePly.node3) or King.stalemate(possiblePly.node1, possiblePly.node2, possiblePly.node3):
				possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
				wholeTree = currentTree.getRoot(currentTree)
				minimax(wholeTree, True)
				return wholeTree.value
			if otherKing.checkmate(possiblePly.node2, possiblePly.node1, possiblePly.node3) or otherKing.stalemate(possiblePly.node2, possiblePly.node1, possiblePly.node3):
				possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
				wholeTree = currentTree.getRoot(currentTree)
				minimax(wholeTree, True)
				return wholeTree.value
			
			currentTree.append(possiblePly, distance)
			if not switch:
				if currentTree.value != None:
					possiblePly.alpha = currentTree.value
					possiblePly.beta = currentTree.beta
				else:
					possiblePly.alpha = currentTree.alpha
					possiblePly.beta = currentTree.beta
			if switch:
				if currentTree.value != None:
					possiblePly.alpha = currentTree.alpha
					possiblePly.beta = currentTree.value
				else:
					possiblePly.alpha = currentTree.alpha
					possiblePly.beta = currentTree.beta
			wholeTree = currentTree.getRoot(currentTree)
		
		prune = False
		while possiblePly != None and not prune:
			if switch:
				depth += 1
				wholeTree.value = alpha_betaPrune(currentTree.getChild(distance), wholeTree, False, depth)
			if not switch:
				depth += 1
				wholeTree.value = alpha_betaPrune(currentTree.getChild(distance), wholeTree, True, depth)
			if not switch:
				if currentTree.value != None:
					if currentTree.value > currentTree.beta:
						prune = True
			if switch:
				if currentTree.value != None:
					if currentTree.value < currentTree.alpha:
						prune = True
			if not prune:
				possiblePly = plyGenerator(currentTree.node2, currentTree.node1, moves)				
				distance += 1
				if possiblePly != None:
					King = None
					for piece in possiblePly.node1:
						if type(piece) == chessboard.King:
							King = piece
					otherKing = None
					for piece in possiblePly.node2:
						if type(piece) == chessboard.King:
							otherKing = piece
					if King.checkmate(possiblePly.node1, possiblePly.node2, possiblePly.node3) or King.stalemate(possiblePly.node1, possiblePly.node2, possiblePly.node3):
						possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
						wholeTree = currentTree.getRoot(currentTree)
						minimax(wholeTree, True)
						return wholeTree.value
					if otherKing.checkmate(possiblePly.node2, possiblePly.node1, possiblePly.node3) or otherKing.stalemate(possiblePly.node2, possiblePly.node1, possiblePly.node3):
						possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
						wholeTree = currentTree.getRoot(currentTree)
						minimax(wholeTree, True)
						return wholeTree.value
					
					currentTree.append(possiblePly, distance)
					if not switch:
						if currentTree.value != None:
							possiblePly.alpha = currentTree.value
							possiblePly.beta = currentTree.beta
						else:
							possiblePly.alpha = currentTree.alpha
							possiblePly.beta = currentTree.beta
					if switch:
						if currentTree.value != None:
							possiblePly.alpha = currentTree.alpha
							possiblePly.beta = currentTree.value
						else:
							possiblePly.alpha = currentTree.alpha
							possiblePly.beta = currentTree.beta
					wholeTree = currentTree.getRoot(currentTree)
					depth -= 1

		return wholeTree.value

	else:
		possiblePly = plyGenerator(currentTree.node1, currentTree.node2, moves)
		distance = 1
		if possiblePly != None:
			King = None
			for piece in possiblePly.node1:
				if type(piece) == chessboard.King:
					King = piece
			otherKing = None
			for piece in possiblePly.node2:
				if type(piece) == chessboard.King:
					otherKing = piece
			if King.checkmate(possiblePly.node1, possiblePly.node2, possiblePly.node3) or King.stalemate(possiblePly.node1, possiblePly.node2, possiblePly.node3):
				possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
				wholeTree = currentTree.getRoot(currentTree)
				minimax(wholeTree, True)
				return wholeTree.value
			if otherKing.checkmate(possiblePly.node2, possiblePly.node1, possiblePly.node3) or otherKing.stalemate(possiblePly.node2, possiblePly.node1, possiblePly.node3):
				possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
				wholeTree = currentTree.getRoot(currentTree)
				minimax(wholeTree, True)
				return wholeTree.value
			
			currentTree.append(possiblePly, distance)
			possiblePly.alpha = currentTree.value
			possiblePly.beta = currentTree.beta
		while possiblePly != None:
			if switch:
				depth += 1
				wholeTree.value = alpha_betaPrune(currentTree.getChild(distance), wholeTree, False, depth)
			if not switch:
				depth += 1
				wholeTree.value = alpha_betaPrune(currentTree.getChild(distance), wholeTree, True, depth)
			possiblePly = plyGenerator(currentTree.node1, currentTree.node2, moves)
			distance += 1
			if possiblePly != None:
				King = None
				for piece in possiblePly.node1:
					if type(piece) == chessboard.King:
						King = piece
				otherKing = None
				for piece in possiblePly.node2:
					if type(piece) == chessboard.King:
						otherKing = piece
				if King.checkmate(possiblePly.node1, possiblePly.node2, possiblePly.node3) or King.stalemate(possiblePly.node1, possiblePly.node2, possiblePly.node3):
					possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
					wholeTree = currentTree.getRoot(currentTree)
					minimax(wholeTree, True)
					return wholeTree.value
				if otherKing.checkmate(possiblePly.node2, possiblePly.node1, possiblePly.node3) or otherKing.stalemate(possiblePly.node2, possiblePly.node1, possiblePly.node3):
					possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
					wholeTree = currentTree.getRoot(currentTree)
					minimax(wholeTree, True)
					return wholeTree.value
				possiblePly.alpha = currentTree.value
				possiblePly.beta = currentTree.beta
				currentTree.append(possiblePly, distance)
				depth -= 1

		return wholeTree.value	

def movement_whitePlayer(white, event, grid, screen, board, clearBoard, black, players):
	whiteState = white
	blackState = black
	gameTree = Tree(whiteState, blackState, grid, 0, 100)

	boardState = grid
	moves = possibleMoves(gameTree.node1, gameTree.node2, boardState)
	possiblePly = plyGenerator(gameTree.node1, gameTree.node2, moves)
	distance = 0
	if possiblePly != None:
		gameTree.append(possiblePly, distance)
	while possiblePly != None:
		distance += 1
		possiblePly = plyGenerator(gameTree.node1, gameTree.node2, moves)
		if possiblePly != None:
			gameTree.append(possiblePly, distance)

	for child in gameTree.children:
		boardState = child.node3
		moves = possibleMoves(child.node2, child.node1, boardState)
		possiblePly = plyGenerator(child.node2, child.node1, moves)
		distance = 0
		if possiblePly != None:
			possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
			child.append(possiblePly, distance)
		while possiblePly != None:
			distance += 1
			possiblePly = plyGenerator(child.node2, child.node1, moves)
			if possiblePly != None:
				possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
				child.append(possiblePly, distance)

	maxMove = minimax(gameTree, True)

	#maxMove = alpha_betaPrune(gameTree, gameTree, True, 0)
	ply = None
	for child in gameTree.children:
		if child.value == maxMove:
			ply = child

	white = ply.node1
	black = ply.node2
	players.clear(board, clearBoard)
	players.draw(board)
	screen.blit(board, (0, 0))
	pygame.display.update()

	return False

def movement_blackPlayer(black, event, grid, screen, board, clearBoard, white, players):
	gameTree = Tree(black, white, grid, 0, 100)

	#boardState = grid
	#moves = possibleMoves(gameTree.node1, gameTree.node2, boardState)
	#ply = plyGenerator(gameTree.node1, gameTree.node2, moves)

	boardState = grid
	moves = possibleMoves(gameTree.node1, gameTree.node2, boardState)
	possiblePly = plyGenerator(gameTree.node1, gameTree.node2, moves)
	distance = 0
	if possiblePly != None:
		gameTree.append(possiblePly, distance)
		possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
		print(possiblePly.value)
	while possiblePly != None:
		distance += 1
		possiblePly = plyGenerator(gameTree.node1, gameTree.node2, moves)
		if possiblePly != None:
			gameTree.append(possiblePly, distance)
			possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
			print(possiblePly.value)

	#print("past 1st level")
	#for child in gameTree.children:
		#print("next part")
		#boardState = child.node3
		#moves = possibleMoves(child.node2, child.node1, boardState)
		#possiblePly = plyGenerator(child.node2, child.node1, moves)
		#distance = 0
		#if possiblePly != None:
			#possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
			#child.append(possiblePly, distance)
		#while possiblePly != None:
			#print("2nd level")
			#distance += 1
			#possiblePly = plyGenerator(child.node2, child.node1, moves)
			#if possiblePly != None:
				#possiblePly.value = evaluation(possiblePly.node1, possiblePly.node2, possiblePly.node3)
				#child.append(possiblePly, distance)
	#print("past 2nd level")

	#maxMove = minimax(gameTree, True)

	#maxMove = alpha_betaPrune(gameTree, gameTree, True, 0)
	#ply = None
	#for child in gameTree.children:
		#if child.value == maxMove:
			#ply = child
	
	ply = None
	maxValue = 0
	for child in gameTree.children:
		if child.value > maxValue:
			maxValue = child.value
			ply = child

	print("chosen value:", ply.value)

	colorList = black.sprites()
	new_colorList = ply.node1.sprites()

	same_colorList = []
	same_new_colorList = []
	oldPiece = []
	newPiece = []

	for piece in colorList:
		for checkPiece in new_colorList:
			if type(checkPiece) == type(piece):
				if checkPiece.xpos == piece.xpos and checkPiece.ypos ==  piece.ypos:
					same_colorList.append(piece)
					same_new_colorList.append(checkPiece)

	for piece in colorList:
		if piece not in same_colorList:
			oldPiece.append(piece)

	for piece in new_colorList:
		if piece not in same_new_colorList:
			newPiece.append(piece)
	
	Piece = None
	movedPiece = None
	pawnPromotion = False
	if len(oldPiece) == 1:
		if type(oldPiece[0]) == type(newPiece[0]):
			for piece in black.sprites():
				if piece == oldPiece[0]:
					Piece = piece
					movedPiece = newPiece[0]
		else:
			for piece in black.sprites():
				if piece == oldPiece[0]:
					Piece = piece
					movedPiece = newPiece[0]
					pawnPromotion = True

	if len(oldPiece) == 2:
		if type(oldPiece[0]) == chessboard.King:
			for piece in black.sprites():
				if piece == oldPiece[0]:
					Piece = piece
			for newpiece in newPiece:
				if type(newpiece) == chessboard.King:
					movedPiece = newpiece
		else:
			for piece in black.sprites():
				if piece == oldPiece[1]:
					Piece = piece
			for newpiece in newPiece:
				if type(newpiece) == chessboard.King:
					movedPiece = newpiece


	if pawnPromotion == False:
		oldSquare = chessboard.square_finder(Piece.xpos, Piece.ypos, grid)
		futureSquare = chessboard.square_finder(movedPiece.xpos, movedPiece.ypos, grid)
		Piece.move(movedPiece.xpos, movedPiece.ypos, black, white, oldSquare, futureSquare, grid, False)
		futureSquare.occupant = Piece

	else:
		oldSquare = chessboard.square_finder(Piece.xpos, Piece.ypos, grid)
		futureSquare = chessboard.square_finder(movedPiece.xpos, movedPiece.ypos, grid)
		Piece.move(movedPiece.xpos, movedPiece.ypos, black, white, oldSquare, futureSquare, grid, False)
		if type(movedPiece) == chessboard.Knight:
			black_knight = chessboard.Knight('blackknight.gif', movedPiece.xpos, movedPiece.ypos, 'black')
			black.add(black_knight)
			players.add(black_knight)
			futureSquare.occupant = black_knight
			Piece.kill()
		elif type(movedPiece) == chessboard.Bishop:
			black_bishop = chessboard.Bishop('blackbishop.png', movedPiece.xpos, movedPiece.ypos, 'black')
			black.add(black_bishop)
			players.add(black_bishop)
			futureSquare.occupant = black_bishop
			Piece.kill()
		elif type(movedPiece) == chessboard.Rook:
			black_rook = chessboard.Rook('blackrook.png', movedPiece.xpos, movedPiece.ypos, 'black')
			black.add(black_rook)
			players.add(black_rook)
			futureSquare.occupant = black_rook
			Piece.kill()
		elif type(movedPiece) == chessboard.Queen:
			black_queen = chessboard.Queen('blackqueen.png', movedPiece.xpos, movedPiece.ypos, 'black')
			black.add(black_queen)
			players.add(black_queen)
			futureSquare.occupant = black_queen
			Piece.kill()

	players.clear(board, clearBoard)
	players.draw(board)
	screen.blit(board, (0, 0))
	pygame.display.update()
	print("break")

	return True