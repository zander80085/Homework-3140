
import time
import subprocess
passwords = [
    '123456',
    '123456789',
    'picture1',
    'password',
    '12345678',
    '111111',
    '123123',
    '12345',
    '1234567890',
    'senha',
    '1234567',
    'qwerty',
    'abc123',
    'Million2',
    '1234',
    'iloveyou',
    'aaron431',
    'password1',
    'qqww1122'
]
processes = []
username = "Adam"
time_start = time.time()
for i in range(len(passwords)):
    arguments = ['python', 'Login.py', username, passwords[i]]
    process = subprocess.Popen(arguments)
    processes.append(process)
time_end = time.time()
total_time = time_end - time_start
print(f"Total time taken: {total_time}s")