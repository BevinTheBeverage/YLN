from tkinter import *

# initialize tkinter
root = Tk()
root.title("Press Clips Reporter")

title = Label(root, text='Press Clips Reporter', font=('Times New Roman', 24))
title.pack(padx=100, pady=(25, 0))

topics_label = Label(root, text='Topics', font=('Times New Roman', 20), justify=LEFT)
topics_label.pack(padx=50, anchor='w')

topic_entries = [Entry(font=('Times New Roman', 16))]
for entry in topic_entries:
    entry.pack(pady=(5, 25), anchor='w', padx=55)

root.mainloop()
