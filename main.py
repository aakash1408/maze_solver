# from visuals import Window, Line, Point
# from cell import Cell

# def main():
#     win = Window(800, 600)
#     # l = Line(Point(50,50), Point(400,400))
#     # win.draw_line(l, "black")
    
#     #cells
#     c = Cell(win)
#     c.has_left_wall = False
#     c.draw(50, 50, 100, 100)

#     c = Cell(win)
#     c.has_right_wall = False
#     c.draw(125, 125, 200, 200)

#     c = Cell(win)
#     c.has_bottom_wall = False
#     c.draw(225, 225, 250, 250)

#     c = Cell(win)
#     c.has_top_wall = False
#     c.draw(300, 300, 500, 500)
#     win.wait_for_close()

# main()

from visuals import Window
from maze import Maze


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    print("Maze Created")
    can_solve = maze.solve()
    if can_solve:
        print("Maze has been solved ..")
    else:
        print("Sorry maze cannot be solved")

    win.wait_for_close()


main()