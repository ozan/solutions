
LINES = """the horse and the hound and the horn
that belonged to *the farmer sowing his corn
that kept *the rooster that crowed in the morn
that woke *the priest all shaven and shorn
that married *the man all tattered and torn
that kissed *the maiden all forlorn
that milked *the cow with the crumpled horn
that tossed *the dog
that worried *the cat
that killed *the rat
that ate *the malt
that lay in """.split('*')


def verse(n):
    inner = '' if n == 0 else ''.join(LINES[-n:])
    return 'This is {}the house that Jack built.'.format(inner)


def rhyme():
    return '\n\n'.join(verse(n) for n in range(12))
