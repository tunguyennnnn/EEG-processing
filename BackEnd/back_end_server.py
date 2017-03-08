"""
Provides an API for calling procedures on the front end through RPC.
"""
from concurrent import futures

import time

import grpc

import shared_pb2
import back_end_pb2

from main import acquire_data, reset, train, recognize, stop_recognition
from main import create_user_profile, delete_user_profile, get_user_profile, get_user_profiles, delete_user_data
from main import update_sensor_data


class BackEndServicer(back_end_pb2.BackEndServicer):

  def AcquireDataForCommand(self, request, context):
    command = COMMAND_MAP[request.command]
    acquire_data(request.username, command)

    status = shared_pb2.StatusReply(code=0)
    return status

  def ResetDataForCommand(self, request, context):
    command = COMMAND_MAP[request.command]
   
    delete_user_data(request.username, request.command)

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

  def StopRecognizion(self, request, context):
    stop_recognition()

    status = shared_pb2.StatusReply(code=0)
    return status

  def CreateUserProfile(self, request, context):
    create_user_profile(request.username)

    status = shared_pb2.StatusReply(code=0)
    return status

  def DeleteUserProfile(self, request, context):
    delete_user_profile(request.username)

    status = shared_pb2.StatusReply(code=0)
    return status

  def GetUserProfile(self, request, context):
    profile_data = get_user_profile(request.username)

    # Convert command strings to enum values
    profile_data = {COMMAND_MAP_INV[command_string]: num_samples for command_string, num_samples in profile_data.items()}

    profile_data_reply = back_end_pb2.ProfileDataReply(profile_data = profile_data)
    return profile_data_reply

  def GetUserProfiles(self, request, context):
    profiles = get_user_profiles()

    # Convert command strings to enum values
    profiles = {username: back_end_pb2.ProfileDataReply(profile_data = 
      {COMMAND_MAP_INV[command_string]: num_samples for command_string, num_samples in profile_data.items()}) for username, profile_data in profiles.items()}

    profile_list_reply = back_end_pb2.ProfileListReply(profile_list = profiles)
    return profile_list_reply

  def UpdateSensorData(self, request, context):
    sensor_data = request.sensor_data
    update_sensor_data(sensor_data)

    print(sensor_data)

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

# Inverted COMMAND_MAP
COMMAND_MAP_INV = {v: k for k, v in COMMAND_MAP.items()}
