from DrawingPanel import *
panel = DrawingPanel(700, 700, "lightblue")

panel.fill_rect(25, 25, 650, 650, "black")
panel.fill_rect(50, 50, 600, 600, "white")
panel.fill_rect(100, 100, 500, 500, "red")
panel.fill_rect(150, 150, 400, 400, "yellow")
panel.fill_rect(200, 200, 300, 300, "black")
panel.fill_rect(250, 250, 200, 200, "white")
panel.fill_rect(300, 300, 100, 100, "red")
panel.fill_rect(325 + panel.get_mouse_x() * .05, 325 + panel.get_mouse_y() * .05, 50, 50, "yellow")





