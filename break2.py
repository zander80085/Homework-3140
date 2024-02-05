
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

usernames = [
    "Adam",
    "Al",
    "Charles",
    "Ted",
    "Tom",
    "Bonnie",
    "Clyde",
    "Kevin",
    "Andrew",
    "Jack",
    "Richard",
    "Donald",
    "Kim",
    "Vlad",
    "Benedict",
    "Billy",
    "Anne",
    "John"
]

time_start = time.time()
for i in range(len(usernames)):
    for j in range(len(passwords)):
        arguments = ['python', 'Login.py', usernames[i], passwords[j]]
        process = subprocess.run(arguments)
time_end = time.time()
total_time = time_end - time_start
with open('username_password.txt', "r") as file:
    for lines in file:
        print(lines)
print(f"Total time taken: {total_time}s")