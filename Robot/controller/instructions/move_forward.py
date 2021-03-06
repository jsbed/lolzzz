from Robot.controller.robot_instruction import RobotInstruction


NUMBER_OF_BYTES = 9
EMPTY_BYTE = "0"
CM_TO_MM_MULTIPLIER = 10
MOVE_BACKWARD = "BA"
MOVE_FOWARD = "GO"


class MoveForward(RobotInstruction):

    def __init__(self, distance_cm):
        self._distance_mm = int(distance_cm * CM_TO_MM_MULTIPLIER)

    def execute(self, serial_port):
        if (self._distance_mm != 0):
            command_to_send = self._format_distance_to_string()
            serial_port.send_string(command_to_send)

    def _format_distance_to_string(self):
        if (self._distance_mm < 0):
            formated_string = MOVE_BACKWARD
            self._distance_mm = abs(self._distance_mm)

        else:
            formated_string = MOVE_FOWARD

        distance_string = str(self._distance_mm)

        while(len(distance_string) < NUMBER_OF_BYTES):
            distance_string = EMPTY_BYTE + distance_string

        formated_string += distance_string

        return formated_string

    def __str__(self):
        return "move: " + str(self._distance_mm / CM_TO_MM_MULTIPLIER)
