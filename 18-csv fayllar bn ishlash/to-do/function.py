from file_manager import append, read
from utils import generate_new_id
import csv



def add_task():
    new_id = generate_new_id(filename="tasks")
    name = input("Enter task name: ")

    task = [new_id, name, 0]
    append(filename="tasks", data=task)
    print("New task is added")

def show_all():
        reader = csv.reader("tasks.csv")
        print(list(reader))
        for line in reader:
            print(line)

