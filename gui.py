# ADD SLIDER FOR NUMBER OF RESULTS WITH TICKINTERVAL 10: https://python-course.eu/tkinter/sliders-in-tkinter.php

from tkinter import *
from PIL import Image

TOPIC_ENTRY_WIDTH = 3

MAX_SUBTOPICS = 5

class Topic:
    def __init__(self, text=None, subtopics=[]):
        self.topic_entry = Entry(font=('Times New Roman', 16))
        if(text):
            self.set_text(self.topic_entry, text)
        self.icon = PhotoImage(file='plus.png').subsample(25, 25)
        self.expand_btn = Button(root, image=self.icon, command=self.toggle_subtopics, width=15, height=15)
        self.subtopics = subtopics
        self.subtopics_label = Label(root, text='Subtopics (Optional)', font=('Times New Roman', 16), bg='#89CFF0')
        self.add_subtopics_btn = Button(root, text= "   Add Subtopic   ", font=('Times New Roman', 14), command=self.add_subtopic)
        self.del_subtopics_btn = Button(root, text= "Remove Subtopic", font=('Times New Roman', 14), command=self.remove_subtopic)
        self.subtopics_shown = False
        self.subtopic_entries = [Entry(font=('Times New Roman', 16), width = 15) for subtopic in subtopics]
        self.row = 0
        self.col = 0
        for i, entry in enumerate(self.subtopic_entries):
            self.set_text(entry, subtopics[i])

    def hide_buttons(self):
        self.add_subtopics_btn.grid_remove()
        self.del_subtopics_btn.grid_remove()

    def show_buttons(self):
        self.add_subtopics_btn.grid(row=self.row+2+MAX_SUBTOPICS, column=0, columnspan=4, pady=(15, 5))
        self.del_subtopics_btn.grid(row=self.row+3+MAX_SUBTOPICS, column=0, columnspan=4, pady=(5, 15))
        
    def toggle_subtopics(self):
        if self.subtopics_shown:
            for entry in self.subtopic_entries:
                entry.grid_remove()
            self.subtopics_label.grid_remove()
            self.hide_buttons()
        else:
            for topic in topic_entries:
                if topic.subtopics_shown:
                    topic.toggle_subtopics()
            for i, entry in enumerate(self.subtopic_entries):
                entry.grid(row=self.row+i+2, column=1, columnspan=2, pady=5)
            self.subtopics_label.grid(row=self.row+1, column=0, columnspan=4, pady=(10, 0))
            self.show_buttons()
        self.subtopics_shown = not self.subtopics_shown

    def add_subtopic(self):
        if len(self.subtopic_entries) < MAX_SUBTOPICS:
            self.subtopic_entries.append(Entry(font=('Times New Roman', 16), width = 15))
            self.hide_buttons()
            self.subtopic_entries[-1].grid(row=self.row+1+len(self.subtopic_entries), column=1, columnspan=2, pady=5)
            self.show_buttons()

    def remove_subtopic(self):
        if len(self.subtopic_entries) != 0:
            entry = self.subtopic_entries.pop(-1)
            entry.grid_remove()
            self.hide_buttons()
            self.show_buttons()

    def set_text(self, entry, text):
        entry.delete(0,END)
        entry.insert(0,text)

    def grid(self, r, c):
        self.row, self.col = r, c
        self.topic_entry.grid(row=r, column=c, columnspan=TOPIC_ENTRY_WIDTH, padx=(10,0), pady=(10, 0))
        self.expand_btn.grid(row=r, column=c+TOPIC_ENTRY_WIDTH, pady=(10, 0))

    def delete(self):
        self.topic_entry.grid_remove()
        self.expand_btn.grid_remove()
        self.subtopics_label.grid_remove()
        self.hide_buttons()

def refresh_buttons():
    add_topic_btn.grid_remove()
    delete_topic_btn.grid_remove()
    add_topic_btn.grid(column=0, row = len(topic_entries)*(MAX_SUBTOPICS+4)+3, pady=(15, 10), columnspan=4)
    delete_topic_btn.grid(column=0, row=len(topic_entries)*(4+MAX_SUBTOPICS)+4, pady=(0, 15), columnspan=4)

def add_topic(text=None, subtopics = []):
    topic = (Topic(text, subtopics))
    topic_entries.append(topic)
    topic.grid(c = 0, r = (len(topic_entries)-1)*(MAX_SUBTOPICS+4)+2)
    refresh_buttons()

def delete_topic():
    if len(topic_entries) != 0:
        topic = topic_entries.pop(-1)
        topic.delete()
        refresh_buttons()

# initialize tkinter
root = Tk()
root.title("Press Clips Reporter")
root.resizable(False, False)
root.config(bg='#89CFF0')

title = Label(root, text='Press Clips Reporter', font=('Times New Roman', 24), bg='#89CFF0')
title.grid(row=0, column=0, columnspan=4, padx = 10, pady= 10)

topics_label = Label(root, text='Topics', font=('Times New Roman', 20), bg='#89CFF0')
topics_label.grid(row=1, column=0, columnspan=4)

topic_entries = []

add_topic_btn = Button(root, text= "   Add Topic   ", font=('Times New Roman', 14), command=add_topic)

delete_topic_btn = Button(root, text= "Remove Topic", font=('Times New Roman', 14), command=delete_topic)

default_topics = {"Yuh-Line Niou": ['BDS'],
            "Bill de Blasio": [''],
            "Mondaire Jones": [''],
            "Carlina Rivera": [''],
            "Dan Goldman": [''],
            "Jo Anne Simon": ['']}

for default_topic in default_topics.keys():
    add_topic(default_topic, default_topics[default_topic])

root.mainloop()
