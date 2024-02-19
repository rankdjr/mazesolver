from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800,600)
    c1 = Cell(win)
    c2 = Cell(win)
    c3 = Cell(win)
    c4 = Cell(win)


    c1.has_top_wall = False
    c1.has_bottom_wall = False
    c2.has_top_wall = False
    c2.has_bottom_wall = False
    c3.has_top_wall = False
    c3.has_right_wall = False
    c4.has_left_wall = False
    c3.has_right_wall = False
    
    
    c1.draw(10,10,60,60)
    c2.draw(10,60,60,110)
    c3.draw(10,110,60,160)
    c4.draw(60,110,110,160)

    win.wait_for_close()


main()