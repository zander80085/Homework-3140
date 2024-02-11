import re
import hashlib
with open("hashedPWs.txt", 'r', encoding='utf-8') as file:
    hashed_tuples = []
    for line in file:
        if '\n' in line:
            stripped_line = re.sub('\n', "", line)
            spaced_line = re.sub(',', " ", stripped_line)
            if " " in spaced_line:
                line_split = spaced_line.split()
                hashed_tuples.append((line_split[0], line_split[1]))
    print(hashed_tuples)
with open('PwnedPWs100k.txt', 'r', encoding="utf-8") as file:
    password_hash_lst = {}
    for line in file:
        stripped_line = re.sub('\n', '', line)
        for number in range(0, 100):
            if number < 9:
                password = stripped_line + str(0)+ str(number)
            else:
                password = (stripped_line + str(number))
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            password_hash_lst[password_hash] = password
            print(password_hash_lst)
successful_crack = []
for hash in range(len(hashed_tuples)):
    if hashed_tuples[hash][1] in password_hash_lst:
        successful_crack.append((hashed_tuples[hash][0], hashed_tuples[hash][1], password_hash_lst[hashed_tuples[hash][1]]))
for element in range(len(successful_crack)):
    print(f'Username: {successful_crack[element][0]}, Password Hash = {successful_crack[element][1]}, Password = {successful_crack[element][2]}') 