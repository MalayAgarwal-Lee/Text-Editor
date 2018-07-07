import platform

operating_system = platform.system()

if operating_system == 'Windows':

    bold = '\uE19B'
    italic = '\uE199'
    underline = '\uE19A'

elif operating_system == 'Linux':

    bold = '\u0061'
    italic = ''
    underline = '\u00AA'

strike = 'S̵t̵r̵i̵k̵e̵'
