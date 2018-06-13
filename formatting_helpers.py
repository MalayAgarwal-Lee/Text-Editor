from tkinter import *
from tags import *


def styling_helper(obj, format_type):
        text_box = obj.text_box

        try:
            start_index = text_box.index('sel.first')
            end_index = text_box.index('sel.last')

            tag_names = text_box.tag_names(start_index)
            last_formatting = tag_names[-1]

            for formatting in tag_names[1:]:
                text_box.tag_remove(formatting, start_index, end_index)

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

            text_box.tag_config(tag['tagName'], **tag['kw'])
            text_box.tag_add(tag['tagName'], start_index, end_index)

        except TclError:
            pass
