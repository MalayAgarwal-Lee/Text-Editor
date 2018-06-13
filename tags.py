import font

FONT = font.get_font()

BLD_FONT = FONT + ('bold',)
IT_FONT = FONT + ('italic',)
UL_FONT = FONT + ('underline',)
BLD_IT_FONT = FONT + ('bold italic',)
BLD_UL_FONT = FONT + ('bold underline',)
IT_UL_FONT = FONT + ('italic underline',)
COMB_FONT = FONT + ('bold italic underline',)

TAGS = {'bld': {'tagName': 'bld', 'kw': {'font': BLD_FONT}},
        'it': {'tagName': 'it', 'kw': {'font': IT_FONT}},
        'ul': {'tagName': 'ul', 'kw': {'font': UL_FONT}},
        'bld-it': {'tagName': 'bld-it', 'kw': {'font': BLD_IT_FONT}},
        'bld-ul': {'tagName': 'bld-ul', 'kw': {'font': BLD_UL_FONT}},
        'it-ul': {'tagName': 'it-ul', 'kw': {'font': IT_UL_FONT}},
        'bld-it-ul': {'tagName': 'bld-it-ul', 'kw': {'font': COMB_FONT}}
        }
