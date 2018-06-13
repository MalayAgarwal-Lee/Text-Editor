from tkinter import *
import font


FONT = font.get_font()


class TextBox(Text):
    def __init__(self, master=None, font=FONT):
        super().__init__(master, font=font)

        self.add_scrollbar()
        self.config(wrap=WORD, spacing2=10)
        self.pack(side=LEFT, fill=BOTH, expand=True)

    def add_scrollbar(self):
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)

        scrollbar.config(command=self.yview)
        self.config(yscrollcommand=scrollbar.set)


class FormatButton(Button):
    def __init__(self, master=None, text='', command=None):
        super().__init__(master, text=text, command=command)
        self.pack(side=LEFT)


class FormattingFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(side=TOP, fill=X)
        self.configure(background='gray99', borderwidth=2)

        self.create_widgets()

    def create_widgets(self):
        self.bold_button = FormatButton(self, text='Bold')
        self.underline_button = FormatButton(self, text='Underline')
        self.italic_button = FormatButton(self, text='Italic')
