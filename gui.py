from tkinter import *

# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)


# initialize tkinter
root = Tk()
root.title("Press Clips Reporter")
WINDOW_WIDTH = 800
HEIGHT = 600
CANVAS_WIDTH = WINDOW_WIDTH - 20
root.geometry(f"{WINDOW_WIDTH}x{HEIGHT}")

# set container as parent window
container = Frame(root, width = WINDOW_WIDTH, height = HEIGHT)

# create canvas within parent window
canvas = ResizingCanvas(container, width = CANVAS_WIDTH, height = HEIGHT, highlightthickness=0)

# add scrollbar
scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)

# add scrollable window within canvas
scrollable_frame = Frame(canvas, width = CANVAS_WIDTH, height = HEIGHT)

# change canvas size when scrollable window changes size
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

# change canvas size when scrollable window changes size
container.bind(
    "<Configure>",
    lambda e: canvas.configure(
        height=container.winfo_height(), width=container.winfo_width()-20
    )
)

# draw scrollable window within canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# set scrollarbar to move with canvas
canvas.configure(yscrollcommand=scrollbar.set)

# TEST #
label1 = Label(root, text='Calculate the Square Root')
label1.config(font=('helvetica', 14))

container.pack(fill=BOTH, expand=YES)
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window(200, 25, window=label1)
scrollbar.pack(side="right", fill="y")

root.mainloop()