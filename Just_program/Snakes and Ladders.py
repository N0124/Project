class SnakesLadders():
    def __init__(self):
        self.players_position = [0, 0]
        self.current = 0
        self.board = {1: 1, 2: 38, 3: 3, 4: 4, 5: 5, 6: 6, 7: 14, 8: 31, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 26, 16: 6, 17: 17, 18: 18, 19: 19, 20: 20, 21: 42, 22: 22, 23: 23, 24: 24, 25: 25, 26: 26, 27: 27, 28: 84, 29: 29, 30: 30, 31: 31, 32: 32, 33: 33, 34: 34, 35: 35, 36: 44, 37: 37, 38: 38, 39: 39, 40: 40, 41: 41, 42: 42, 43: 43, 44: 44, 45: 45, 46: 25, 47: 47, 48: 48, 49: 11, 50: 50, 51: 67, 52: 52, 53: 53, 54: 54, 55: 55, 56: 56, 57: 57, 58: 58, 59: 59, 60: 60, 61: 61, 62: 19, 63: 63, 64: 60, 65: 65, 66: 66, 67: 67, 68: 68, 69: 69, 70: 70, 71: 91, 72: 72, 73: 73, 74: 53, 75: 75, 76: 76, 77: 77, 78: 98, 79: 79, 80: 80, 81: 81, 82: 82, 83: 83, 84: 84, 85: 85, 86: 86, 87: 94, 88: 88, 89: 68, 90: 90, 91: 91, 92: 88, 93: 93, 94: 94, 95: 75, 96: 96, 97: 97, 98: 98, 99: 80, 100: 100}



    def play(self, die1, die2):
        player = self.players_position
        position = self.current

        if 100 in player:
            return "Game over!"

        move = die1 + die2 + player[position]
        if move > 100:
            move = 100 - (100 - player[position]) - (die2 + die1 - 100 - player[position])

        player[position] = self.board[move]

        winner = 1 if position == 0 else 2
        if player[position] == 100:

            return 'Player %s Wins!' % winner

        elif player[position] != 100:
            if die2 != die1:
                self.current = 1 if self.current == 0 else 0
            return "Player %s is on square %s"%(winner, player[position])



game = SnakesLadders()
print (game.play(1,1), game.play(1,5), game.play(6,2),game.players_position)