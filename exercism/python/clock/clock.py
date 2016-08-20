
MINUTES_IN_A_DAY = 60 * 24


class Clock(object):
    def __init__(self, hours, mins):
        self.minutes = (hours * 60 + mins) % MINUTES_IN_A_DAY

    def __unicode__(self):
        return '{:02d}:{:02d}'.format(self.minutes // 60, self.minutes % 60)
    __str__ = __unicode__

    def __eq__(self, other):
        return self.minutes == other.minutes

    def add(self, mins):
        return Clock(0, self.minutes + mins)
