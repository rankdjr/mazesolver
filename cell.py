from graphics import Line, Point

class Cell:
    """Represents a cell in a maze, including its walls, position, and visitation status.

    Attributes:
        has_left_wall (bool): Indicates if the cell has a left wall.
        has_right_wall (bool): Indicates if the cell has a right wall.
        has_top_wall (bool): Indicates if the cell has a top wall.
        has_bottom_wall (bool): Indicates if the cell has a bottom wall.
        visited (bool): Indicates if the cell has been visited during maze generation or solving.
    """
    def __init__(self, win=None):
        """Initializes a new instance of the Cell class.

        Args:
            win: The window or graphical context where the cell will be drawn. Optional; defaults to None.
        """
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        """Draws the cell and its walls in the specified graphical window.

        Args:
            x1 (float): The x-coordinate of the cell's top-left corner.
            y1 (float): The y-coordinate of the cell's top-left corner.
            x2 (float): The x-coordinate of the cell's bottom-right corner.
            y2 (float): The y-coordinate of the cell's bottom-right corner.
        """
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        left_wall = Line(Point(x1, y1), Point(x1, y2))
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))

        line_color = "black" if self.has_left_wall == True else "white"
        self._win.draw_line(left_wall, line_color)
        
        line_color = "black" if self.has_right_wall == True else "white"
        self._win.draw_line(right_wall, line_color)
        
        line_color = "black" if self.has_top_wall == True else "white"
        self._win.draw_line(top_wall, line_color)
        
        line_color = "black" if self.has_bottom_wall == True else "white"
        self._win.draw_line(bottom_wall, line_color)

    def get_center_coords(self):
        """Calculates and returns the center coordinates of the cell.

        Returns:
            tuple: The (x, y) coordinates of the cell's center.
        """
        mid_x = (self._x1 + self._x2) / 2
        mid_y = (self._y1 + self._y2) / 2
        return mid_x, mid_y

    def draw_move(self, to_cell, undo=False):
        """Draws a line representing a move from this cell to another cell.

        Args:
            to_cell (Cell): The cell to move to.
            undo (bool): If True, the move is being undone (e.g., for backtracking). Optional; defaults to False.
        """
        if self._win is None:
            return
        
        fill_color = "gray" if undo == True else "red"
        
        self_x_mid, self_y_mid = self.get_center_coords()
        end_x_mid, end_y_mid = to_cell.get_center_coords()
        
        # Moves will be rendered in half steps
        # Moving Left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, self_y_mid), Point(self_x_mid, self_y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(end_x_mid, end_y_mid), Point(to_cell._x2, end_y_mid))
            self._win.draw_line(line, fill_color)

        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(self_x_mid, self_y_mid), Point(self._x2, self_y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, end_y_mid), Point(end_x_mid, end_y_mid))
            self._win.draw_line(line, fill_color)

        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(self_x_mid, self_y_mid), Point(self_x_mid, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(end_x_mid, to_cell._y2), Point(end_x_mid, end_y_mid))
            self._win.draw_line(line, fill_color)

        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(self_x_mid, self_y_mid), Point(self_x_mid, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(end_x_mid, end_y_mid), Point(end_x_mid, to_cell._y1))
            self._win.draw_line(line, fill_color)
        
        
        