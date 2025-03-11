from cell import Cell
import random

DIRECTIONS = [
            [1, 0], [-1, 0],
            [0, 1], [0, -1],
            [1, 1], [-1, -1],
            [-1, 1], [1, -1]
        ]


class GamePole:
    """Pole class."""
    def __init__(self, n, m):
        self.size = n
        self.mines = m
        self._pole = self._create_pole()

    def show(self):
        """Show pole in the console."""
        for i in self._pole:
            for c in i:
                print(c, end=' ')
            print('')

    def _get_mine_coordinates(self):
        """Get random coordinates for m mines."""
        set_mine_cords = set()
        while self.mines != len(set_mine_cords):
            i = random.randint(0, self.size - 1)
            j = random.randint(0, self.size - 1)
            set_mine_cords.add((i, j))
        return set_mine_cords

    def _count_around_mines(self, cords, x, y):
        """Count number of mines in 3x3 area from poit coordinates."""
        around_mines = 0
        for dx, dy in DIRECTIONS:
            i, j = x + dx, y + dy
            if i in range(self.size) and j in range(self.size) and (i, j) in cords:
                around_mines += 1
        return around_mines

    def _create_pole(self):
        """Creating pole nxn with Cell objects"""
        pole = []
        mine_cor = self._get_mine_coordinates()
        for x in range(0, self.size):
            pole.append([None]*self.size)
            for y in range(0, self.size):
                mine = True if (x, y) in mine_cor else False
                around_mines = self._count_around_mines(mine_cor, x, y)
                pole[x][y] = Cell(mine=mine, around_mines=around_mines)
        return pole

