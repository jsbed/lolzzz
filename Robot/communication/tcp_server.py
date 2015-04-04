import zmq


class TcpServer():

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.DEALER)  # @UndefinedVariable

    def set_host(self, value):
        self._host = value

    def set_port(self, value):
        self._port = value

    def start_server(self):
        url = "tcp://{}:{}".format(self._host, self._port)
        self._socket.bind(url)

    def send_data(self, data):
        try:
            self._socket.send(bytes(data, "utf-8"))
        except:
            print('Send failed')

    def get_data(self):
        try:
            return self._socket.recv().decode("utf-8")
        except:
            print('Recv failed')
