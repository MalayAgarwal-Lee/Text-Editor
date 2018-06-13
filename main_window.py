from tkinter import *
import font
from tags import *

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


class MenuBar(Menu):
    pass


class MainPage(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill=BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.menu_frame = Frame(self)
        self.menu_frame.pack(side=TOP)

        self.bold_button = FormatButton(self.menu_frame,
                                        text='Bold',
                                        command=self.make_bold)

        self.italic_button = FormatButton(self.menu_frame,
                                          text='Italic',
                                          command=self.make_italic)

        self.underline_button = FormatButton(self.menu_frame,
                                             text='Underline',
                                             command=self.make_underline)

        self.text_frame = Frame(self)
        self.text_frame.pack(fill=BOTH, expand=True)

        self.text_box = TextBox(self.text_frame)

    def formatting_dispatcher(self, format_type):
        text_box = self.text_box

        try:
            start_index = text_box.index('sel.first')
            end_index = text_box.index('sel.last')

            tag_names = text_box.tag_names(start_index)
            last_formatting = tag_names[-1]

            for formatting in tag_names[1:]:
                self.text_box.tag_remove(formatting, start_index, end_index)

            if last_formatting == 'sel':
                formats = [format_type]

            elif format_type in last_formatting:
                formats = last_formatting.split('-')
                formats = [x for x in formats if x != format_type]
                formats.sort()

            else:
                formats = last_formatting.split('-') + [format_type]
                formats.sort()

            formatting_strng = '-'.join(formats)

            if formatting_strng and formatting_strng != 'sel':
                tag = TAGS[formatting_strng]
            else:
                return

            self.text_box.tag_config(tag['tagName'], **tag['kw'])
            self.text_box.tag_add(tag['tagName'], start_index, end_index)

        except TclError:
            pass

    def make_bold(self):
        self.formatting_dispatcher('bld')

    def make_italic(self):
        self.formatting_dispatcher('it')

    def make_underline(self):
        self.formatting_dispatcher('ul')


root = Tk()
main_page = MainPage(master=root)
main_page.mainloop()
