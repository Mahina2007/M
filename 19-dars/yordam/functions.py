from file_manager import read_from_json, write_to_json
import os
from datetime import datetime

def add_worker():
    name = input("name: ")
    time = input("came time: ")

    worker = {
        "name": name,
        "time": time
    }

    workers = read_from_json(file="workers.json")
    workers.append(worker)
    write_to_json(file="workers.json", data=workers)
    print("New worker is added")


def calculate():
    enter_name = input("enter name: ")
    workers = read_from_json("workers.json")
    for worker in workers:
        if worker['name'] == enter_name:
            start_time = "09:00"
            came_time = worker["time"]


            start_obj = datetime.strptime(start_time, "%H:%M")
            came_obj = datetime.strptime(came_time, "%H:%M")


            difference = (came_obj - start_obj).total_seconds() // 60

            if difference < 0:
                print(f"{enter_name} is on time")
            elif difference > 0:
                print(f"{enter_name} was late for {difference} minutes. Fine is {difference * 1000}")
            else:
                print("invalid choice")
            return

def clear_all():
    if os.path.exists("workers.json"):
        os.remove("workers.json")
        print("deleted")
    else:
        print("nothing is found")

def calculate_all():
    total_fine = 0
    workers = read_from_json("workers.json")
    start_time = "09:00"
    for worker in workers:
        if worker['time']:

            came_time = worker["time"]


            start_obj = datetime.strptime(start_time, "%H:%M")
            came_obj = datetime.strptime(came_time, "%H:%M")


            difference = (came_obj - start_obj).total_seconds() // 60

            if difference > 0:
                fine = difference * 1000
                total_fine += fine
    print(f"total fine is {total_fine}")
    return






