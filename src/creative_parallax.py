from DrawingPanel import *

# Juan Torres, CS 115, Winter 2025
# Creative Parallax, 03/04/25
#
# The creative parallax creates multiple shapes and moves 2 of the shapes when the x/y
# positions are changed.

panel = DrawingPanel(700, 700, "lightblue")
prev_x, prev_y = panel.get_mouse_x(), panel.get_mouse_y

while True:
    x,y = panel.get_mouse_x(), panel.get_mouse_y()

    if (x,y) != (prev_x, prev_y):
        panel.fill_rect(25, 25, 650, 650, "black")
        panel.fill_rect(50, 50, 600, 600, "white")
        panel.fill_rect(100, 100, 500, 500, "red")
        panel.fill_rect(150, 150, 400, 400, "yellow")
        panel.fill_rect(200, 200, 300, 300, "black")
        panel.fill_rect(250, 250, 200, 200, "white")
        panel.fill_rect(300 + panel.get_mouse_x() * .05, 300 + panel.get_mouse_y() * .05, 100, 100, "red")
        panel.fill_rect(325 + panel.get_mouse_x() * .15, 325 + panel.get_mouse_y() * .15, 50, 50, "yellow")
        prev_x, prev_y = x,y
    panel.sleep(2)




