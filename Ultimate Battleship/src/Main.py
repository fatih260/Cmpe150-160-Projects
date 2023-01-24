
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    taslak_list = [[['-' for i in range(10)] for j in range(10)], [['-' for l in range(10)] for m in range(10)]]
    # player 1 deploy ships
    confirm = False
    coordinates_occupied = []
    while confirm == False:
        my_big_list1 = [[['-' for i in range(10)] for j in range(10)], [['-' for l in range(10)] for m in range(10)]]
        print_3d_list(my_big_list1)
        # player 1 deploy ships
        used_ships = []
        title_used_list = []

        case = 0
        while case < 5:
            flag = True
            case += 1
            print_ships_to_be_placed()
            list_ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
            low_list_ships = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
            displayed_list_ships = [chara for chara in list_ships if chara not in title_used_list]
            residual_list_ships = [char for char in low_list_ships if char not in used_ships]
            for j in displayed_list_ships:
                print_single_element(j)
            print_empty_line()
            print_player_turn_to_place(1)
            print_to_place_ships()
            my_str = input()
            my_list = my_str.split()
            if len(my_list) < 4:
                print_incorrect_input_format()
                case -= 1
                flag = False
                print_3d_list(my_big_list1)
            else:
                name = my_list[0]

                coordinate_x = my_list[1]
                coordinate_y = my_list[2]
                if flag == True:
                    try:
                        coordinate_x = int(coordinate_x)
                        coordinate_y = int(coordinate_y)
                    except:
                        print_incorrect_input_format()
                        case -= 1
                        flag = False
                if flag == True:
                    if (int(coordinate_x) not in [z for z in range(1, 11)]) or (
                            int(coordinate_y) not in [z for z in range(1, 11)]):
                        print_incorrect_coordinates()
                        case -= 1
                        flag = False

                if name.lower() in residual_list_ships:
                    if name.lower() == low_list_ships[0]:
                        length = 5
                    elif name.lower() == low_list_ships[1]:
                        length = 4
                    elif name.lower() == low_list_ships[2] or name.lower() == low_list_ships[3]:
                        length = 3
                    else:
                        length = 2

                elif name.lower() in used_ships:
                    if flag == True:
                        print_ship_is_already_placed(name.title())
                        case -= 1
                        flag = False

                else:
                    length = 0
                    if flag == True:
                        print_incorrect_ship_name()
                        case -= 1
                        flag = False

                orientation = my_list[3]
                if orientation not in ['h', 'v'] and flag == True:
                    print_incorrect_orientation()
                    case -= 1
                    flag = False

                if flag == True:
                    if orientation == 'h' and coordinate_x <= 10 and int(coordinate_x) + length > 11:
                        print_ship_cannot_be_placed_outside(name.title())
                        case -= 1
                        flag = False
                if flag == True:
                    if orientation == 'v' and coordinate_y <= 10 and int(coordinate_y) + length > 11:
                        print_ship_cannot_be_placed_outside(name.title())
                        case -= 1
                        flag = False

                # checking if the new ship coincides with an already placed ship
                if flag == True and orientation == 'h':
                    new_ship_list = [(coordinate_x + inc, coordinate_y) for inc in range(length)]
                    flag1 = True
                    for ea in new_ship_list:
                        if ea in coordinates_occupied:
                            flag1 = False
                            break
                        else:
                            flag1 = True

                    if flag1 == False:
                        print_ship_cannot_be_placed_occupied(name.title())
                        case -= 1
                        flag = False
                if flag == True and orientation == 'v':
                    new_ship_list = [(coordinate_x, coordinate_y + inc) for inc in range(length)]
                    flag1 = True
                    for ea in new_ship_list:
                        if ea in coordinates_occupied:
                            flag1 = False
                            break
                        else:
                            flag1 = True

                    if flag1 == False:
                        print_ship_cannot_be_placed_occupied(name.title())
                        case -= 1
                        flag = False

                if orientation == 'h' and flag == True and length > 1:
                    for i in range(length):
                        my_big_list1[0][int(coordinate_y) - 1][int(coordinate_x) - 1 + i] = '#'
                        used_ships.append(name.lower())
                        title_used_list = [elem.title() for elem in used_ships]
                    for l in range(length):
                        coordinates_occupied.append((coordinate_x + l, coordinate_y))

                if orientation == 'v' and flag == True and length > 1:
                    for i in range(length):
                        my_big_list1[0][(int(coordinate_y) - 1 + i)][int(coordinate_x) - 1] = '#'
                        used_ships.append(name.lower())
                        title_used_list = [elem.title() for elem in used_ships]
                    for l in range(length):
                        coordinates_occupied.append((coordinate_x, coordinate_y + l))
                print_3d_list(my_big_list1)
        biflag = None
        while biflag == True or biflag == None:
            print_confirm_placement()
            confirmation = input()
            if confirmation == 'N' or confirmation == 'n':
                biflag = False
                coordinates_occupied = []
                confirm = False

            elif confirmation == 'Y' or confirmation == 'y':
                biflag = False
                confirm = True
            else:

                biflag = True



    #Second player to deploy ships
    confirm2 = False
    coordinates_occupied2 = []
    while confirm2 == False:
        my_big_list2 = [[['-' for i in range(10)] for j in range(10)], [['-' for l in range(10)] for m in range(10)]]
        print_3d_list(my_big_list2)
        used_ships2 = []
        title_used_list2 = []

        case = 0
        while case < 5:
            flag = True
            case += 1
            print_ships_to_be_placed()
            list_ships2 = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
            low_list_ships2 = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
            displayed_list_ships2 = [chara for chara in list_ships2 if chara not in title_used_list2]
            residual_list_ships2 = [char for char in low_list_ships2 if char not in used_ships2]
            for j in displayed_list_ships2:
                print_single_element(j)
            print_empty_line()
            print_player_turn_to_place(2)
            print_to_place_ships()
            my_str = input()
            my_list = my_str.split()
            if len(my_list) < 4:
                print_incorrect_input_format()
                case -= 1
                flag = False
                print_3d_list(my_big_list2)
            else:
                name = my_list[0]

                coordinate_x = my_list[1]
                coordinate_y = my_list[2]
                if flag == True:
                    try:
                        coordinate_x = int(coordinate_x)
                        coordinate_y = int(coordinate_y)
                    except:
                        print_incorrect_input_format()
                        case -= 1
                        flag = False
                if flag == True:
                    if (int(coordinate_x) not in [z for z in range(1, 11)]) or (
                            int(coordinate_y) not in [z for z in range(1, 11)]):
                        print_incorrect_coordinates()
                        case -= 1
                        flag = False

                if name.lower() in residual_list_ships2:
                    if name.lower() == low_list_ships2[0]:
                        length = 5
                    elif name.lower() == low_list_ships2[1]:
                        length = 4
                    elif name.lower() == low_list_ships2[2] or name.lower() == low_list_ships2[3]:
                        length = 3
                    else:
                        length = 2

                elif name.lower() in used_ships2:
                    if flag == True:
                        print_ship_is_already_placed(name.title())
                        case -= 1
                        flag = False

                else:
                    length = 0
                    if flag == True:
                        print_incorrect_ship_name()
                        case -= 1
                        flag = False

                orientation = my_list[3]
                if orientation not in ['h', 'v'] and flag == True:
                    print_incorrect_orientation()
                    case -= 1
                    flag = False

                if flag == True:
                    if orientation == 'h' and coordinate_x <= 10 and int(coordinate_x) + length > 11:
                        print_ship_cannot_be_placed_outside(name.title())
                        case -= 1
                        flag = False
                if flag == True:
                    if orientation == 'v' and coordinate_y <= 10 and int(coordinate_y) + length > 11:
                        print_ship_cannot_be_placed_outside(name.title())
                        case -= 1
                        flag = False

                # checking if the new ship coincides with an already placed ship
                if flag == True and orientation == 'h':
                    new_ship_list = [(coordinate_x + inc, coordinate_y) for inc in range(length)]
                    flag1 = True
                    for ea in new_ship_list:
                        if ea in coordinates_occupied2:
                            flag1 = False
                            break
                        else:
                            flag1 = True

                    if flag1 == False:
                        print_ship_cannot_be_placed_occupied(name.title())
                        case -= 1
                        flag = False
                if flag == True and orientation == 'v':
                    new_ship_list = [(coordinate_x, coordinate_y + inc) for inc in range(length)]
                    flag1 = True
                    for ea in new_ship_list:
                        if ea in coordinates_occupied2:
                            flag1 = False
                            break
                        else:
                            flag1 = True

                    if flag1 == False:
                        print_ship_cannot_be_placed_occupied(name.title())
                        case -= 1
                        flag = False

                if orientation == 'h' and flag == True and length > 1:
                    for i in range(length):
                        my_big_list2[1][int(coordinate_y) - 1][int(coordinate_x) - 1 + i] = '#'
                        used_ships2.append(name.lower())
                        title_used_list2 = [elem.title() for elem in used_ships2]
                    for l in range(length):
                        coordinates_occupied2.append((coordinate_x + l, coordinate_y))

                if orientation == 'v' and flag == True and length > 1:
                    for i in range(length):
                        my_big_list2[1][(int(coordinate_y) - 1 + i)][int(coordinate_x) - 1] = '#'
                        used_ships2.append(name.lower())
                        title_used_list2 = [elem.title() for elem in used_ships2]
                    for l in range(length):
                        coordinates_occupied2.append((coordinate_x, coordinate_y + l))
                print_3d_list(my_big_list2)
        biflag2 = None
        while biflag2 == True or biflag2 == None:
            print_confirm_placement()
            confirmation = input()
            if confirmation == 'N' or confirmation == 'n':
                biflag2 = False
                coordinates_occupied = []
                confirm2 = False
            elif confirmation == 'Y' or confirmation == 'y':
                biflag2 = False
                confirm2 = True
            else:

                biflag2 = True

    #battlephasebegin

    yeni_list1 = [['-' for k in range(10)] for jj in range(10)]
    yeni_list2 = [['-' for k in range(10)] for jj in range(10)]

    devamedicem1 = False
    devamedicem2 = False
    bitmedi = True
    sonflag = True
    coordinates_struck1 = set()
    coordinates_struck2 = set()

    while bitmedi == True:

        vurus = True

        while vurus == True:

            print_3d_list([my_big_list1[0], yeni_list1])
            print_player_turn_to_strike(1)
            print_choose_target_coordinates()
            try:
                coordinate_by_x, coordinate_by_y = input().split()
                coordinate_by_x = int(coordinate_by_x)
                coordinate_by_y = int(coordinate_by_y)
            except:
                print_incorrect_input_format()
                continue

            if coordinate_by_x<0 or coordinate_by_x>11 or coordinate_by_y<0 or coordinate_by_y>11:
                print_incorrect_coordinates()
                continue


            if (coordinate_by_x, coordinate_by_y) in coordinates_struck1:
                print_tile_already_struck()

            else:
                coordinates_struck1.add((coordinate_by_x, coordinate_by_y))
                if (coordinate_by_x, coordinate_by_y) not in coordinates_occupied2:
                    print_miss()
                    my_big_list2[1][coordinate_by_y - 1][coordinate_by_x - 1] = 'O'
                    yeni_list1[coordinate_by_y - 1][coordinate_by_x - 1] = 'O'
                    vurus = False
                    devamedicem1 = False
                else:
                    devamedicem1 = True
                    coordinates_occupied2.remove((coordinate_by_x, coordinate_by_y))
                    print_hit()
                    my_big_list2[1][coordinate_by_y - 1][coordinate_by_x - 1] = '!'
                    yeni_list1[coordinate_by_y - 1][coordinate_by_x - 1] = '!'
                    vurus = True
                    if coordinates_occupied2 == []:
                        print_3d_list([my_big_list1[0], yeni_list1])
                        print_player_won(1)
                        print_thanks_for_playing()
                        bitmedi = False
                        sonflag = False

                        break
                flagdone = True
                while flagdone == True and bitmedi == True and devamedicem1 == False:
                    print_type_done_to_yield(2)
                    passing = input().lower()
                    if passing == 'done':
                        flagdone = False

                    else:
                        flagdone = True

        vurus2 = True
        while vurus2 == True and sonflag == True:
            print_3d_list([yeni_list2, my_big_list2[1]])
            print_player_turn_to_strike(2)
            print_choose_target_coordinates()
            try:
                coordinate_by_x2, coordinate_by_y2 = input().split()
                coordinate_by_x2 = int(coordinate_by_x2)
                coordinate_by_y2 = int(coordinate_by_y2)
            except:
                print_incorrect_input_format()
                continue

            if coordinate_by_x2<0 or coordinate_by_x2>11 or coordinate_by_y2<0 or coordinate_by_y2>11:
                print_incorrect_coordinates()
                continue

            if (coordinate_by_x2, coordinate_by_y2) in coordinates_struck2:
                print_tile_already_struck()

            else:
                coordinates_struck2.add((coordinate_by_x2, coordinate_by_y2))
                if (coordinate_by_x2, coordinate_by_y2) not in coordinates_occupied:
                    print_miss()
                    my_big_list1[0][coordinate_by_y2 - 1][coordinate_by_x2 - 1] = 'O'
                    yeni_list2[coordinate_by_y2 - 1][coordinate_by_x2 - 1] = 'O'
                    vurus2 = False
                    devamedicem2 = False
                else:
                    coordinates_occupied.remove((coordinate_by_x2, coordinate_by_y2))
                    print_hit()
                    my_big_list1[0][coordinate_by_y2 - 1][coordinate_by_x2 - 1] = '!'
                    yeni_list2[coordinate_by_y2 - 1][coordinate_by_x2 - 1] = '!'
                    vurus2 = True
                    devamedicem2 = True
                    if coordinates_occupied == []:
                        print_3d_list([yeni_list2, my_big_list2[1]])
                        print_player_won(2)
                        print_thanks_for_playing()
                        bitmedi = False

                        break
                flagdone2 = True
                while flagdone2 == True and bitmedi == True and devamedicem2 == False:
                    print_type_done_to_yield(1)
                    passing2 = input().lower()
                    if passing2 == 'done':
                        flagdone2 = False

                    else:
                        flagdone2 = True


    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()

