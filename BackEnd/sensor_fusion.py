
from front_end_client import *

class CommandToDrone:
    def __init__(self, start_states="up-down", to_drone = False):
        self.state_set = ["move_up-move_down", "move_forward-move_backward", 'move_left-move_right', 'turn_left-turn_right']
        self.command_mapping = {"neutral": 0, "move_up": 1, "move_down": 2, "move_left": 3, "move_right": 4, "move_forward": 5, "move_backward": 6, "turn_left": 7, "turn_right": 8}
        self.state = start_states
        self.allowed_to_execute = False
        self.front_end = FrontEndClient()
        self.to_drone = to_drone
        self.command = 0
        if to_drone:
            # process = sb.Popen(['node', 'drone_input.js'], stdin=sb.PIPE, stdout=sb.PIPE)
            # host = socket.
            pass
        if not self.state in self.state_set:
            self.state = self.state_set[0]

    def next_state(self):
        state_index = self.state_set.index(self.state)
        next_index = (len(self.state_set) + state_index + 1) % len(self.state_set)
        self.state = self.state_set[next_index]

    def update_command(self, command):
        self.command = command

    def execute_command(self):
        if self.allowed_to_execute:
            command = self.state.split("-")[self.command]
            self.send(command, self.command_mapping[command])
        else:
            self.send("neutral", self.command_mapping["neutral"])

    def send(self, command_to_ui, command_to_drone):
        self.front_end.call_method(command_to_ui)
        if self.to_drone:
            process = sb.Popen(self.drone_program, stdin=sb.PIPE, stdout=sb.PIPE)




class Sensor:
    def __init__(self, callback):
        self.sensor_data_state = {1: 'no-signal', 2: 'low-signal', 3: 'medium-signal', 4: 'high-signal'}
        self.callback = callback

    def update_data(self, data):
        self.callback(self.sensor_data_state[data])


class SensorFusion:
    def __init__(self):
        self.drone_command = CommandToDrone()
        self.sensor_1 = Sensor(self.sensor_1_callback)
        self.sensor_2 = Sensor(self.sensor_2_callback)
        self.sensor_3 = Sensor(self.sensor_3_callback)
        self.sensor_4 = Sensor(self.sensor_4_callback)


    def check_valid_input(self, sensor_data):
        sensor1_data, sensor2_data, sensor3_data, sensor4_data = sensor_data
        counter = 0
        pairs = []
        for i, val in zip(range(4), sensor_data):
            if val > 2:
                counter += 1
                pairs.append((i, val))
        if counter == 0:
            return False
        if counter == 1:
            return pairs[0]
        else: return False

    def update_sensor_data(self, sensor_data):
        list_of_sensors = [self.sensor_1, self.sensor_2, self.sensor_3, self.sensor_4]
        valid_result = self.check_valid_input(sensor_data)
        if valid_result:
            index, value = valid_result
            list_of_sensors[index].update_data(value)



    def sensor_1_callback(self, signal_type):
        if signal_type != 'high-signal':
            self.drone_command.allowed_to_execute = False
        else:
            self.drone_command.allowed_to_execute = True
        self.drone_command.execute_command()
        
    def sensor_2_callback(self, signal_type):
        pass

    def sensor_3_callback(self, signal_type):
        pass

    def sensor_4_callback(self, signal_type):
        if signal_type == 'high-signal':
            self.drone_command.next_state()
