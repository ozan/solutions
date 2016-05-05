
def clean(given):
    chars = [ch for ch in given if ch.isdigit()]
    if not (len(chars) == 10 or len(chars) == 11 and chars[0] == '1'):
        return False
    return ''.join(chars[-10:])


class Phone(object):

    INVALID = '0000000000'

    def __init__(self, given):
        self.number = clean(given) or self.INVALID

    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return '({}) {}-{}'.format(
            self.area_code(),
            self.number[3:6],
            self.number[6:]
        )
