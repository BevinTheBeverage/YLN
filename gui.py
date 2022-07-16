# ADD SLIDER FOR NUMBER OF RESULTS WITH TICKINTERVAL 10: https://python-course.eu/tkinter/sliders-in-tkinter.php

from tkinter import *
from generate_report import generate_report, update_status
from PIL import Image
import os

TOPIC_ENTRY_WIDTH = 3

MAX_SUBTOPICS = 5

BG_COLOR = '#89CFF0'

class Topic:
    def __init__(self,  topic_entries, text=None, subtopics=[]):
        self.topic_entry = Entry(font=('Times New Roman', 16))
        self.topic_entries = topic_entries
        if(text):
            self.set_text(self.topic_entry, text)
        self.icon = PhotoImage(file='plus.png').subsample(25, 25)
        self.expand_btn = Button(root,
        image=self.icon,
        command=lambda: self.toggle_subtopics(self.topic_entries),
        #width=15, height=15
        )
        self.subtopics = subtopics
        self.subtopics_label = Label(root, text='Subtopics (Optional)', font=('Times New Roman', 14), bg=BG_COLOR)
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

    def toggle_subtopics(self, topic_entries):
        if self.subtopics_shown:
            for entry in self.subtopic_entries:
                entry.grid_remove()
            self.subtopics_label.grid_remove()
            self.hide_buttons()
        else:
            for topic in topic_entries:
                if topic.subtopics_shown:
                    topic.toggle_subtopics(topic_entries)
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

def refresh_buttons(add_topic_btn, delete_topic_btn, continue_btn, topic_entries):
    add_topic_btn.grid_remove()
    delete_topic_btn.grid_remove()
    continue_btn.grid_remove()
    add_topic_btn.grid(column=0, row = len(topic_entries)*(MAX_SUBTOPICS+4)+3, pady=(15, 10), columnspan=4)
    delete_topic_btn.grid(column=0, row=len(topic_entries)*(4+MAX_SUBTOPICS)+4, pady=(0, 15), columnspan=4)
    continue_btn.grid(column=0, row=len(topic_entries)*(4+MAX_SUBTOPICS)+5, pady=(0, 15), columnspan=4)

def add_topic(add_topic_btn, delete_topic_btn, continue_btn, topic_entries, text=None, subtopics = []):
    topic = (Topic(topic_entries, text, subtopics))
    topic_entries.append(topic)
    topic.grid(c = 0, r = (len(topic_entries)-1)*(MAX_SUBTOPICS+4)+2)
    refresh_buttons(add_topic_btn, delete_topic_btn, continue_btn, topic_entries)

def delete_topic(add_topic_btn, delete_topic_btn, continue_btn, topic_entries):
    if len(topic_entries) != 0:
        topic = topic_entries.pop(-1)
        topic.delete()
        refresh_buttons(add_topic_btn, delete_topic_btn, continue_btn, topic_entries)

def first_page():
    for widgets in root.winfo_children():
        widgets.destroy()

    title = Label(root, text='Press Clips Reporter', font=('Times New Roman', 24), bg=BG_COLOR)
    title.grid(row=0, column=0, columnspan=4, padx = 10, pady= 10)

    topics_label = Label(root, text='Topics', font=('Times New Roman', 20), bg=BG_COLOR)
    topics_label.grid(row=1, column=0, columnspan=4)

    topic_entries = []

    def next_page():
        topics = {}
        for topic in topic_entries:
            key = topic.topic_entry.get()
            if len(key) != 0:
                subtopics = [''] + list(filter(lambda text: len(text) != 0, [subtopic.get() for subtopic in topic.subtopic_entries]))
                topics[key] = subtopics
        for widgets in root.winfo_children():
            widgets.destroy()
        second_page(topics)

    add_topic_btn = Button(root, text= "   Add Topic   ", font=('Times New Roman', 14), command=lambda: add_topic(add_topic_btn, delete_topic_btn, continue_btn, topic_entries))
    delete_topic_btn = Button(root, text= "Remove Topic", font=('Times New Roman', 14), command=lambda: delete_topic(add_topic_btn, delete_topic_btn, continue_btn, topic_entries))
    continue_btn = Button(root, text= "Continue", font=('Times New Roman', 18), command=next_page)

    default_topics = {"Yuh-Line Niou": ['BDS'],
                "Bill de Blasio": [''],
                "Mondaire Jones": [''],
                "Carlina Rivera": [''],
                "Dan Goldman": [''],
                "Jo Anne Simon": ['']}

    for default_topic in default_topics.keys():
        add_topic(add_topic_btn, delete_topic_btn, continue_btn, topic_entries, default_topic, default_topics[default_topic])

def second_page(topics):
    title = Label(root, text='Press Clips Reporter', font=('Times New Roman', 24), bg=BG_COLOR)
    title.grid(row=0, column=0, padx=10, pady= 10)

    topics_and_subtopics_heading = "Topics and Subtopics:"
    topics_and_subtopics_display = ""

    for k, v in topics.items():
        subtopicsList = ''
        for i, subtopic in enumerate(list(filter(lambda text: len(text) != 0, v))):
            if i != 0:
                subtopicsList += ', '
            subtopicsList += subtopic
        topics_and_subtopics_display += f"{k}:\t{subtopicsList}\n" if len(subtopicsList) != 0 else f"{k}\n"

    topics_and_subtopics_heading_label = Label(root, text=topics_and_subtopics_heading, font=('Times New Roman', 16, 'bold'), bg=BG_COLOR)
    topics_and_subtopics_heading_label.grid(row=1, column=0)
    topics_and_subtopics_display_label = Label(root, text=topics_and_subtopics_display, font=('Times New Roman', 14), justify='left', bg=BG_COLOR)
    topics_and_subtopics_display_label.grid(row=2, column=0)

    results_slider_label = Label(root, text="Number of results per subtopic:", justify=CENTER, font=('Times New Roman', 14), bg=BG_COLOR)
    results_slider_label.grid(row=3, column=0)

    results_slider = Scale(root, from_=10, to=100, resolution=10, tickinterval=30, font=('Times New Roman', 14), orient=HORIZONTAL, length=210, bg=BG_COLOR, highlightthickness=0)
    results_slider.set(10)
    results_slider.grid(row=4, column=0)

    days_slider_label = Label(root, text="Days to search from:", justify=CENTER, font=('Times New Roman', 14), bg=BG_COLOR)
    days_slider_label.grid(row=5, column=0, pady=(10, 0))

    days_slider = Scale(root, from_=1, to=7, tickinterval=1, font=('Times New Roman', 14), orient=HORIZONTAL, length=210, bg=BG_COLOR, highlightthickness=0)
    days_slider.set(2)
    days_slider.grid(row=6, column=0)

    generate_btn = Button(root, text= "Generate Report", font=('Times New Roman', 14), command=lambda: third_page(topics, int(results_slider.get())/10, days_slider.get()))
    generate_btn.grid(row=7, column=0, pady=10)

def third_page(topics, pages, days):
    for widgets in root.winfo_children():
      widgets.destroy()

    title = Label(root, text='Press Clips Reporter', font=('Times New Roman', 24), bg=BG_COLOR)
    title.grid(row=0, column=0, padx=10, pady= 10)

    status_label = Label(root, text="Generating report...", font=('Times New Roman', 14), justify='left', bg=BG_COLOR)
    status_label.grid(row=1, column=0)

    # generate_report(status_label, root, topics, pages, days)

    try:
        filename = generate_report(status_label, root, topics, pages, days)
        open_btn = Button(root, text= "Open Reports Folder", font=('Times New Roman', 14), command=lambda: os.system("explorer.exe reports"))
        open_btn.grid(row=2, column=0, pady=10)
    except Exception as ex:
        if type(ex).__name__ != 'QuotaExceeded':
            template = "Report generation failed.\nAn exception of type {0} occurred.\nArguments:{1!r}.\nPlease contact Kevin with this information."
            message = template.format(type(ex).__name__, ex.args)
            update_status(root, status_label, message)
        
    restart_btn = Button(root, text= "New Report", font=('Times New Roman', 14), command=first_page)
    restart_btn.grid(row=3, column=0, pady=10)

if __name__ == '__main__':
    # initialize tkinter
    root = Tk()
    root.title("Press Clips Reporter")
    root.resizable(False, False)
    root.config(bg=BG_COLOR)  

    first_page()
    root.mainloop()
