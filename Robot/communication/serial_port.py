import serial


class SerialPort():

    def __init__(self, serial_port, baudrate=9600, timeout=0):
        self._serial = serial.Serial(serial_port, baudrate=baudrate,
                                     timeout=timeout)

    def send_string(self, data):
        print(data)
        self._serial.write(data.encode())

    def send_array_of_ints(self, array):
        self._serial.write(bytearray(array))

    # Wait for a non-empty line in the serial port
    def wait_for_read_line(self):
        while True:
            line = self._serial.readline()

            if line:
                return line.decode("utf-8")
