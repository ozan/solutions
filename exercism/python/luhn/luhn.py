
class Luhn(object):

    MAPPING = dict(zip('0123456789', '0246813579'))

    def __init__(self, given):
        self.digits = list(str(given))

    def addends(self):
        kept = self.digits[-1::-2]
        mapped = [self.MAPPING[d] for d in self.digits[-2::-2]]
        return [int(d) for d in kept + mapped]

    def checksum(self):
        return sum(self.addends())

    def is_valid(self):
        return self.checksum() % 10 == 0

    @staticmethod
    def create(given):
        candidate = given * 10
        return candidate + (-Luhn(candidate).checksum() % 10)
