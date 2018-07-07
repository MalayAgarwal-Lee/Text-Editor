import platform


OP_SYS = platform.system()


def get_font():
    if OP_SYS == 'Linux':
        return ('Ubuntu', 12)
    elif OP_SYS == 'Windows':
        return ('Segoe UI', 12)
    else:
        return ('San Francisco', 12)
