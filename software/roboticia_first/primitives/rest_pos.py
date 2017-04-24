from pypot.primitive import Primitive

class Pos(Primitive):
    properties = Primitive.properties + ['p1'] + ['p2'] + ['p3'] +  ['duration'] + ['wait']
    def __init__(self, robot, p1 = 0, p2 = 0 , p3 = 0 , duration = 1, wait = True):
        Primitive.__init__(self, robot)
        self.duration = duration
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.wait = wait

    def run(self):
        self.robot.goto_position({'m1' : self.p1, 'm2' : self.p2, 'm3' : self.p3}, self.duration, wait=self.wait)
