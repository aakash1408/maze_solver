from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        #create a new root directory 
        self.root = Tk()

        #set the title property of the root widget
        self.root.title("Maze Solver")

        # Create a Canvas and save it as a data member
        self.canvas = Canvas(self.root, width = self.width, height = self.height)

        #pack the canvas so it is ready to be drawn
        self.canvas.pack()

        # Create a data member to represent that the window is "running", and set it to False
        self.is_running = False 

        self.root.protocol("WM_DELETE_WINDOW", self.close)

    #create a redraw method as tkinter is not a reactive framework like react or vue
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

    def close(self):
        self.is_running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color = "black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill = fill_color, width = 2)
        canvas.pack()

        