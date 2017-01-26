from pypot.primitive import LoopPrimitive
from pypot.primitive.utils import Sinus


class Dance(LoopPrimitive):
    def __init__(self, robot):
        LoopPrimitive.__init__(self, robot, 1.)

    def setup(self):
        for m in self.robot.motors:
            m.compliant = False

        self.sinus = [
            Sinus(self.robot, 25., [self.robot.m1], amp=90., freq=0.25),
            Sinus(self.robot, 25., [self.robot.m2], amp=60., freq=0.45, phase=180.),

            Sinus(self.robot, 25., [self.robot.m3], amp=30, freq=.8),
            
            Sinus(self.robot, 25., self.robot.motors, amp=10, freq=.1)
        ]

        init_pos = {'m1':0, 'm2':0, 'm3':90 }

        self.robot.goto_position(init_pos, 3., wait=True)

        for m in self.robot.motors:
            m.moving_speed = 150.

        for m in self.robot.motors:
            m.led = 'green'

        [s.start() for s in self.sinus]

    def update(self):
        pass

    def teardown(self):
        [s.stop() for s in self.sinus]
        
        for m in self.robot.motors:
            m.moving_speed = 0

        for m in self.robot.motors:
            m.led = 'off'