
import time
import subprocess

password_list = []
with open('PwnedPWs100k.txt', 'r', encoding='utf-8') as file:
    for line in file:
        stripped_line = line.strip()
        if stripped_line:
            password_list.append(stripped_line)

usernames = [
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
    for j in range(len(password_list)):
        arguments = ['python', 'Login.py', usernames[i], password_list[j]]
        process = subprocess.run(arguments)
time_end = time.time()
total_time = time_end - time_start
print(f"Total time taken: {total_time}s")