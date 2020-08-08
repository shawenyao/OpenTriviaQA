import numpy as np
import random

print("====================================")
print("Welcome to OpenTriviaQA")
print("====================================")

categories = [
    "animals",
    "brain-teasers",
    "celebrities",
    "entertainment",
    "for-kids",
    "general",
    "geography",
    "history",
    "hobbies",
    "humanities",
    "literature",
    "movies",
    "music",
    "newest",
    "people",
    "rated",
    "religion-faith",
    "science-technology",
    "sports",
    "television",
    "video-games",
    "world"]
file_names = ["categories/" + category for category in categories]

lines_list = []
for file_name in file_names:
    with open(file_name, encoding='utf-8', errors='replace') as f:
        lines_raw = f.readlines()
        lines = [line.rstrip('\n') for line in lines_raw]
    lines_list.append(lines)

while True:
    for counter, value in enumerate(categories):

        print("Category: " + value)
        input('')

        index_start = np.where([line.startswith("#") for line in lines_list[counter]])[0]

        index = random.choice(index_start)

        while True:
            if lines_list[counter][index] == "":
                input('')
                print(lines_list[counter][index_answer])
                print("====================================")
                break
            elif lines_list[counter][index].startswith("^"):
                index_answer = index
            else:
                print(lines_list[counter][index])
            index = index + 1
