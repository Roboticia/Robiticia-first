import requests
from pypot.primitive import LoopPrimitive


class Mirror(LoopPrimitive):
    def __init__(self, robot, refresh_freq):
        self.robot = robot
        LoopPrimitive.__init__(self, robot, refresh_freq)
        
    def setup(self):
        for m in self.robot.motors:
            m.compliant = False
        for m in self.robot.motors:
            m.led = 'pink'

    # The update function is automatically called at the frequency given on the constructor
    def update(self):
        for m in self.robot.motors:
            try :
                r = requests.get('http://roboticia-first-02.local:8080/motor/'+m.name+'/register/present_position')
            except :
                pass
            else :
                m.goal_position = r.json()['present_position']   
            
    def teardown(self):
        for m in self.robot.motors:
            m.led = 'off'