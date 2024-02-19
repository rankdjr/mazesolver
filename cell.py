from graphics import Line, Point

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "black")

    def get_center_coords(self):
        mid_x = (self._x1 + self._x2) / 2
        mid_y = (self._y1 + self._y2) / 2
        return mid_x, mid_y

    def draw_move(self, to_cell, undo=False):
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
        
        
        