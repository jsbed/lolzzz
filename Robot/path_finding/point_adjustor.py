from collections.__main__ import Point
from Robot.path_finding.grid import SquareGrid


class PointAdjustor():
    def __init__(self):
        self._grid = SquareGrid()
        self._target_point = Point(0, 0)
        self._cube_center = Point(0, 0)
        self._robot_position = Point(0, 0)

    '''
    Description: Verify if the cube is too close or next to a wall
                 and adjust the target position accordingly. Otherwise,
                 call adjut_target_point to find the target position
                 closest to the robot.
    '''
    def check_if_cube_too_close_to_wall(self):
        if (self._cube_center.x < self._grid.get_robot_radius()):
            self._target_point = Point(self._target_point.x +
                                       self._grid.get_cube_radius() +
                                       self._grid.get_robot_radius(),
                                       self._target_point.y)

        elif (self._cube_center.x > (self._grid.get_width() -
                                     self._grid.get_robot_radius())):
            self._target_point = Point(self._target_point.x -
                                       self._grid.get_cube_radius() -
                                       self._grid.get_robot_radius(),
                                       self._target_point.y)

        elif (self._cube_center.y > (self._grid.get_height() -
                                     self._grid.get_robot_radius())):
            self._target_point = Point(self._target_point.x,
                                       self._target_point.y -
                                       self._grid.get_cube_radius() -
                                       self._grid.get_robot_radius())

        elif (self._cube_center.y < self._grid.get_robot_radius()):
            self._target_point = Point(self._target_point.x,
                                       self._target_point.y +
                                       self._grid.get_cube_radius() +
                                       self._grid.get_robot_radius())

        else:
            self.adjust_target_point()

    def adjust_target_point(self):
        if (self._cube_center.x <= self._robot_position.x):
            if (self._cube_center.y <= (self._robot_position.y -
                                        self._grid.get_robot_radius() -
                                        self._grid.get_cube_radius())):
                self._target_point = Point(self._target_point.x,
                                           self._target_point.y +
                                           self._grid.get_cube_radius() +
                                           self._grid.get_robot_radius())

            elif (self._cube_center.y >= (self._robot_position.y +
                                          self._grid.get_robot_radius() +
                                          self._grid.get_cube_radius())):
                self._target_point = Point(self._target_point.x,
                                           self._target_point.y -
                                           self._grid.get_cube_radius() -
                                           self._grid.get_robot_radius())

            else:
                self._target_point = (self._target_point.x +
                                      self._grid.get_cube_radius() +
                                      self._grid.get_robot_radius(),
                                      self._target_point.y)

        else:
            self._target_point = Point(self._target_point.x -
                                       self._grid.get_cube_radius() -
                                       self._grid.get_robot_radius(),
                                       self._target_point.y)

    def find_target_position(self, cube_position, robot_position):
        self._target_point = cube_position
        self._cube_center = cube_position
        self._robot_position = robot_position
        self.check_if_cube_too_close_to_wall()
        return self._target_point
