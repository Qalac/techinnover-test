class Rover:

    def __init__(self, x_pos, y_pos, dir):
        self.x_pos = int(x_pos)
        self.y_pos = int(y_pos)
        self.dir = dir

    def setLeft(self):
        if self.dir == "N":
            self.dir = "W"
        elif self.dir == "E":
            self.dir = "N"
        elif self.dir == "W":
            self.dir = "S"
        elif self.dir == "S":
            self.dir = "E"

    def setRight(self):
        if self.dir == "N":
            self.dir = "E"
        elif self.dir == "E":
            self.dir = "S"
        elif self.dir == "W":
            self.dir = "N"
        elif self.dir == "S":
            self.dir = "W"

    def moveForward(self):
        if self.dir == "N":
            self.y_pos = self.y_pos + 1
        elif self.dir == "S":
            self.y_pos = self.y_pos - 1
        elif self.dir == "E":
            self.x_pos = self.x_pos + 1
        elif self.dir == "W":
            self.x_pos = self.x_pos - 1

    @property
    def position(self):
        dim = self.x_pos, self.y_pos, self.dir
        return dim