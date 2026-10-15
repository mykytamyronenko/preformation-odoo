import random

def create_grid(rows, cols, value):
    grid = []

    for i in range(rows):
        row = [value] * cols
        grid.append(row)

    return grid



def get_neighbors(rows, cols, r, c):
    neighbors = []

    for delta_r in [-1, 0, 1]:
        for delta_c in [-1, 0, 1]:
            new_r = r + delta_r
            new_c = c + delta_c

            if (new_r, new_c) != (r, c):
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    neighbors.append((new_r, new_c))

    return neighbors



def generate_mines(rows, cols, nb_mines, forbidden_cell):
    mines = []

    while len(mines) < nb_mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)

        if (r, c) != forbidden_cell and (r, c) not in mines:
            mines.append((r, c))

    return mines



def create_hidden_grid(rows, cols, mines):
    hidden = create_grid(rows, cols, 0)

    for r, c in mines:
        hidden[r][c] = "*"

    for r in range(rows):
        for c in range(cols):
            if hidden[r][c] != "*":
                count = 0

                for nr, nc in get_neighbors(rows, cols, r, c):
                    if hidden[nr][nc] == "*":
                        count += 1

                hidden[r][c] = count

    return hidden




def reveal(hidden, visible, r, c):
    if visible[r][c] != "?":
        return

    visible[r][c] = hidden[r][c]

    if hidden[r][c] != 0:
        return

    for new_r, new_c in get_neighbors(len(hidden), len(hidden[0]), r, c):
        reveal(hidden, visible, new_r, new_c)



def print_grid(grid):
    nb_col = -1
    nb_row = 0
    for i in range (len(grid)+1):
        nb_col += 1
        print(nb_col, end= '   ')

    print()
    
    for row in grid:
        nb_row += 1
        print(nb_row, *row, sep= '   ')



def has_won(hidden, visible):
    pass


def minesweeper(rows, cols, nb_mines):
    visible = create_grid(rows,cols,'?')
    
    print_grid(visible)

    player_command = input("Appuyer sur un 'o' -> ligne -> colonne, pour ouvrir une case\n"
                           "Appuyer sur un 'f' -> ligne -> colonne, pour poser ou retirer un dreapeau\n")

    r = int(input("ligne : "))
    c = int(input("colonne : "))

    if player_command == "o":
        forbidden_cell = (r-1, c-1)

    mines = generate_mines(rows, cols, nb_mines, forbidden_cell)

    hidden = create_hidden_grid(rows, cols, mines)

    reveal(hidden, visible, r, c)
    print_grid(visible)

minesweeper(5, 5, 5)




# def minesweeper(rows, cols, nb_mines):
#     hidden = None
#     visible = create_grid(rows, cols, "?")
#     flags = create_grid(rows, cols, False)

#     print_grid(visible)

#     first_move = True

#     while True:
#         player_command = input(
#             "Commande (o ligne colonne / f ligne colonne / q) : "
#         ).split()

#         if player_command[0] == "q":
#             print("Partie quittée.")
#             break

#         if len(player_command) != 3:
#             print("Commande invalide.")
#             continue

#         action = player_command[0]

#         try:
#             r = int(player_command[1]) - 1
#             c = int(player_command[2]) - 1
#         except ValueError:
#             print("Les coordonnées doivent être des nombres.")
#             continue

#         if not (0 <= r < rows and 0 <= c < cols):
#             print("Coordonnées hors de la grille.")
#             continue

#         if action == "f":
#             if visible[r][c] != "?":
#                 print("Cette case est déjà révélée.")
#                 continue

#             flags[r][c] = not flags[r][c]

#         elif action == "o":
#             if flags[r][c]:
#                 print("Retire d'abord le drapeau.")
#                 continue

#             if first_move:
#                 mines = generate_mines(rows, cols, nb_mines, (r, c))
#                 hidden = create_hidden_grid(rows, cols, mines)
#                 first_move = False

#             if hidden[r][c] == "*":
#                 visible[r][c] = "*"
#                 print_grid(visible)
#                 print("Perdu ! Tu as trouvé une mine.")
#                 break

#             reveal(hidden, visible, r, c)

#         else:
#             print("Commande inconnue.")
#             continue

#         # Affichage temporaire des drapeaux
#         display = create_grid(rows, cols, "?")

#         for i in range(rows):
#             for j in range(cols):
#                 if flags[i][j]:
#                     display[i][j] = "F"
#                 elif visible[i][j] != "?":
#                     display[i][j] = visible[i][j]

#         print_grid(display)

#         if hidden is not None and has_won(hidden, visible):
#             print("Bravo, tu as gagné !")
#             break

# minesweeper(5, 5, 5)