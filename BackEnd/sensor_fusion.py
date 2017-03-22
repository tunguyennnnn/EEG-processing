
from front_end_client import *
import time
import os
from threading import Thread
import subprocess as sb
class CommandToDrone:
    def __init__(self, start_states="move_forward-move_backward"):
        self.state_set = ["move_forward-move_backward", 'move_left-move_right', 'turn_left-turn_right']
        self.command_mapping = {"neutral": 0, "move_up": 1, "move_down": 2, "move_left": 3, "move_right": 4, "move_forward": 5, "move_backward": 6, "turn_left": 7, "turn_right": 8}
        self.state = start_states
        self.allowed_to_execute = False
        self.front_end = FrontEndClient()
        self.to_drone = False
        self.command = 0
        self.final_command = self.command
        self.speak_state = 'recognizing'
        self.is_executing = False
        if not self.state in self.state_set:
            self.state = self.state_set[0]

    def launch_the_drone(self):
        self.to_drone = True
        self.drone_process = sb.Popen(['node', 'drone_input.js'], stdin=sb.PIPE, stdout=sb.PIPE)

    def land_the_drone(self):
        if self.to_drone:
            self.drone_process.stdin.write('quit')
    def next_state(self):
        state_index = self.state_set.index(self.state)
        next_index = (len(self.state_set) + state_index + 1) % len(self.state_set)
        self.state = self.state_set[next_index]
        if self.state == "move_forward-move_backward":
            os.system('cmdmp3 mp3/mode_forward_backward.mp3');
        elif self.state == "move_up-move_down":
            os.system('cmdmp3 mp3/mode_up_down.mp3');
        elif self.state == 'move_left-move_right':
            os.system('cmdmp3 mp3/mode_left_right.mp3')
        elif self.state == 'turn_left-turn_right':
            os.system('cmdmp3 mp3/mode_turn_left_right.mp3')

    def update_command(self, command):
        self.command = command
        Thread(target=self.speak_the_command, args=(command, self.final_command)).start()

    def speak_the_command(self, command, final_command):
        if self.speak_state == 'recognizing':
            if command == 0:
                if self.state == "move_forward-move_backward":
                    os.system('cmdmp3 mp3/move_forward.mp3');
                elif self.state == "move_up-move_down":
                    os.system('cmdmp3 mp3/move_up.mp3');
                elif self.state == 'move_left-move_right':
                    os.system('cmdmp3 mp3/move_left.mp3')
                elif self.state == 'turn_left-turn_right':
                    os.system('cmdmp3 mp3/turn_left.mp3')
            elif command == 1:
                if self.state == "move_forward-move_backward":
                    os.system('cmdmp3 mp3/move_backward.mp3');
                elif self.state == "move_up-move_down":
                    os.system('cmdmp3 mp3/move_down.mp3');
                elif self.state == 'move_left-move_right':
                    os.system('cmdmp3 mp3/move_right.mp3')
                elif self.state == 'turn_left-turn_right':
                    os.system('cmdmp3 mp3/turn_right.mp3')
        elif self.speak_state == 'selecting':
            pass
            # if final_command == 0:
            #     if self.state == "move_forward-move_backward":
            #         os.system('cmdmp3 mp3/mode_go_forward.mp3');
            #     elif self.state == "move_up-move_down":
            #         os.system('cmdmp3 mp3/mode_go_up.mp3');
            #     elif self.state == 'move_left-move_right':
            #         os.system('cmdmp3 mp3/mode_go_left.mp3')
            #     elif self.state == 'turn_left-turn_right':
            #         os.system('cmdmp3 mp3/mode_turn_left.mp3')
            # elif final_command == 1:
            #     if self.state == "move_forward-move_backward":
            #         os.system('cmdmp3 mp3/mode_go_backward.mp3');
            #     elif self.state == "move_up-move_down":
            #         os.system('cmdmp3 mp3/mode_go_down.mp3');
            #     elif self.state == 'move_left-move_right':
            #         os.system('cmdmp3 mp3/mode_go_right.mp3')
            #     elif self.state == 'turn_left-turn_right':
            #         os.system('cmdmp3 mp3/mode_turn_right.mp3')

    def execute_command(self):
        command = self.state.split("-")[self.command]
        self.send(command, self.command_mapping[command], True)



    def update_final_command(self):
        if self.speak_state == 'selecting':
            self.speak_state = 'recognizing'
        else:
            self.speak_state = 'selecting'
            self.final_command = self.command
            if self.final_command == 0:
                if self.state == "move_forward-move_backward":
                    os.system('cmdmp3 mp3/mode_go_forward.mp3');
                elif self.state == "move_up-move_down":
                    os.system('cmdmp3 mp3/mode_go_up.mp3');
                elif self.state == 'move_left-move_right':
                    os.system('cmdmp3 mp3/mode_go_left.mp3')
                elif self.state == 'turn_left-turn_right':
                    os.system('cmdmp3 mp3/mode_turn_left.mp3')
            elif self.final_command == 1:
                if self.state == "move_forward-move_backward":
                    os.system('cmdmp3 mp3/mode_go_backward.mp3');
                elif self.state == "move_up-move_down":
                    os.system('cmdmp3 mp3/mode_go_down.mp3');
                elif self.state == 'move_left-move_right':
                    os.system('cmdmp3 mp3/mode_go_right.mp3')
                elif self.state == 'turn_left-turn_right':
                    os.system('cmdmp3 mp3/mode_turn_right.mp3')


    def send(self, command_to_ui, command_to_drone, drone):
        self.front_end.call_method(command_to_ui)
        time.sleep(0.5)
        self.front_end.call_method("neutral")
        if self.to_drone and (not self.is_executing):
            self.is_executing = True
            self.drone_process.stdin.write(str(command_to_drone))
            time.sleep(0.5)
            if "done" in self.drone_process.stdout.readline():
                self.is_executing = False
            else:
                time.sleep(0.5)
                self.is_executing = False




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
        self.sensor_5 = Sensor(self.sensor_5_callback) # 1 and 2 combined
        self.sensor_6 = Sensor(self.sensor_6_callback)


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
        if counter == 2:
            if pairs[0][0] == 0 and pairs[1][0] == 1:
                return (4, 4)
            else:
                return False
        else: return False

    def update_sensor_data(self, sensor_data):
        list_of_sensors = [self.sensor_1, self.sensor_2, self.sensor_3, self.sensor_4, self.sensor_5, self.sensor_6]
        valid_result = self.check_valid_input(sensor_data)
        if valid_result:
            index, value = valid_result
            list_of_sensors[index].update_data(value)

    def launch_the_drone(self):
        self.drone_command.launch_the_drone()

    def land_the_drone(self):
        self.drone_command.land_the_drone()

    def sensor_1_callback(self, signal_type):
        if signal_type == 'high-signal'or signal_type == 'medium-signal':
            self.drone_command.execute_command()

    def sensor_2_callback(self, signal_type):
        if signal_type == 'high-signal' or signal_type == 'medium-signal':
            self.drone_command.update_final_command()

    def sensor_3_callback(self, signal_type):
        if signal_type == 'high-signal' or signal_type == 'medium-signal':
            self.drone_command.drone_process.stdin.write("quit");

    def sensor_4_callback(self, signal_type):
        if signal_type == 'high-signal' or signal_type == 'medium-signal':
            self.drone_command.next_state()

    def sensor_5_callback(self, signal_type):
        if signal_type == 'high-signal':
            self.drone_command.update_final_command()

    def sensor_6_callback(self, signal_type):
        pass
