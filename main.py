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

# a list of all the questions by category
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

        # find all rows where a question starts
        index_start = np.where([line.startswith("#") for line in lines_list[counter]])[0]

        # randomly select the next question
        index = random.choice(index_start)

        while True:
            # if it's the end of the question
            if lines_list[counter][index] == "":
                input('')

                # print the answer
                print(lines_list[counter][index_answer])
                print("====================================")
                break

            # if it's the answer
            elif lines_list[counter][index].startswith("^"):
                # remember where the answer is
                index_answer = index

            # if it's the question
            else:
                print(lines_list[counter][index])
            index = index + 1
