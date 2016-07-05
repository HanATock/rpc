import json
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = json.loads(self.request.recv(1024).strip().decode("utf-8"))
        print(self.data)
        function_dict[self.data["action"]](self.data["payload"])

if __name__ == "__main__":
    HOST, PORT = "192.168.178.43", 1338

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()


def set_value():
    # call function in server
    pass

function_dict = {
    'set_value': set_value
}


def read_pin(params):
    pass


def write_pin(params):
    pass


def register(params):
    pass


def read_analog(params):
    pass


def send_analog_update(params):
    pass
