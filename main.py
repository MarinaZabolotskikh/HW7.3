import os

BASE_PATH = os.getcwd()
TEXT_NAME = "text"
file_list = os.listdir(TEXT_NAME)
FILE_NAME = "comb_text.txt"

all_list = []
res = None
for files in file_list:
    with open(os.path.join(TEXT_NAME, files), 'r', encoding= "utf-8") as f:
        all_list.append([files, 0, []])
        for line in f:
            all_list[-1][2].append(line.strip())
            all_list[-1][1] += 1
            res = sorted(all_list, key=lambda x: x[1])
with open(FILE_NAME, 'w', encoding="utf-8") as newfile:
    for strings in res:
        newfile.write(f"{strings[0]} \n{strings[1]} \n")
        for string in strings[2]:
            newfile.write(string + '\n')











