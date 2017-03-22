"""
Provides an API for calling procedures on the front end through RPC.
"""
import grpc

from front_end_pb2 import FrontEndStub, CommandRequest, BCIDataRequest, ChannelData
import shared_pb2

class FrontEndClient:

    ADDRESS = 'localhost:50051'

    def __init__(self):
        channel = grpc.insecure_channel(self.ADDRESS)
        self.stub = FrontEndStub(channel)

    def move_forward(self):
        move_forward_command = shared_pb2.MOVE_FORWARD
        self.execute_command(move_forward_command)

    def move_backward(self):
        move_forward_command = shared_pb2.MOVE_BACK
        self.execute_command(move_forward_command)

    def move_right(self):
        move_forward_command = shared_pb2.MOVE_RIGHT
        self.execute_command(move_forward_command)

    def move_left(self):
        move_forward_command = shared_pb2.MOVE_LEFT
        self.execute_command(move_forward_command)

    def move_up(self):
        move_forward_command = shared_pb2.MOVE_UP
        self.execute_command(move_forward_command)

    def move_down(self):
        move_forward_command = shared_pb2.MOVE_DOWN
        self.execute_command(move_forward_command)

    def turn_right(self):
        move_forward_command = shared_pb2.TURN_RIGHT
        self.execute_command(move_forward_command)

    def turn_left(self):
        move_forward_command = shared_pb2.TURN_LEFT
        self.execute_command(move_forward_command)

    def neutral(self):
        move_forward_command = shared_pb2.RESET
        self.execute_command(move_forward_command)

    def execute_command(self, command):
        command_request = CommandRequest(command_type=command)
        response = self.stub.ExecuteMentalCommand(command_request)
        print("Front End responded with " + str(response.code))

    def UpdateBCIData(self, array):
        channel_data = []

        for row in array:
          channel_values = ChannelData(values=row)
          channel_data.append(channel_values)

        request = BCIDataRequest(BCIData=channel_data)
        response = self.stub.UpdateBCIData(request)

    def call_method(self, name):
        getattr(self, name)();
