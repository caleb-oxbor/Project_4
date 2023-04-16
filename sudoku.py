# project 4 skeleton

class SudokuGenerator:
    row_length = 9

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells

    def get_board(self):
        rows, cols = (9, 9)
        [[0 for i in range[rows]]for j in range[cols]]
        return

    def print_board(self):
        print(SudokuGenerator.get_board())
        return

    def valid_in_row(self, row, num):
        if num in row:
            return True
        else:
            return False

    def valid_in_col(self, col, num):
        if num in col:
            return True
        else:
            return False

    def valid_in_box(self, row_start, col_start, num):
        if num in range[row_start, row_start + 3]:
            return True
        elif num in range[col_start, col_start + 3]:
            return True
        else:
            return False

    def is_valid(self, row, col, num):
        for i in row:
            if num in row[i] == 0:
                return True
        for j in col:
            if num in col[j] == 0:
                return True
        else:
            return False

    def fill_box(self, row_start, col_start):
        pass

    def fill_diagonal(self):
        pass

    def fill_remaining(self, row, col):
        pass

    def fill_values(self):
        pass

    def remove_cells(self):
        pass


def generate_sudoku(size, removed):
    pass


class Cell:
    def __init__(self, value, row, col, screen):
        pass

    def set_cell_value(self, value):
        pass

    def set_sketched_value(self, value):
        pass

    def draw(self):
        pass


class Board:
    def __init__(self, width, height, screen, difficulty):
        pass

    def draw(self):
        pass

    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass

def main():
    pass

if __name__ == 'main':
    main()