import ctypes

from functools import partial
from numpy import sum

from pypot.creatures import AbstractPoppyCreature

from .primitives.dance import Dance
from .primitives.mirror import Mirror
from .primitives.rest_pos import Pos


class RoboticiaFirst(AbstractPoppyCreature):
    @classmethod
    def setup(cls, robot):
        robot._primitive_manager._filter = partial(sum, axis=0)
        for m in robot.motors:
            m.goto_behavior = 'dummy'
            m.moving_speed = 0

        robot.attach_primitive(Dance(robot), 'dance')
        robot.attach_primitive(Mirror(robot,50), 'mirror')
        robot.attach_primitive(Pos(robot), 'pos')

        if robot.simulated:
            cls.vrep_hack(robot)
            cls.add_vrep_methods(robot)


    @classmethod
    def vrep_hack(cls, robot):
        # fix vrep orientation bug
        wrong_motor = [robot.m3, robot.m2]
        
        for m in wrong_motor:
            m.direct = not m.direct
            #m.offset = -m.offset
            
        # use minjerk to simulate speed in vrep
        for m in robot.motors:
            m.goto_behavior = 'minjerk'
            
    @classmethod
    def add_vrep_methods(cls, robot):
        from pypot.vrep.controller import VrepController
        from pypot.vrep.io import remote_api

        def set_vrep_force(robot, vector_force, shape_name):
            """ Set a force to apply on the robot. """
            vrep_io = next(c for c in robot._controllers
                           if isinstance(c, VrepController)).io

            raw_bytes = (ctypes.c_ubyte * len(shape_name)).from_buffer_copy(shape_name)
            vrep_io.call_remote_api('simxSetStringSignal', 'shape',
                                    raw_bytes, sending=True)

            packedData = remote_api.simxPackFloats(vector_force)
            raw_bytes = (ctypes.c_ubyte * len(packedData)).from_buffer_copy(packedData)
            vrep_io.call_remote_api('simxSetStringSignal', 'force',
                                    raw_bytes, sending=True)

        robot.set_vrep_force = partial(set_vrep_force, robot)
        
