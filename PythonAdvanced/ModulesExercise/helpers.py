from canvas import tk

def clear_screen():
    for el in tk.grid_slaves():
        el.destroy()