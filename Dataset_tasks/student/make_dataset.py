import threading
import os
import csv
with open(os.path.join("../../data/student/student.csv")) as file:
    a = csv.DictReader(file)
    print(a)

