from tkinter import *
from formatting_helpers import *
from tags import *
from helper_classes import *


class MainPage(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill=BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.format_frame = FormattingFrame(self)
        self.format_frame.pack(side=TOP)

        format_frame = self.format_frame

        format_frame.bold_button.config(command=self.make_bold)
        format_frame.italic_button.config(command=self.make_italic)
        format_frame.underline_button.config(command=self.make_underline)

        self.text_frame = Frame(self)
        self.text_frame.pack(fill=BOTH, expand=True)

        self.text_box = TextBox(self.text_frame)

    def make_bold(self):
        styling_helper(self, 'bld')

    def make_italic(self):
        styling_helper(self, 'it')

    def make_underline(self):
        styling_helper(self, 'ul')


root = Tk()
root.option_add('*tearOff', FALSE)
main_page = MainPage(master=root)
main_page.mainloop()
