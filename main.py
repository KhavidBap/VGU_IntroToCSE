import time
from scheduler import *
from task1 import *
from task2 import *
from task3 import *
from task4 import *
from task5 import *
from task6 import *
from task7 import *

scheduler = Scheduler()
scheduler.SCH_Init()

task1 = Task1()
task2 = Task2()
task3 = Task3()
task4 = Task4()
task5 = Task5()
task6 = Task6()
task7 = Task7()

scheduler.SCH_Add_Task(task1.Task1_Run, 3000, 5000)
scheduler.SCH_Add_Task(task2.Task2_Run, 3000, 5000)
scheduler.SCH_Add_Task(task3.Task3_Run, 8000, 5000)
scheduler.SCH_Add_Task(task4.Task4_Run, 8000, 5000)
scheduler.SCH_Add_Task(task5.Task5_Run, 8000, 5000)
scheduler.SCH_Add_Task(task6.Task6_Run, 3000, 5000)
scheduler.SCH_Add_Task(task7.Task7_Run, 3000, 5000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)