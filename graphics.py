from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        super().__init__()
        self.__root = Tk()
        self.__root.title('Maze Solver')
        self.__root.geometry(f'{width}x{height}')
        self.__root.minsize(width, height)
        self.canvas = Canvas(self.__root)
        self.canvas.pack()
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        # self.root.mainloop()
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while(self.is_running):
            self.redraw()
        
    def close(self):
        self.is_running = False