
import time
import subprocess

password_list = []
with open('PwnedPWs100k.txt', 'r', encoding='utf-8') as file:
    for line in file:
        password_list.append(line)

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