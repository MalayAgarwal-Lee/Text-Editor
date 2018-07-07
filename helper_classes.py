from tkinter import *
import font
import unicode_chars


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
        self.customize()

    def customize(self):
        self['background'] = 'gray99'
        self['width'] = 10
        self['padx'] = 5
        self['pady'] = 5
        self['borderwidth'] = 0


class FormattingFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(side=TOP, fill=X)
        self.configure(background='gray99', borderwidth=2)

        self.create_widgets()

    def create_widgets(self):
        self.bold_button = FormatButton(self, text=unicode_chars.bold)
        self.underline_button = FormatButton(self, text=unicode_chars.underline)
        self.italic_button = FormatButton(self, text=unicode_chars.italic)
        self.strike_through = FormatButton(self, text=unicode_chars.strike)

        self.bold_button.pack(side=LEFT)
        self.underline_button.pack(side=LEFT)
        self.italic_button.pack(side=LEFT)
        self.strike_through.pack(side=LEFT)
