from datetime import datetime
import random
from string import ascii_uppercase as a2z, digits as dig


class Robot(object):

    @classmethod
    def random_name(cls):
        random.seed(datetime.now())
        return ''.join(random.choice(xs) for xs in (a2z, a2z, dig, dig, dig))

    def __init__(self):
        self.reset()

    def reset(self):
        self.name = Robot.random_name()
