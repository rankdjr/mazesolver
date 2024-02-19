from tkinter import Tk, BOTH, Canvas

class Window:
    """
    Represents a window for drawing graphics.

    Attributes:
        __root (Tk): The Tkinter root window.
        __canvas (Canvas): The canvas for drawing.
        __is_running (bool): Flag indicating if the window is running.
    """

    def __init__(self, width, height):
        """
        Initializes the Window object with the given width and height.

        Args:
            width (int): The width of the window.
            height (int): The height of the window.
        """
        self.__root = Tk()
        self.__root.title('Maze Master')
        self.__root.protocol("WM_DELETE_WINDOW", self.__close_window)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False

    
    def __close_window(self):
        """
        Closes the window.
        """
        self.__is_running = False
        self.__root.destroy()


    def redraw(self):
        """
        Redraws the window.
        """
        self.__root.update_idletasks()
        self.__root.update()


    def run(self):
        """
        Runs the window main loop.
        """
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("Window closed...")
    

    def draw_line(self, line, fill_color="black"):
        """
        Draws a line on the canvas.

        Args:
            line (Line): The Line object to draw.
            fill_color (str): The color of the line. Default is "black".
        """
        line.draw(self.__canvas, fill_color)


class Point:
    """
    Represents a point in 2D space.
    """

    def __init__(self, x, y):
        """
        Initializes the Point object with the given coordinates.

        Args:
            x (int): The x-coordinate of the point.
            y (int): The y-coordinate of the point.
        """
        self._x = x
        self._y = y


class Line:
    """
    Represents a line segment between two points.
    """

    def __init__(self, p1, p2):
        """
        Initializes the Line object with the given start and end points.

        Args:
            p1 (Point): The start point of the line.
            p2 (Point): The end point of the line.
        """
        self._p1 = p1
        self._p2 = p2


    def draw(self, canvas, fill_color):
        """
        Draws the line on the canvas.

        Args:
            canvas (Canvas): The canvas to draw on.
            fill_color (str): The color of the line.
        """
        canvas.create_line(
            self._p1._x, self._p1._y, self._p2._x, self._p2._y, fill=fill_color, width=2
        )
    