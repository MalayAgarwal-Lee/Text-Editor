from tkinter import *
from tags import *


def styling_helper(obj, format_type):
    """
    Function to apply bld, it and ul styling

    Arguments:
        obj: main_window.MainPage object
        format_type, str, 'bld', 'it' or 'ul'

    Return:
        None
    """

    # storing the TextBox object in variable
    # for faster access
    text_box = obj.text_box

    # catching selection, if any
    try:
        # getting the start, end of selection
        start_index = text_box.index('sel.first')
        end_index = text_box.index('sel.last')

        # getting prexisting tags applied at selection
        # 'sel' tag is always present
        tag_names = text_box.tag_names(start_index)

        # getting the last formatting applied on the selection
        # can be any of the tags defined in tags.py
        # including 'sel' (if no tags are applied)
        last_formatting = tag_names[-1]

        # removing all tags, except 'sel' (always the first tag)
        for formatting in tag_names[1:]:
            text_box.tag_remove(formatting, start_index, end_index)

        # 'sel' if no previous tags have been applied
        # storing the tag passed in a list
        if last_formatting == 'sel':
            formats = [format_type]

        # if tag was already applied, needs to be removed
        # with all other formatting still intact
        elif format_type in last_formatting:

            # splitting the last formatting's name into components
            # will be a list containing 'bld', 'it' and 'ul' (see tags.py)
            formats = last_formatting.split('-')

            # excluding the passed formatting from the list
            formats = [x for x in formats if x != format_type]
            
            # if passed tag was the only pre-existing formatting
            # and the corresponding format button was clicked
            # list will be empty
            # if list's empty, we can return
            # because tag was already removed by for loop
            if not formats:
                return

            # sorting is important since tags.py stores alphabetically
            # 'bld' < 'it' < 'ul'
            formats.sort()

        # none above true implies passed tag is new
        # adding it to a list, sorting the list
        else:
            formats = last_formatting.split('-') + [format_type]
            formats.sort()

        # creating a string of the form: 'fmt1-...-fmtn', n = 1, 2, 3
        # using the list made in if clauses
        formatting_strng = '-'.join(formats)

        # Obtaining relevant tag to be applied
        # from 'TAG' dict in tags.py
        tag = TAGS[formatting_strng]

        # configuring and adding the obtained tag
        text_box.tag_config(tag['tagName'], **tag['kw'])
        text_box.tag_add(tag['tagName'], start_index, end_index)

    except TclError:
        pass
