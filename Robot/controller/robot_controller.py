from time import sleep

from Robot.configuration import config
from Robot.controller.instructions.move import Move
from Robot.controller.robot import Robot
from Robot.game_cycle import atlas
from Robot.managers.led_manager import LedManager
from Robot.path_finding.point_adjustor import PointAdjustor
from Robot.controller.instructions.rotate import Rotate


class RobotController():

    def __init__(self):
        self._robot = Robot(None)
        self._find_target_point_and_robot_orientation = PointAdjustor()
        self._led_manager = LedManager(None)

    def get_cube(self, cube):
        return self._move_to(cube.get_localization().position)

    def move_cube(self, cube):
        return self._move_to(cube.get_target_zone_position())

    def get_question_from_atlas(self):
        self._led_manager.display_red_led()
        sleep(2)
        self._led_manager.close_red_led()
        return atlas.get_question()

    def move_to_atlas(self):
        self._robot.update_localization()
        robot_position = self._robot.get_localization_position()
        robot_orientation = self._robot.get_localization_orientation()
        target_point = self._find_target_point_and_robot_orientation.find_next_point(robot_position,
                                                      config.Config().
                                                      get_atlas_zone_position())
        distance = \
            self._find_target_point_and_robot_orientation._calculate_distance_between_points(robot_position,
                                                              target_point)
        if (self._verify_distance(distance)):
            return True

        target_orientation = \
            self._find_target_point_and_robot_orientation.find_robot_orientation(robot_orientation,
                                                  robot_position,
                                                  target_point)
        Rotate().rotate(target_orientation)
        Move().move(distance)
        self._robot.append_instruction(Rotate().execute)
        self._robot.append_instruction(Move().execute)
        self._robot.execute_instructions()
        return False

    def display_country_leds(self, country):
        self._led_manager.display_country(country)
        sleep(5)

    def ask_for_cube(self, cube):
        self._led_manager.next_flag_led(cube)

    def _move_to(self, destination):
        self._robot.update_localization()
        robot_position = self._robot.get_localization_position()
        robot_orientation = self._robot.get_localization_orientation()
        target_point = \
            self._find_target_point_and_robot_orientation.find_target_position(destination,
                                                robot_position)
        next_point = self._find_target_point_and_robot_orientation.find_next_point(robot_position,
                                                    target_point)
        distance = \
            self._find_target_point_and_robot_orientation._calculate_distance_between_points(robot_position,
                                                              next_point)
        if (self._verify_distance(distance)):
            return True

        target_orientation = \
            self._find_target_point_and_robot_orientation.find_robot_orientation(robot_orientation,
                                                  robot_position,
                                                  next_point)
        Rotate().rotate(target_orientation)
        Move().move(distance)
        self._robot.append_instruction(Rotate().execute)
        self._robot.append_instruction(Move().execute)
        self._robot.execute_instructions()
        return False

    def _verify_distance(self, distance):
        if (distance <= config.Config().get_distance_uncertainty()):
            return True
        else:
            return False
