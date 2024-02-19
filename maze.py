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
        time.sleep(0.0015)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)


    def _break_walls_r(self, i, j):
        cell = self._cells[i][j]
        cell._visited = True

        neighbors = self._get_unvisited_neighbors(i, j)
        while neighbors:
            random_neighbor = random.choice(neighbors)
            ni, nj = random_neighbor
            neighbor_cell = self._cells[ni][nj]
            
            # Break the wall between cell and neighbor_cell
            self._break_wall_between(cell, neighbor_cell)
            
            # Recursively visit the neighbor
            self._break_walls_r(ni, nj)

            # Draw cells
            self._draw_cell(i,j)
            self._draw_cell(ni,nj)            
            
            # Update neighbors for the current cell
            neighbors = self._get_unvisited_neighbors(i, j)

    def _get_unvisited_neighbors(self, i, j):
        neighbors = []
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < self._num_cols and 0 <= nj < self._num_rows:
                neighbor = self._cells[ni][nj]
                if not neighbor._visited:
                    neighbors.append((ni, nj))
        return neighbors
    
    def _break_wall_between(self, cell1, cell2):
        # Determine the relative positions of cell1 and cell2
        if cell1._x1 < cell2._x1:
            # cell2 is to the right of cell1
            cell1.has_right_wall = False
            cell2.has_left_wall = False
        elif cell1._x1 > cell2._x1:
            # cell2 is to the left of cell1
            cell1.has_left_wall = False
            cell2.has_right_wall = False
        elif cell1._y1 < cell2._y1:
            # cell2 is below cell1
            cell1.has_bottom_wall = False
            cell2.has_top_wall = False
        elif cell1._y1 > cell2._y1:
            # cell2 is above cell1
            cell1.has_top_wall = False
            cell2.has_bottom_wall = False
        else:
            # cell1 and cell2 are at the same position, no wall to break
            pass

            

