class Topic:
    def __init__(self, text=None, subtopics=[]):
        self.topic_entry = Entry(font=('Times New Roman', 16))
        if(text):
            self.set_text(self.topic_entry, text)
        self.expand_btn = Button(root, text="+", font=('Times New Roman', 14), command=self.toggle_subtopics)
        self.subtopics = subtopics
        self.subtopics_label = Label(root, text='Subtopics', font=('Times New Roman', 16))
        self.add_subtopics_btn = Button(root, text= "Add Subtopic", font=('Times New Roman', 14), command=self.add_subtopic)
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
        self.add_subtopics_btn.grid(row=self.row+2+MAX_SUBTOPICS, column=self.col+1, columnspan=2)
        self.del_subtopics_btn.grid(row=self.row+3+MAX_SUBTOPICS, column=self.col+1, columnspan=2)
        
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
                entry.grid(row=self.row+i+2, column=1, padx=(60,0))
            self.subtopics_label.grid(row=self.row+1, column=self.col+1)
            self.show_buttons()
        self.subtopics_shown = not self.subtopics_shown

    def add_subtopic(self):
        if len(self.subtopic_entries) < MAX_SUBTOPICS:
            self.subtopic_entries.append(Entry(font=('Times New Roman', 16), width = 15))
            self.hide_buttons()
            self.subtopic_entries[-1].grid(row=self.row+1+len(self.subtopic_entries), column=1, padx=(60,0))
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
        self.topic_entry.grid(row=r, column=c, columnspan=TOPIC_ENTRY_WIDTH, padx=(10,0))
        self.expand_btn.grid(row=r, column=c+TOPIC_ENTRY_WIDTH, padx=(0, 15))

    def delete(self):
        self.topic_entry.grid_remove()
        self.expand_btn.grid_remove()
        self.subtopics_label.grid_remove()
        self.hide_buttons()
