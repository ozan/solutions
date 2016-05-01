NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

DISPLACEMENTS = ((0, 1), (1, 0), (0, -1), (-1, 0))


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def _turn(self, direction):
        self.bearing = (self.bearing + direction + 4) % 4

    def turn_left(self):
        self._turn(-1)

    def turn_right(self):
        self._turn(1)

    def advance(self):
        coord_disp = zip(self.coordinates, DISPLACEMENTS[self.bearing])
        self.coordinates = tuple(map(sum, coord_disp))

    def simulate(self, instructions):
        do = {'L': self.turn_left, 'R': self.turn_right, 'A': self.advance}
        [do[ch]() for ch in instructions]
