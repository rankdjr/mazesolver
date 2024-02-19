from graphics import Window, Line, Point
from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y= cell_size_y
        self._win = win
        self._cells = []
        if seed is not None:
            self._seed = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            cell_col_list = []
            for j in range(self._num_rows):
                cell_col_list.append(Cell(self._win))
            self._cells.append(cell_col_list)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        
        x1 = self._x1 + self._cell_size_x*i
        y1 = self._y1 + self._cell_size_y*j
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()      

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)
            
    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            unvisited_index_list = []

            # Find neighboring cells which have not been visited
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                unvisited_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                unvisited_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                unvisited_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                unvisited_index_list.append((i, j + 1))

            # if there is no unvisited neighbors, break from loop
            if len(unvisited_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(unvisited_index_list))
            next_index = unvisited_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True

        # check if at end cell
        if i == self._num_cols - 1 and j == self._num_rows -1:
            return True
        
        # check directions for valid cells
        # left
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall:
            to_cell = self._cells[i - 1][j]
            current_cell.draw_move(to_cell)
            if self._solve_r(i - 1, j) == True:
                return True
            else:
                current_cell.draw_move(to_cell, undo=True)


        # right
        if i < self._num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_right_wall:
            to_cell = self._cells[i + 1][j]
            current_cell.draw_move(to_cell)
            if self._solve_r(i + 1, j) == True:
                return True
            else:
                current_cell.draw_move(to_cell, undo=True)
        # up
        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top_wall:
            to_cell = self._cells[i][j - 1]
            current_cell.draw_move(to_cell)
            if self._solve_r(i, j - 1) == True:
                return True
            else:
                current_cell.draw_move(to_cell, undo=True)
        # down
        if j < self._num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom_wall:
            to_cell = self._cells[i][j + 1]
            current_cell.draw_move(to_cell)
            if self._solve_r(i, j + 1) == True:
                return True
            else:
                current_cell.draw_move(to_cell, undo=True)

        return False

            

