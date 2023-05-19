from algorithms import minimax, minimax_alphabeta
from board import Board
import time
import tkinter as tk


# GAME LINK
# http://kevinshannon.com/connect4/


def main(algorithm, difficulty):
    board = Board()

    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        print(game_board)
        board.print_grid(game_board)

        # 0 is minimax , 1 is alpha beta
        if algorithm == 0:
            # 0 is depth 1 , 1 is depth 3 , 2 is depth 5
            if difficulty == 0:
                column, val = minimax(game_board, 1, 1)
            elif difficulty == 1:
                column, val = minimax(game_board, 1, 3)
            else:
                column, val = minimax(game_board, 1, 5)
        else:
            # 0 is depth 2 , 1 is depth 4 , 2 is depth 6
            if difficulty == 0:
                column, val = minimax_alphabeta(game_board, 1, -10000000000000, 10000000000000, 2)
            elif difficulty == 1:
                column, val = minimax_alphabeta(game_board, 1, -10000000000000, 10000000000000, 4)
            else:
                column, val = minimax_alphabeta(game_board, 1, -10000000000000, 10000000000000, 8)

        board.select_column(column)

        time.sleep(4)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Connect 4")
    root.geometry("450x450")
    # connect 4 label
    tk.Label(root, text='Connect 4', font=('Arial', 25), fg='#039dfc').pack(anchor='w', padx=10, pady=5)

    # algorithm label
    tk.Label(root, text='Algorithms', font=('Arial', 18), ).pack(anchor='w', padx=10, pady=5)

    # variables
    algo = tk.IntVar(None, 0)
    diff = tk.IntVar(None, 0)

    # algorithms radio buttons
    tk.Radiobutton(root, text="Minimax algorithm", font=('Arial', 15), variable=algo, value=0).pack(anchor='w', padx=20,
                                                                                                    pady=5)
    tk.Radiobutton(root, text="Minimax algorithm with alpha beta pruning", font=('Arial', 15), variable=algo,
                   value=1).pack(anchor='w', padx=20, pady=5)

    # difficulty label
    tk.Label(root, text='Difficulty', font=('Arial', 18), ).pack(anchor='w', padx=10, pady=5)

    # difficulty radio buttons
    tk.Radiobutton(root, text="Easy", font=('Arial', 15), variable=diff, value=0).pack(
        anchor='w', padx=20, pady=5)
    tk.Radiobutton(root, text="Medium", font=('Arial', 15), variable=diff,
                   value=1).pack(anchor='w', padx=20, pady=5)
    tk.Radiobutton(root, text="Hard", font=('Arial', 15), variable=diff,
                   value=2).pack(anchor='w', padx=20, pady=5)

    # play button
    tk.Button(root, text="Start", font=('Arial', 16), bg='#039dfc', fg='white', borderwidth=0,
              activebackground='white', activeforeground='#039dfc',
              command=lambda: main(algo.get(), diff.get())).pack(anchor='e', padx=15, pady=5)

    root.mainloop()
