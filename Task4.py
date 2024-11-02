"""class Elevator:
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

        elif floor_num < self.current_floor:
            for i in range(floor_num + self.current_floor):
                if not self.floor_down():
                    break
        else:
            print(f"The elevator is already at this floor {self.current_floor}")


h = Elevator(1, 6)
target_floor = int(input("Which floor would you like to go to? "))
h.go_to_floor(target_floor)


# Task 2
class Building:
    def __init__(self, bottom, top, ele_num):
        self.ele_num = []
        for i in range(ele_num):
            self.ele_num.append(Elevator(bottom, top))

    def run_elevator(self, elevator, floor_number):
        print(f"The {elevator} is moving")
        self.ele_num[elevator - 1].go_to_floor(floor_number)
#Task3
    def fire_alarm(self):
        print("There is a fire!")
        for i in self.ele_num:
            i.go_to_floor(i.bottom)


print("\n Elevators in the building are: ")
building1 = Building(1, 7, 3)
building1.run_elevator(1, 5)
building1.run_elevator(2, 5)
building1.fire_alarm()
"""
#Task 4
import random
from mod9 import Car

class Race:
    def __init__(self,name,distance,cars):
        self.cars = cars

    def hours_passses(self):
        for car in self.cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1.)

    def print_status(self):
        print(self.name + ":")
        print("Plate Speed Odomete")
        print("--------------------")
        for car in self.cars:
            print(f"{car.regPlate: 6s } : {car.speed : 3d}, {car.odometer}  ")

    def race_finished(self):
        for car in self.cars:
            if car.odometer >= self.distance:
                return True
            return False
cars = []
for i in range(10):
    cars.append(Car("ABC-" + str(i+1), random.randint(100,200)))

race1 = Race("Grand Demolition Derby", 8000., cars)
n = 0
while not race1.race_finished():
    race1.hours_passses()
    n += 1
    if n % 10 == 0:
        print(f"After {n} hours passes")
        race1.print_status()
print(f"Final results, after {n} hours passes")
race1.print_status()
