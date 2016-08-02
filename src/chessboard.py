import pygame

pygame.init()

class Pawn(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        pygame.display.set_mode()
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.xpos = x
        self.ypos = y
        self.color = color
        self.firstMove = True
        self.switch = False

    def set(self, x, y):
        self.xpos = x
        self.ypos = y
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, x, y, Color, oppositeColor, oldSquare, futureSquare, grid, test):
        king = None
        for piece in Color.sprites():
            if type(piece) == King:
                king = piece
        if self.firstMove:
            if self.color == 'white':
                if x == self.xpos and (y == self.ypos - 80 or y == self.ypos - 160):
                    if y == self.ypos - 160:
                        spot = None
                        for square in grid:
                            if square.xpos == x and square.ypos == y + 80:
                                spot = square
                        if spot.occupant == None:
                            if futureSquare.occupant == None:
                                self.rect = self.image.get_rect(center=(x, y))
                                self.xpos = x
                                self.ypos = y
                                if not king.check(Color, oppositeColor, grid):
                                    if not test:
                                        self.firstMove = False
                                        oldSquare.occupant = None
                                        self.switch = True
                                    else:
                                        return True
                    elif futureSquare.occupant == None:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                self.firstMove = False
                                oldSquare.occupant = None
                            else:
                                return True
                elif (x == self.xpos - 80 or x == self.xpos + 80) and y == self.ypos - 80:
                    if futureSquare.occupant != None:
                        if futureSquare.occupant.color != self.color:
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    self.firstMove = False
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True    
                            else:
                                futureSquare.occupant.add(oppositeColor)
            elif self.color == 'black':
                if x == self.xpos and (y == self.ypos + 80 or y == self.ypos + 160):
                    if y == self.ypos + 160:
                        spot = None
                        for square in grid:
                            if square.xpos == x and square.ypos == y - 80:
                                spot = square
                        if spot.occupant == None:
                            if futureSquare.occupant == None:
                                self.rect = self.image.get_rect(center=(x, y))
                                self.xpos = x
                                self.ypos = y
                                if not king.check(Color, oppositeColor, grid):
                                    if not test:
                                        self.firstMove = False
                                        oldSquare.occupant = None
                                        self.switch = True
                                    else:
                                        return True
                    elif futureSquare.occupant == None:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                self.firstMove = False
                                oldSquare.occupant = None
                            else:
                                return True
                elif (x == self.xpos - 80 or x == self.xpos + 80) and y == self.ypos + 80:
                    if futureSquare.occupant != None:
                        if futureSquare.occupant.color != self.color:
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    self.firstMove = False
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
        else:
            if self.color == 'white':
                if x == self.xpos and y == self.ypos - 80:
                    if futureSquare.occupant == None:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                oldSquare.occupant = None  
                            else:
                                return True
                elif (x == self.xpos - 80 or x == self.xpos + 80) and y == self.ypos - 80:
                    if futureSquare.occupant != None:
                        if futureSquare.occupant.color != self.color:
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                    else:
                        self.en_passant(x, y, Color, oppositeColor, oldSquare, grid, test)
            elif self.color == 'black':
                if x == self.xpos and y == self.ypos + 80:
                    if futureSquare.occupant == None:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                oldSquare.occupant = None
                            else:
                                return True
                elif (x == self.xpos - 80 or x == self.xpos + 80) and y == self.ypos + 80:
                    if futureSquare.occupant != None:
                        if futureSquare.occupant.color != self.color:
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True    
                            else:
                                futureSquare.occupant.add(oppositeColor)
                    else:
                        self.en_passant(x, y, Color, oppositeColor, oldSquare, grid, test)
        return False

    def en_passant(self, x, y, Color, oppositeColor, oldSquare, grid, test):
        king = None
        for piece in Color.sprites():
            if type(piece) == King:
                king = piece
        if x == self.xpos + 80:
            spot = None
            for square in grid:
                if square.xpos == self.xpos + 80 and square.ypos == self.ypos:
                    spot = square
            if spot != None:
                if spot.occupant != None:
                    if type(spot.occupant) == Pawn:
                        if spot.occupant.color != self.color:
                            if spot.occupant.switch:
                                self.rect = self.image.get_rect(center=(x, y))
                                self.xpos = x
                                self.ypos = y
                                spot.occupant.remove(oppositeColor)
                                if not king.check(Color, oppositeColor, grid):
                                    if not test:
                                        oldSquare.occupant = None
                                        spot.occupant.kill()
                                    else:
                                        spot.occupant.add(oppositeColor)
                                        return True
                                else:
                                    spot.occupant.add(oppositeColor)
        elif x == self.xpos - 80:
            spot = None
            for square in grid:
                if square.xpos == self.xpos - 80 and square.ypos == self.ypos:
                    spot = square
            if spot != None:
                if spot.occupant != None:
                    if type(spot.occupant) == Pawn:
                        if spot.occupant.color != self.color:
                            if spot.occupant.switch:
                                self.rect = self.image.get_rect(center=(x, y))
                                self.xpos = x
                                self.ypos = y
                                spot.occupant.remove(oppositeColor)
                                if not king.check(Color, oppositeColor, grid):
                                    if not test:
                                        oldSquare.occupant = None
                                        spot.occupant.kill()
                                    else:
                                        spot.occupant.add(oppositeColor)
                                        return True    
                                else:
                                    spot.occupant.add(oppositeColor)
                            
class Knight(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        pygame.display.set_mode()
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.xpos = x
        self.ypos = y
        self.color = color

    def set(self, x, y):
        self.xpos = x
        self.ypos = y
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, x, y, Color, oppositeColor, oldSquare, futureSquare, grid, test):
        king = None
        for piece in Color.sprites():
            if type(piece) == King:
                king = piece
        if futureSquare.occupant == None:    
            if x == self.xpos + 80 and y == self.ypos + 160:   
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                    else:
                        return True
            elif x == self.xpos - 80 and y == self.ypos + 160:   
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                    else:
                        return True
            elif x == self.xpos + 80 and y == self.ypos - 160:   
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                    else:
                        return True
            elif x == self.xpos - 80 and y == self.ypos - 160:   
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                    else:
                        return True
            elif x == self.xpos + 160 and y == self.ypos + 80:   
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                    else:
                        return True
            elif x == self.xpos - 160 and y == self.ypos + 80:   
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                    else:
                        return True
            elif x == self.xpos + 160 and y == self.ypos - 80:   
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                    else:
                        return True
            elif x == self.xpos - 160 and y == self.ypos - 80:   
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                    else:
                        return True
        
        elif futureSquare.occupant.color != self.color:
            if x == self.xpos + 80 and y == self.ypos + 160:
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True    
                else:
                    futureSquare.occupant.add(oppositeColor)
            elif x == self.xpos - 80 and y == self.ypos + 160:   
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True
                else:
                    futureSquare.occupant.add(oppositeColor)
            elif x == self.xpos + 80 and y == self.ypos - 160:   
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True
                else:
                    futureSquare.occupant.add(oppositeColor)
            elif x == self.xpos - 80 and y == self.ypos - 160:   
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True
                else:
                    futureSquare.occupant.add(oppositeColor)
            elif x == self.xpos + 160 and y == self.ypos + 80:   
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True
                else:
                    futureSquare.occupant.add(oppositeColor)
            elif x == self.xpos - 160 and y == self.ypos + 80:   
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True
                else:
                    futureSquare.occupant.add(oppositeColor)
            elif x == self.xpos + 160 and y == self.ypos - 80:  
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True
                else:
                    futureSquare.occupant.add(oppositeColor)
            elif x == self.xpos - 160 and y == self.ypos - 80:   
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not king.check(Color, oppositeColor, grid):
                    if not test:
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True
                else:
                    futureSquare.occupant.add(oppositeColor)
        return False

    def underAttack(self, Color, oppositeColor, grid):
        if self.color == 'white':
            for otherPiece in oppositeColor.sprites():
                if (otherPiece.xpos == self.xpos + 80 or otherPiece.xpos == self.xpos - 80) and otherPiece.ypos == self.ypos - 80:
                    if type(otherPiece) == Pawn or type(otherPiece) == Bishop or type(otherPiece) == Queen or type(otherPiece) == King:
                        return True
    
        elif self.color == 'black':
            for otherPiece in oppositeColor.sprites():
                if (otherPiece.xpos == self.xpos + 80 or otherPiece.xpos == self.xpos - 80) and otherPiece.ypos == self.ypos + 80:
                    if type(otherPiece) == Pawn or type(otherPiece) == Bishop or type(otherPiece) == Queen or type(otherPiece) == King:
                        return True
    
        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx > 0 and squareposy > 0):
            squareposx -= 80
            squareposy -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True
    
        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx < 640 and squareposy < 640):
            squareposx += 80
            squareposy += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx < 640 and squareposy > 0):
            squareposx += 80
            squareposy -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True
        
        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx > 0 and squareposy < 640):
            squareposx -= 80
            squareposy += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx > 0):
            squareposx -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx < 640):
            squareposx += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposy > 0):
            squareposy -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposy < 640):
            squareposy += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        for otherPiece in oppositeColor.sprites():
            if otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos + 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos + 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos - 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos - 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos + 160 and otherPiece.ypos == self.ypos + 80:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 160 and otherPiece.ypos == self.ypos + 80:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos + 160 and otherPiece.ypos == self.ypos - 80:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 160 and otherPiece.ypos == self.ypos - 80:
                if type(otherPiece) == Knight:
                    return True

        for otherPiece in oppositeColor.sprites():
            if otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos + 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos - 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos + 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos - 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos and otherPiece.ypos == self.ypos + 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos and otherPiece.ypos == self.ypos - 80: 
                if type(otherPiece) == King:
                    return True

        return False

class Bishop(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        pygame.display.set_mode()
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.xpos = x
        self.ypos = y
        self.color = color

    def set(self, x, y):
        self.xpos = x
        self.ypos = y
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, x, y, Color, oppositeColor, oldSquare, futureSquare, grid, test):
        king = None
        for piece in Color.sprites():
            if type(piece) == King:
                king = piece
        found = False
        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposx > 0 and squareposy > 0):
            squareposx -= 80
            squareposy -= 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False

        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposx < 640 and squareposy < 640):
            squareposx += 80
            squareposy += 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False
        
        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposx < 640 and squareposy > 0):
            squareposx += 80
            squareposy -= 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False

        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposx > 0 and squareposy < 640):
            squareposx -= 80
            squareposy += 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False
        return False

    def underAttack(self, Color, oppositeColor, grid):
        if self.color == 'white':
            for otherPiece in oppositeColor.sprites():
                if (otherPiece.xpos == self.xpos + 80 or otherPiece.xpos == self.xpos - 80) and otherPiece.ypos == self.ypos - 80:
                    if type(otherPiece) == Pawn or type(otherPiece) == Bishop or type(otherPiece) == Queen or type(otherPiece) == King:
                        return True
    
        elif self.color == 'black':
            for otherPiece in oppositeColor.sprites():
                if (otherPiece.xpos == self.xpos + 80 or otherPiece.xpos == self.xpos - 80) and otherPiece.ypos == self.ypos + 80:
                    if type(otherPiece) == Pawn or type(otherPiece) == Bishop or type(otherPiece) == Queen or type(otherPiece) == King:
                        return True
    
        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx > 0 and squareposy > 0):
            squareposx -= 80
            squareposy -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True
    
        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx < 640 and squareposy < 640):
            squareposx += 80
            squareposy += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx < 640 and squareposy > 0):
            squareposx += 80
            squareposy -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True
        
        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx > 0 and squareposy < 640):
            squareposx -= 80
            squareposy += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx > 0):
            squareposx -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx < 640):
            squareposx += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposy > 0):
            squareposy -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposy < 640):
            squareposy += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        for otherPiece in oppositeColor.sprites():
            if otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos + 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos + 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos - 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos - 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos + 160 and otherPiece.ypos == self.ypos + 80:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 160 and otherPiece.ypos == self.ypos + 80:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos + 160 and otherPiece.ypos == self.ypos - 80:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 160 and otherPiece.ypos == self.ypos - 80:
                if type(otherPiece) == Knight:
                    return True

        for otherPiece in oppositeColor.sprites():
            if otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos + 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos - 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos + 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos - 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos and otherPiece.ypos == self.ypos + 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos and otherPiece.ypos == self.ypos - 80: 
                if type(otherPiece) == King:
                    return True

        return False

class Rook(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        pygame.display.set_mode()
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.xpos = x
        self.ypos = y
        self.color = color
        self.firstMove = True

    def set(self, x, y):
        self.xpos = x
        self.ypos = y
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, x, y, Color, oppositeColor, oldSquare, futureSquare, grid, test):
        king = None
        for piece in Color.sprites():
            if type(piece) == King:
                king = piece
        found = False
        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposx > 0):
            squareposx -= 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                if self.firstMove:
                                    self.firstMove = False
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    if self.firstMove:
                                        self.firstMove = False
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False

        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposx < 640):
            squareposx += 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                if self.firstMove:
                                    self.firstMove = False
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    if self.firstMove:
                                        self.firstMove = False
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False
        
        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposy > 0):
            squareposy -= 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                if self.firstMove:
                                    self.firstMove = False
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    if self.firstMove:
                                        self.firstMove = False
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False
        
        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposy < 640):
            squareposy += 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                if self.firstMove:
                                    self.firstMove = False
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    if self.firstMove:
                                        self.firstMove = False
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False
        return False

    def underAttack(self, Color, oppositeColor, grid):
        if self.color == 'white':
            for otherPiece in oppositeColor.sprites():
                if (otherPiece.xpos == self.xpos + 80 or otherPiece.xpos == self.xpos - 80) and otherPiece.ypos == self.ypos - 80:
                    if type(otherPiece) == Pawn or type(otherPiece) == Bishop or type(otherPiece) == Queen or type(otherPiece) == King:
                        return True
    
        elif self.color == 'black':
            for otherPiece in oppositeColor.sprites():
                if (otherPiece.xpos == self.xpos + 80 or otherPiece.xpos == self.xpos - 80) and otherPiece.ypos == self.ypos + 80:
                    if type(otherPiece) == Pawn or type(otherPiece) == Bishop or type(otherPiece) == Queen or type(otherPiece) == King:
                        return True
    
        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx > 0 and squareposy > 0):
            squareposx -= 80
            squareposy -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True
    
        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx < 640 and squareposy < 640):
            squareposx += 80
            squareposy += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx < 640 and squareposy > 0):
            squareposx += 80
            squareposy -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True
        
        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx > 0 and squareposy < 640):
            squareposx -= 80
            squareposy += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx > 0):
            squareposx -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx < 640):
            squareposx += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposy > 0):
            squareposy -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposy < 640):
            squareposy += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        for otherPiece in oppositeColor.sprites():
            if otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos + 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos + 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos - 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos - 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos + 160 and otherPiece.ypos == self.ypos + 80:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 160 and otherPiece.ypos == self.ypos + 80:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos + 160 and otherPiece.ypos == self.ypos - 80:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 160 and otherPiece.ypos == self.ypos - 80:
                if type(otherPiece) == Knight:
                    return True

        for otherPiece in oppositeColor.sprites():
            if otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos + 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos - 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos + 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos - 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos and otherPiece.ypos == self.ypos + 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos and otherPiece.ypos == self.ypos - 80: 
                if type(otherPiece) == King:
                    return True

        return False

class Queen(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        pygame.display.set_mode()
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.xpos = x
        self.ypos = y
        self.color = color

    def set(self, x, y):
        self.xpos = x
        self.ypos = y
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, x, y, Color, oppositeColor, oldSquare, futureSquare, grid, test):
        #oldxpos = self.xpos
        #oldypos = self.ypos
        #Rook.move(self, x, y, Color, oppositeColor, oldSquare, futureSquare, grid, test)
        #if self.xpos == oldxpos and self.ypos == oldypos:
            #Bishop.move(self, x, y, Color, oppositeColor, oldSquare, futureSquare, grid, test)

        king = None
        for piece in Color.sprites():
            if type(piece) == King:
                king = piece
        found = False
        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposx > 0 and squareposy > 0):
            squareposx -= 80
            squareposy -= 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False

        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposx < 640 and squareposy < 640):
            squareposx += 80
            squareposy += 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False
        
        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposx < 640 and squareposy > 0):
            squareposx += 80
            squareposy -= 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False

        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposx > 0 and squareposy < 640):
            squareposx -= 80
            squareposy += 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False

        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposx > 0):
            squareposx -= 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False

        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposx < 640):
            squareposx += 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False
        
        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposy > 0):
            squareposy -= 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False
        
        squareposx = self.xpos
        squareposy = self.ypos
        legal = True
        while legal and not found and (squareposy < 640):
            squareposy += 80
            currentSquare = None
            for square in grid:
                if square.xpos == squareposx and square.ypos == squareposy:
                    currentSquare = square
            if currentSquare == None:
                legal = False
            else:
                if currentSquare.occupant == None:
                    if x == squareposx and y == squareposy:
                        self.rect = self.image.get_rect(center=(x, y))
                        self.xpos = x
                        self.ypos = y
                        if not king.check(Color, oppositeColor, grid):
                            if not test:
                                oldSquare.occupant = None
                                found = True
                            else:
                                return True
                else:
                    if currentSquare.occupant.color != self.color:
                        if x == currentSquare.xpos and y == currentSquare.ypos: 
                            self.rect = self.image.get_rect(center=(x, y))
                            self.xpos = x
                            self.ypos = y
                            futureSquare.occupant.remove(oppositeColor)
                            if not king.check(Color, oppositeColor, grid):
                                if not test:
                                    oldSquare.occupant = None
                                    futureSquare.occupant.kill()
                                    found = True
                                else:
                                    futureSquare.occupant.add(oppositeColor)
                                    return True
                            else:
                                futureSquare.occupant.add(oppositeColor)
                                legal = False
                                found = True
                        else:
                            legal = False
                    else:
                        legal = False
        return False

    def underAttack(self, Color, oppositeColor, grid):
        if self.color == 'white':
            for otherPiece in oppositeColor.sprites():
                if (otherPiece.xpos == self.xpos + 80 or otherPiece.xpos == self.xpos - 80) and otherPiece.ypos == self.ypos - 80:
                    if type(otherPiece) == Pawn or type(otherPiece) == Bishop or type(otherPiece) == Queen or type(otherPiece) == King:
                        return True
    
        elif self.color == 'black':
            for otherPiece in oppositeColor.sprites():
                if (otherPiece.xpos == self.xpos + 80 or otherPiece.xpos == self.xpos - 80) and otherPiece.ypos == self.ypos + 80:
                    if type(otherPiece) == Pawn or type(otherPiece) == Bishop or type(otherPiece) == Queen or type(otherPiece) == King:
                        return True
    
        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx > 0 and squareposy > 0):
            squareposx -= 80
            squareposy -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True
    
        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx < 640 and squareposy < 640):
            squareposx += 80
            squareposy += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx < 640 and squareposy > 0):
            squareposx += 80
            squareposy -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True
        
        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx > 0 and squareposy < 640):
            squareposx -= 80
            squareposy += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx > 0):
            squareposx -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx < 640):
            squareposx += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposy > 0):
            squareposy -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposy < 640):
            squareposy += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        for otherPiece in oppositeColor.sprites():
            if otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos + 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos + 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos - 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos - 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos + 160 and otherPiece.ypos == self.ypos + 80:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 160 and otherPiece.ypos == self.ypos + 80:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos + 160 and otherPiece.ypos == self.ypos - 80:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 160 and otherPiece.ypos == self.ypos - 80:
                if type(otherPiece) == Knight:
                    return True

        for otherPiece in oppositeColor.sprites():
            if otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos + 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos - 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos + 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos - 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos and otherPiece.ypos == self.ypos + 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos and otherPiece.ypos == self.ypos - 80: 
                if type(otherPiece) == King:
                    return True

        return False

class King(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        pygame.display.set_mode()
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.xpos = x
        self.ypos = y
        self.color = color
        self.firstMove = True

    def set(self, x, y):
        self.xpos = x
        self.ypos = y
        self.rect = self.image.get_rect(center=(x, y))

    def check(self, Color, oppositeColor, grid):
        if self.color == 'white':
            for otherPiece in oppositeColor.sprites():
                if (otherPiece.xpos == self.xpos + 80 or otherPiece.xpos == self.xpos - 80) and otherPiece.ypos == self.ypos - 80:
                    if type(otherPiece) == Pawn or type(otherPiece) == Bishop or type(otherPiece) == Queen or type(otherPiece) == King:
                        return True
    
        elif self.color == 'black':
            for otherPiece in oppositeColor.sprites():
                if (otherPiece.xpos == self.xpos + 80 or otherPiece.xpos == self.xpos - 80) and otherPiece.ypos == self.ypos + 80:
                    if type(otherPiece) == Pawn or type(otherPiece) == Bishop or type(otherPiece) == Queen or type(otherPiece) == King:
                        return True
    
        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx > 0 and squareposy > 0):
            squareposx -= 80
            squareposy -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True
    
        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx < 640 and squareposy < 640):
            squareposx += 80
            squareposy += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx < 640 and squareposy > 0):
            squareposx += 80
            squareposy -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True
        
        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx > 0 and squareposy < 640):
            squareposx -= 80
            squareposy += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Bishop and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Bishop or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx > 0):
            squareposx -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposx < 640):
            squareposx += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposy > 0):
            squareposy -= 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        squareposx = self.xpos
        squareposy = self.ypos
        protected = False
        while not protected and (squareposy < 640):
            squareposy += 80
            present = False
            for piece in Color.sprites():
                if piece.xpos == squareposx and piece.ypos == squareposy:
                    present = True
            for otherPiece in oppositeColor.sprites():
                if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                    if not type(otherPiece) == Rook and not type(otherPiece) == Queen:
                        present = True
            if present:
                protected = True
            else:
                for otherPiece in oppositeColor.sprites():
                    if otherPiece.xpos == squareposx and otherPiece.ypos == squareposy:
                        if type(otherPiece) == Rook or type(otherPiece) == Queen:
                            return True

        for otherPiece in oppositeColor.sprites():
            if otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos + 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos + 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos - 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos - 160:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos + 160 and otherPiece.ypos == self.ypos + 80:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 160 and otherPiece.ypos == self.ypos + 80:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos + 160 and otherPiece.ypos == self.ypos - 80:
                if type(otherPiece) == Knight:
                    return True
            elif otherPiece.xpos == self.xpos - 160 and otherPiece.ypos == self.ypos - 80:
                if type(otherPiece) == Knight:
                    return True

        for otherPiece in oppositeColor.sprites():
            if otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos + 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos + 80 and otherPiece.ypos == self.ypos - 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos + 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos - 80 and otherPiece.ypos == self.ypos - 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos and otherPiece.ypos == self.ypos + 80: 
                if type(otherPiece) == King:
                    return True
            elif otherPiece.xpos == self.xpos and otherPiece.ypos == self.ypos - 80: 
                if type(otherPiece) == King:
                    return True

        return False

    def move(self, x, y, Color, oppositeColor, oldSquare, futureSquare, grid, test):
        if futureSquare.occupant == None:
            if x == self.xpos - 80 and y == self.ypos: 
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                    else:
                        return True
            elif x == self.xpos + 80 and y == self.ypos: 
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                    else:
                        return True
            elif x == self.xpos - 80 and y == self.ypos - 80: 
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                    else:
                        return True
            elif x == self.xpos + 80 and y == self.ypos - 80: 
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                    else:
                        return True
            elif x == self.xpos - 80 and y == self.ypos +80: 
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                    else:
                        return True
            elif x == self.xpos + 80 and y == self.ypos + 80: 
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                    else:
                        return True
            elif x == self.xpos and y == self.ypos - 80: 
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                    else:
                        return True
            elif x == self.xpos and y == self.ypos + 80: 
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                    else:
                        return True
            elif (x == self.xpos + 160 or x == self.xpos - 160) and y == self.ypos:
                if not self.check(Color, oppositeColor, grid):
                    self.castle(x, y, Color, oppositeColor, oldSquare, grid)

        elif futureSquare.occupant.color != self.color:
            if x == self.xpos - 80 and y == self.ypos: 
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True
                else:
                    futureSquare.occupant.add(oppositeColor)
            elif x == self.xpos + 80 and y == self.ypos:  
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True
                else:
                    futureSquare.occupant.add(oppositeColor)
            elif x == self.xpos - 80 and y == self.ypos - 80: 
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True
                else:
                    futureSquare.occupant.add(oppositeColor)
            elif x == self.xpos + 80 and y == self.ypos - 80:
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True
                else:
                    futureSquare.occupant.add(oppositeColor)              
            elif x == self.xpos - 80 and y == self.ypos +80: 
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True
                else:
                    futureSquare.occupant.add(oppositeColor)
            elif x == self.xpos + 80 and y == self.ypos + 80: 
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True
                else:
                    futureSquare.occupant.add(oppositeColor)
            elif x == self.xpos and y == self.ypos - 80: 
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True
                else:
                    futureSquare.occupant.add(oppositeColor)
            elif x == self.xpos and y == self.ypos + 80: 
                self.rect = self.image.get_rect(center=(x, y))
                self.xpos = x
                self.ypos = y
                futureSquare.occupant.remove(oppositeColor)
                if not self.check(Color, oppositeColor, grid):
                    if not test:
                        if self.firstMove:
                            self.firstMove = False
                        oldSquare.occupant = None
                        futureSquare.occupant.kill()
                    else:
                        futureSquare.occupant.add(oppositeColor)
                        return True
                else:
                    futureSquare.occupant.add(oppositeColor)
        return False

    def castle(self, x, y, Color, oppositeColor, oldSquare, grid):
        if self.firstMove:
            if x == self.xpos + 160 and y == self.ypos:
                spot = None
                for square in grid:
                    if square.xpos == self.xpos + 80 and square.ypos == self.ypos:
                        spot = square
                if spot.occupant == None:
                    for square in grid:
                        if square.xpos == self.xpos + 160 and square.ypos == self.ypos:
                            spot = square
                    if spot.occupant == None:
                        self.set(self.xpos + 80, self.ypos)
                        if not self.check(Color, oppositeColor, grid):
                            self.set(x, y)
                            if not self.check(Color, oppositeColor, grid):
                                for square in grid:
                                    if square.xpos == self.xpos + 80 and square.ypos == self.ypos:
                                        spot = square
                                if spot.occupant != None:
                                    if type(spot.occupant) == Rook:
                                        if spot.occupant.firstMove:
                                            spot.occupant.set(self.xpos - 80, self.ypos)
                                            spot.occupant.firstMove = False
                                            self.firstMove = False
                                            spot.occupant = None
                                            oldSquare.occupant = None
                                        else:
                                            self.set(oldSquare.xpos, oldSquare.ypos)
                                    else:
                                        self.set(oldSquare.xpos, oldSquare.ypos)
                                else:
                                    self.set(oldSquare.xpos, oldSquare.ypos)
                            else:
                                self.set(oldSquare.xpos, oldSquare.ypos)
                        else:
                            self.set(oldSquare.xpos, oldSquare.ypos)

            elif x == self.xpos - 160 and y == self.ypos:
                spot = None
                for square in grid:
                    if square.xpos == self.xpos - 80 and square.ypos == self.ypos:
                        spot = square
                if spot.occupant == None:
                    for square in grid:
                        if square.xpos == self.xpos - 160 and square.ypos == self.ypos:
                            spot = square
                    if spot.occupant == None:
                        self.set(self.xpos - 80, self.ypos)
                        if not self.check(Color, oppositeColor, grid):
                            self.set(x, y)
                            if not self.check(Color, oppositeColor, grid):
                                for square in grid:
                                    if square.xpos == self.xpos - 160 and square.ypos == self.ypos:
                                        spot = square
                                if spot.occupant != None:
                                    if type(spot.occupant) == Rook:
                                        if spot.occupant.firstMove:
                                            rookSquare = spot
                                            for square in grid:
                                                if square.xpos == rookSquare.occupant.xpos + 80 and square.ypos == rookSquare.occupant.ypos:
                                                    spot = square
                                            if spot.occupant == None:
                                                rookSquare.occupant.set(self.xpos + 80, self.ypos)
                                                rookSquare.occupant.firstMove = False
                                                self.firstMove = False
                                                rookSquare.occupant = None
                                                oldSquare.occupant = None
                                            else:
                                                self.set(oldSquare.xpos, oldSquare.ypos)
                                        else:
                                            self.set(oldSquare.xpos, oldSquare.ypos)
                                    else:
                                        self.set(oldSquare.xpos, oldSquare.ypos)
                                else:
                                    self.set(oldSquare.xpos, oldSquare.ypos)
                            else:
                                self.set(oldSquare.xpos, oldSquare.ypos)
                        else:
                            self.set(oldSquare.xpos, oldSquare.ypos)

    def stalemate(self, Color, oppositeColor, grid):
        if not self.check(Color, oppositeColor, grid):
            colorList = Color.sprites()
            
            while len(colorList) != 0:
                piece = colorList.pop()
                xpos = piece.xpos
                ypos = piece.ypos
                color = piece.color
                possible = False
                currentSquare = square_finder(xpos, ypos, grid)
                
                if type(piece) == Pawn:
                    if color == 'white':
                        newSquare = None
                        for square in grid:
                            if square.xpos == xpos and square.ypos == ypos - 160:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos, ypos - 160, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)
                    
                        for square in grid:
                            if square.xpos == xpos and square.ypos == ypos - 80:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                        for square in grid:
                            if square.xpos == xpos + 80 and square.ypos == ypos - 80:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos + 80, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                        for square in grid:
                            if square.xpos == xpos - 80 and square.ypos == ypos - 80:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos - 80, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    if color == 'black':
                        newSquare = None
                        for square in grid:
                            if square.xpos == xpos and square.ypos == ypos + 160:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos, ypos + 160, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)
                    
                        for square in grid:
                            if square.xpos == xpos and square.ypos == ypos + 80:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                        for square in grid:
                            if square.xpos == xpos + 80 and square.ypos == ypos + 80:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos + 80, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                        for square in grid:
                            if square.xpos == xpos - 80 and square.ypos == ypos + 80:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos - 80, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                elif type(piece) == Knight:
                    newSquare = square_finder(xpos + 80, ypos + 160, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos + 80, ypos + 160, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                    newSquare = square_finder(xpos - 80, ypos + 160, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos - 80, ypos + 160, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                    newSquare = square_finder(xpos - 80, ypos - 160, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos - 80, ypos - 160, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                    newSquare = square_finder(xpos + 80, ypos - 160, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos + 80, ypos - 160, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                    newSquare = square_finder(xpos + 160, ypos + 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos + 160, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                    newSquare = square_finder(xpos - 160, ypos + 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos - 160, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                    newSquare = square_finder(xpos - 160, ypos - 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos - 160, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                    newSquare = square_finder(xpos + 160, ypos - 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos + 160, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                elif type(piece) == Bishop:
                    squareposx = xpos
                    squareposy = ypos
                    while squareposx > 0 and squareposy > 0:
                        squareposx -= 80
                        squareposy -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx < 640 and squareposy < 640:
                        squareposx += 80
                        squareposy += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx < 640 and squareposy > 0:
                        squareposx += 80
                        squareposy -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx > 0 and squareposy < 640:
                        squareposx -= 80
                        squareposy += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                elif type(piece) == Rook:
                    squareposx = xpos
                    squareposy = ypos
                    while squareposx > 0:
                        squareposx -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx < 640:
                        squareposx += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposy > 0:
                        squareposy -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposy < 640:
                        squareposy += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                elif type(piece) == Queen:
                    squareposx = xpos
                    squareposy = ypos
                    while squareposx > 0 and squareposy > 0:
                        squareposx -= 80
                        squareposy -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx < 640 and squareposy < 640:
                        squareposx += 80
                        squareposy += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx < 640 and squareposy > 0:
                        squareposx += 80
                        squareposy -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx > 0 and squareposy < 640:
                        squareposx -= 80
                        squareposy += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx > 0:
                        squareposx -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx < 640:
                        squareposx += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposy > 0:
                        squareposy -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposy < 640:
                        squareposy += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)
                    
                elif type(piece) == King:
                    newSquare = square_finder(xpos + 80, ypos, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos + 80, ypos, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

                    newSquare = square_finder(xpos - 80, ypos, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos - 80, ypos, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

                    newSquare = square_finder(xpos + 80, ypos + 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos + 80, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

                    newSquare = square_finder(xpos - 80, ypos + 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos - 80, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

                    newSquare = square_finder(xpos - 80, ypos - 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos - 80, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

                    newSquare = square_finder(xpos + 80, ypos - 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos + 80, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

                    newSquare = square_finder(xpos, ypos + 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

                    newSquare = square_finder(xpos, ypos - 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

            return True    

    def checkmate(self, Color, oppositeColor, grid):
        if self.check(Color, oppositeColor, grid):
            colorList = Color.sprites()

            while len(colorList) != 0:
                piece = colorList.pop()
                xpos = piece.xpos
                ypos = piece.ypos
                color = piece.color
                possible = False
                currentSquare = square_finder(xpos, ypos, grid)

                if type(piece) == Pawn:
                    if color == 'white':
                        newSquare = None
                        for square in grid:
                            if square.xpos == xpos and square.ypos == ypos - 160:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos, ypos - 160, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)
                    
                        for square in grid:
                            if square.xpos == xpos and square.ypos == ypos - 80:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                        for square in grid:
                            if square.xpos == xpos + 80 and square.ypos == ypos - 80:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos + 80, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                        for square in grid:
                            if square.xpos == xpos - 80 and square.ypos == ypos - 80:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos - 80, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    if color == 'black':
                        newSquare = None
                        for square in grid:
                            if square.xpos == xpos and square.ypos == ypos + 160:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos, ypos + 160, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)
                    
                        for square in grid:
                            if square.xpos == xpos and square.ypos == ypos + 80:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                        for square in grid:
                            if square.xpos == xpos + 80 and square.ypos == ypos + 80:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos + 80, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                        for square in grid:
                            if square.xpos == xpos - 80 and square.ypos == ypos + 80:
                                newSquare = square
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(xpos - 80, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                elif type(piece) == Knight:
                    newSquare = square_finder(xpos + 80, ypos + 160, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos + 80, ypos + 160, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                    newSquare = square_finder(xpos - 80, ypos + 160, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos - 80, ypos + 160, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                    newSquare = square_finder(xpos - 80, ypos - 160, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos - 80, ypos - 160, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                    newSquare = square_finder(xpos + 80, ypos - 160, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos + 80, ypos - 160, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                    newSquare = square_finder(xpos + 160, ypos + 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos + 160, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                    newSquare = square_finder(xpos - 160, ypos + 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos - 160, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                    newSquare = square_finder(xpos - 160, ypos - 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos - 160, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                    newSquare = square_finder(xpos + 160, ypos - 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos + 160, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                            piece.set(xpos, ypos)

                elif type(piece) == Bishop:
                    squareposx = xpos
                    squareposy = ypos
                    while squareposx > 0 and squareposy > 0:
                        squareposx -= 80
                        squareposy -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx < 640 and squareposy < 640:
                        squareposx += 80
                        squareposy += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx < 640 and squareposy > 0:
                        squareposx += 80
                        squareposy -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx > 0 and squareposy < 640:
                        squareposx -= 80
                        squareposy += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                elif type(piece) == Rook:
                    squareposx = xpos
                    squareposy = ypos
                    while squareposx > 0:
                        squareposx -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx < 640:
                        squareposx += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposy > 0:
                        squareposy -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposy < 640:
                        squareposy += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                elif type(piece) == Queen:
                    squareposx = xpos
                    squareposy = ypos
                    while squareposx > 0 and squareposy > 0:
                        squareposx -= 80
                        squareposy -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx < 640 and squareposy < 640:
                        squareposx += 80
                        squareposy += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx < 640 and squareposy > 0:
                        squareposx += 80
                        squareposy -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx > 0 and squareposy < 640:
                        squareposx -= 80
                        squareposy += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx > 0:
                        squareposx -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposx < 640:
                        squareposx += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposy > 0:
                        squareposy -= 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)

                    squareposx = xpos
                    squareposy = ypos
                    while squareposy < 640:
                        squareposy += 80
                        newSquare = square_finder(squareposx, squareposy, grid)
                        if currentSquare != None and newSquare != None:
                            possible = piece.move(squareposx, squareposy, Color, oppositeColor, currentSquare, newSquare, grid, True)
                        if possible:
                            piece.set(xpos, ypos)
                            return False
                        else:
                            piece.set(xpos, ypos)
                    
                elif type(piece) == King:
                    newSquare = square_finder(xpos + 80, ypos, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos + 80, ypos, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

                    newSquare = square_finder(xpos - 80, ypos, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos - 80, ypos, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

                    newSquare = square_finder(xpos + 80, ypos + 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos + 80, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

                    newSquare = square_finder(xpos - 80, ypos + 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos - 80, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

                    newSquare = square_finder(xpos - 80, ypos - 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos - 80, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

                    newSquare = square_finder(xpos + 80, ypos - 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos + 80, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

                    newSquare = square_finder(xpos, ypos + 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos, ypos + 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

                    newSquare = square_finder(xpos, ypos - 80, grid)
                    if currentSquare != None and newSquare != None:
                        possible = piece.move(xpos, ypos - 80, Color, oppositeColor, currentSquare, newSquare, grid, True)
                    if possible:
                        piece.set(xpos, ypos)
                        return False
                    else:
                        piece.set(xpos, ypos)

            return True    

class whitePlayer(pygame.sprite.RenderUpdates):
    def  __init__(self):
        pygame.sprite.RenderUpdates.__init__(self)

class blackPlayer(pygame.sprite.RenderUpdates):
    def  __init__(self):
        pygame.sprite.RenderUpdates.__init__(self)

class Players(pygame.sprite.RenderUpdates):
    def __init__(self):
        pygame.sprite.RenderUpdates.__init__(self)
    def add_both(self, white, black):
        for piece in white:
            self.add(piece)
        for piece in black:
            self.add(black)

class Square:
    def __init__(self, image, x, y, occupant):
        self.image = image
        self.rect = image.get_rect(center=(x + 40, y + 40))
        self.xpos = x + 40
        self.ypos = y + 40
        self.occupant = occupant

def convert(surface):    
    pygame.display.set_mode()
    image = surface
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            if image.get_at((x, y)) == (0, 0, 0, 255):
                image.set_at((x, y), (255, 255, 255, 0))
    return image

def square_finder(xpos, ypos, grid):
    squareFound = None
    for square in grid:
        if square.xpos == xpos and square.ypos == ypos:
            squareFound = square
            return squareFound
    return squareFound 
    
        

def setBlack():
    black_player = blackPlayer()
    
    black_rookLeft = Rook('blackrook.png', 40, 40, 'black')
    black_player.add(black_rookLeft)
    black_knightLeft = Knight('blackknight.gif', 120, 40, 'black')
    black_player.add(black_knightLeft)
    black_bishopLeft = Bishop('blackbishop.png', 200, 40, 'black')
    black_player.add(black_bishopLeft)
    
    black_queen = Queen('blackqueen.png', 280, 40, 'black')
    black_player.add(black_queen)
    black_king = King('blackking.png', 360, 40, 'black')
    black_player.add(black_king)
    
    black_bishopRight = Bishop('blackbishop.png', 440, 40, 'black')
    black_player.add(black_bishopRight)
    black_knightRight = Knight('blackknight.gif', 520, 40, 'black')
    black_player.add(black_knightRight)
    black_rookRight = Rook('blackrook.png', 600, 40, 'black')
    black_player.add(black_rookRight)

    black_pawn0 = Pawn('blackpawn.jpg', 40, 120, 'black')
    black_player.add(black_pawn0)
    black_pawn1 = Pawn('blackpawn.jpg', 120, 120, 'black')
    black_player.add(black_pawn1)
    black_pawn2 = Pawn('blackpawn.jpg', 200, 120, 'black')
    black_player.add(black_pawn2)
    black_pawn3 = Pawn('blackpawn.jpg', 280, 120, 'black')
    black_player.add(black_pawn3)
    black_pawn4 = Pawn('blackpawn.jpg', 360, 120, 'black')
    black_player.add(black_pawn4)
    black_pawn5 = Pawn('blackpawn.jpg', 440, 120, 'black')
    black_player.add(black_pawn5)
    black_pawn6 = Pawn('blackpawn.jpg', 520, 120, 'black')
    black_player.add(black_pawn6)
    black_pawn7 = Pawn('blackpawn.jpg', 600, 120, 'black')
    black_player.add(black_pawn7)


    return black_player

def setWhite():
    white_player = whitePlayer()

    white_rookLeft = Rook('whiterook.png', 40, 600, 'white')
    white_player.add(white_rookLeft)
    white_knightLeft = Knight('whiteknight.png', 120, 600, 'white')
    white_player.add(white_knightLeft)
    white_bishopLeft = Bishop('whitebishop.png', 200, 600, 'white')
    white_player.add(white_bishopLeft)
    
    white_queen = Queen('whitequeen.jpg', 280, 600, 'white')
    white_player.add(white_queen)
    white_king = King('whiteking.png', 360, 600, 'white')
    white_player.add(white_king)
    
    white_bishopRight = Bishop('whitebishop.png', 440, 600, 'white')
    white_player.add(white_bishopRight)
    white_knightRight = Knight('whiteknight.png', 520, 600, 'white')
    white_player.add(white_knightRight)
    white_rookRight = Rook('whiterook.png', 600, 600, 'white')
    white_player.add(white_rookRight)

    white_pawn0 = Pawn('whitepawn.png', 40, 520, 'white')
    white_player.add(white_pawn0)
    white_pawn1 = Pawn('whitepawn.png', 120, 520, 'white')
    white_player.add(white_pawn1)
    white_pawn2 = Pawn('whitepawn.png', 200, 520, 'white')
    white_player.add(white_pawn2)
    white_pawn3 = Pawn('whitepawn.png', 280, 520, 'white')
    white_player.add(white_pawn3)
    white_pawn4 = Pawn('whitepawn.png', 360, 520, 'white')
    white_player.add(white_pawn4)
    white_pawn5 = Pawn('whitepawn.png', 440, 520, 'white')
    white_player.add(white_pawn5)
    white_pawn6 = Pawn('whitepawn.png', 520, 520, 'white')
    white_player.add(white_pawn6)
    white_pawn7 = Pawn('whitepawn.png', 600, 520, 'white')
    white_player.add(white_pawn7)

    return white_player