from tkinter import *

TOPIC_ENTRY_WIDTH = 4

class Topic:
    def __init__(self, text=None):
        self.topic_entry = Entry(font=('Times New Roman', 16))
        if(text):
            self.set_text(text)
        self.expand_btn = Button(root, text="+", font=('Times New Roman', 14), command=self.toggle_subtopics)

    def toggle_subtopics(self):
        # TODO
        return

    def set_text(self, text):
        self.topic_entry.delete(0,END)
        self.topic_entry.insert(0,text)

    def grid(self, r, c):
        self.topic_entry.grid(row=r, column=c, columnspan=TOPIC_ENTRY_WIDTH)
        self.expand_btn.grid(row=r, column=c+TOPIC_ENTRY_WIDTH)

# initialize tkinter
root = Tk()
root.title("Press Clips Reporter")

title = Label(root, text='Press Clips Reporter', font=('Times New Roman', 24))
title.grid(row=0, column=1, ipadx=10, ipady=10)

topics_label = Label(root, text='Topics', font=('Times New Roman', 20))
topics_label.grid(row=1, column=1, ipadx=10, ipady=10)

topic_entries = []

def add_topic(text=None):
    topic = (Topic(text))
    topic_entries.append(topic)
    topic.grid(c = 0, r = len(topic_entries)+3)
    add_topic_btn.pack_forget()
    add_topic_btn.grid(column=1, row=len(topic_entries)+5)

add_topic_btn = Button(root, text= "Add Topic", font=('Times New Roman', 14), command=add_topic)

default_topics = [
        'Yuh-Line Niou',
        'Bill de Blasio'
    ]

for default_topic in default_topics:
    add_topic(default_topic)

for i, topic in enumerate(topic_entries):
    topic.grid(c = 0, r = i+3)

root.mainloop()
