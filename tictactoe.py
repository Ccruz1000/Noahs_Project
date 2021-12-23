board = [[' ' for _ in range(3)] for _ in range(3)]
# Separate Rows into squares
def draw(list):
    for row in range(len(list)):
        if row % 1 == 0 and row != 0:
            print("- - - - - -")
        # Separate Columns into squares
        for column in range(len(list[0])):
            if column % 1 == 0 and column != 0:
                print(' | ', end='')

            if column == 2:
                print(list[row][column])
            else:
                print(str(list[row][column]) + ' ', end='')
def turn(player):
    positionx = int(input("Select your row\n"))
    positiony = int(input("Select your column\n"))
    if player == 1:
        board[positionx][positiony] = 'x'
    elif player == 2:
        board[positionx][positiony] = 'o'

for i in range(9):
    if i % 2 != 0:
        turn(1)
    elif i% 2 == 0:
        turn(2)
    draw(board)

