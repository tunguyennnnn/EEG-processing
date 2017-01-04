import grpc

import simulation_pb2

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = simulation_pb2.FrontEndStub(channel)
    move_forward(stub)

def move_forward(stub):
    move_forward_command = simulation_pb2.CommandRequest.MOVE_FORWARD
    move_forward_request = simulation_pb2.CommandRequest(command_type=move_forward_command)

    response = stub.ExecuteMentalCommand(move_forward_request)
    print("Greeter client received: " + str(response.code))

if __name__ == '__main__':
    run()
