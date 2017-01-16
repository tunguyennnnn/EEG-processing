"""
Provides an API for calling procedures on the front end through RPC.
"""
from concurrent import futures

import grpc

import shared_pb2
import back_end_pb2
from main import acquire_data, train, recognize
import time

class BackEndServicer(back_end_pb2.BackEndServicer):

  def AcquireDataForCommand(self, request, context):
    command = COMMAND_MAP[request.command]
    acquire_data(request.username, command)

    status = shared_pb2.StatusReply(code=0)
    return status

  def TrainClassifier(self, request, context):
    command_list = [COMMAND_MAP[command] for command in request.command_list]

    train(request.username, command_list)

    status = shared_pb2.StatusReply(code=0)
    return status

  def RecognizeCommands(self, request, context):
    recognize(request.username)

    status = shared_pb2.StatusReply(code=0)
    return status

  
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
  back_end_pb2.add_BackEndServicer_to_server(BackEndServicer(), server)
  server.add_insecure_port('[::]:50052')
  server.start()

  print("Server started")
  try:
    while True:
      time.sleep(60 * 60 * 24)
  except KeyboardInterrupt:
    print("Stopping the server...")
    server.stop(0)

COMMAND_TABLES = ["NEUTRAL", "UP", "DOWN", "RIGHT", "LEFT", "FORWARD", "BACKWARD"]

COMMAND_MAP = {
  shared_pb2.RESET: 'NEUTRAL',
  shared_pb2.MOVE_UP: 'UP',
  shared_pb2.MOVE_DOWN: 'DOWN',
  shared_pb2.MOVE_RIGHT: 'RIGHT',
  shared_pb2.MOVE_LEFT: 'LEFT',
  shared_pb2.MOVE_FORWARD: 'FORWARD',
  shared_pb2.MOVE_BACK: 'BACKWARD'
}
