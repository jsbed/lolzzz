from Robot.robot.path_finder import PathFinder
from Robot.robot.robot import Robot
from collections.__main__ import Point
from time import sleep
from Robot.robot.grid import SquareGrid
from Robot.robot.point_adjustor import PointAdjustor


class RobotService():

    def __init__(self):
        self._robot = Robot()
        self._path_finder = PathFinder()
        self._table_grid = SquareGrid()
        self._path = []
        self._adjustor = PointAdjustor(self._table_grid)
        self._target_point = Point(0, 0)

    def get_cube(self, cube):
        self._target_point =  \
            self._adjustor.find_target_position(cube.get_localization().
                                                position,
                                                self._robot.get_localization().
                                                position)
        self._path = self._path_finder.a_star_search(
            self._table_grid,
            self._robot.get_localization().position,
            self._target_point)
        # TODO: Move the robot via the path

    def move_cube(self, cube):
        self._path = self._path_finder.a_star_search(
            self._table_grid,
            self._robot.get_localization().position,
            cube.get_target_zone_position())
        # TODO: Move the robot via the path

    def get_question_from_atlas(self):
        self.move_to_atlas()
        # TODO: Show question led
        sleep(2)

    def move_to_atlas(self):
        self._path = self._path_finder.a_star_search(
            self._table_grid,
            self._robot.get_localization().position,
            self._table_grid.get_atlas_zone_position())
        # TODO: Move the robot via the path

    def display_country_leds(self, country):
        # TODO: display country with led
        sleep(5)

    def ask_for_cube(self, cube):
        # TODO: Led Manager
        pass
