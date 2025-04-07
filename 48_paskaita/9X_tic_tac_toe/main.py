class SmallBoard:
    def __init__(self):
        self.cells = [' ' for _ in range(9)]
        self.winner = None

    def make_move(self, index, player):
        if self.cells[index] == ' ':
            self.cells[index] = player
            self.check_winner(player)
            return True
        return False

    def check_winner(self, player):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in win_combinations:
            if all(self.cells[i] == player for i in combo):
                self.winner = player
                return
        if_full = self.is_full()
        if if_full:
            self.winner = 'D'

    def is_full(self):
        return all(cell != ' ' for cell in self.cells)

    def is_active(self):
        return self.winner is None


class UltimateTicTacToe:
    def __init__(self):
        self.boards = [SmallBoard() for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
        self.active_board = None

    def display(self):
        print()
        for big_row in range(3):
            for small_row in range(3):
                row = []
                for big_col in range(3):
                    board_index = big_row * 3 + big_col
                    board = self.boards[board_index]
                    row_cells = board.cells[small_row*3:(small_row+1)*3]
                    row.append(" | ".join(row_cells))
                print(" || ".join(row))
            if big_row < 2:
                print("="*35)
        print()

    def check_overall_winner(self):
        winners = [b.winner if b.winner in ['X', 'O'] else ' ' for b in self.boards]
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in win_combinations:
            line = [winners[i] for i in combo]
            if line[0] != ' ' and all(w == line[0] for w in line):
                self.winner = line[0]
                return


    def make_move(self, board_index, cell_index):
        if board_index < 0 or board_index >= 9 or cell_index < 0 or cell_index >= 9:
            print('Netinkama lenta arba langelio numeris')
            return False

        board = self.boards[board_index]
        is_active = board.is_active()
        if not is_active:
            print('Si lenta jau baigta')
            return False

        board_move = board.make_move(cell_index, self.current_player)
        if not board_move:
            print('Sis langelis jau uzimtas')
            return False

        self.check_overall_winner()
        self.active_board = cell_index if self.boards[cell_index].is_active() else None
        self.current_player = 'O' if self.current_player == 'X' else 'X'


    def is_draw(self):
        return all(board.winner is not None for board in self.boards) and self.winner is None

    def play(self):
        while self.winner is None and not self.is_draw():
            self.display()
            print(f'Zaidejas {self.current_player} turi ejima.')
            if self.active_board is not None:
                print(f'Privalai zaisti lentoje #{self.active_board + 1}')
            else:
                print('Gali pasirinkti bet kuria aktyvia lenta.')

            try:
                if self.active_board is not None:
                    board_index = self.active_board
                else:
                    board_index = int(input('Ivesk mazos lentos numeri (1-9): ')) - 1
                cell_index = int(input('Ivesk langelio numeri (1-9): ')) - 1
            except ValueError:
                print('Ivestis turi buti skaiciai')
                continue

            move = self.make_move(board_index, cell_index)
            if not move:
                continue

        self.display()
        if self.winner:
            print(f'Zaidejas {self.winner} laimejo visa zaidima!')
        else:
            print('Zaidimas baigesi lygiosiomis')

game = UltimateTicTacToe()
game.play()
