from Rocket import RocketBoard, Rocket


# Thanks to static method we do not have to use the board 
rocket1 = Rocket(altitude = 5)
rocket2 = Rocket()
print(RocketBoard.get_distance(rocket1,rocket2))




'''
board = RocketBoard(3)
print(board.get_distance(board[0],board[1]))
board[0] = 60
print(board[0])
'''


