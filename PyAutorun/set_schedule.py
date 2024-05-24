import os
START_TIME = '20:00'
SCRIPT_LOC = "D:/PyAutorun/ITSFRIDAY.py"
TASK_NAME = "FRIDAY_NIGHT"

os.system(fr'SchTasks /Create /SC WEEKLY /D FRI /TN {TASK_NAME} /TR {SCRIPT_LOC} /ST {START_TIME}')