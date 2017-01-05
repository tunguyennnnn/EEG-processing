import grpc
import simulation_pb2 as SP
class FrontEndClient:
    def __init__(self):
        self.address = 'localhost:50051'

    def connect(self):
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = SP.FrontEndStub(channel)
        self.is_connected = True


    def move_forward(self):
        move_forward_command = SP.CommandRequest.MOVE_FORWARD
        self.execute_command(move_forward_command)

    def move_backward(self):
        move_forward_command = SP.CommandRequest.MOVE_BACK
        self.execute_command(move_forward_command)

    def move_right(self):
        move_forward_command = SP.CommandRequest.MOVE_RIGHT
        self.execute_command(move_forward_command)

    def move_left(self):
        move_forward_command = SP.CommandRequest.MOVE_LEFT
        self.execute_command(move_forward_command)

    def move_up(self):
        move_forward_command = SP.CommandRequest.MOVE_UP
        self.execute_command(move_forward_command)

    def move_down(self):
        move_forward_command = SP.CommandRequest.MOVE_DOWN
        self.execute_command(move_forward_command)

    def turn_right(self):
        move_forward_command = SP.CommandRequest.TURN_RIGHT
        self.execute_command(move_forward_command)

    def turn_left(self):
        move_forward_command = SP.CommandRequest.TURN_LEFT
        self.execute_command(move_forward_command)

    def neutral(self):
        move_forward_command = SP.CommandRequest.RESET
        self.execute_command(move_forward_command)

    def execute_command(self, command):
        move_forward_request = SP.CommandRequest(command_type=command)
        response = self.stub.ExecuteMentalCommand(move_forward_request)
        print(str(response.code))
