class Cell:
    """Class for creating a cell object."""
    def __init__(self, mine: bool, around_mines=0):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

    def __str__(self):
        symbol = '*' if self.mine else ' '
        return symbol if self.fl_open else '#'

    def __repr__(self):
        return '*' if self.mine else ' '





