#Task1
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            print(f"Elevator is moving from {self.current_floor} to {self.current_floor + 1}")
            self.current_floor += 1
            return True
        else:
            return False

    def floor_down(self):
        if self.current_floor > self.bottom:
            print(f"Elevator is moving from {self.current_floor} to {self.current_floor - 1}")
            self.current_floor -= 1
            return True
        else:
            return False

    def go_to_floor(self, floor_num):
        if floor_num > self.current_floor:
            for i in range(floor_num - self.current_floor):
                if not self.floor_up():
                    break

        elif  floor_num < self.current_floor:
            for i in range(floor_num + self.current_floor):
                if not self.floor_down():
                    break
        else:
            print(f"The elevator is already at this floor {self.current_floor}")

h = Elevator(1, 6)
target_floor = int(input("Which floor would you like to go to? "))
h.go_to_floor(target_floor)