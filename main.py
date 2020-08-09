from os import listdir
import numpy as np
import random

print('====================================')
print('Welcome to OpenTriviaQA')
print('====================================')
input('All available categories:')

# show all available categories
categories_all = listdir('categories/')
for counter, value in enumerate(categories_all):
    print(str(counter + 1) + ': ' + value)

# let user specify categories of choice
print('====================================')
print('Input the categories of choice, separated by comma:')
categories_input = input('')

# parse user input
categories_input_index = [int(index) - 1 for index in categories_input.split(',')]
categories_input_index = set(np.clip(categories_input_index, 0, len(categories_all) - 1))  # avoid illegal index
categories = [categories_all[i] for i in categories_input_index]

# print selected categories
print('Selected categories:')
for counter, value in enumerate(categories):
    print(str(counter + 1) + ': ' + value)
print('====================================')

# read all questions in selected categories
file_names = ['categories/' + category for category in categories]
lines_list = []
for file_name in file_names:
    with open(file_name, encoding='utf-8', errors='replace') as f:
        lines_raw = f.readlines()
        lines = [line.rstrip('\n') for line in lines_raw]
    lines_list.append(lines)

# game begins
round_count = 1
while True:
    # loop through categories
    for counter, value in enumerate(categories):

        print('Round ' + str(round_count) + ', Player ' + str(counter + 1) + '/' + str(len(categories)))
        
        print('Category: ' + value)
        input('')

        # find all rows where a question starts
        index_start = np.where([line.startswith('#') for line in lines_list[counter]])[0]

        # randomly select the next question
        index = random.choice(index_start)

        while True:
            # if it's the end of the question, wait for user input to show the answer and break the loop
            if lines_list[counter][index] == '' and index_answer is not None:
                input('')

                # print the answer
                print(lines_list[counter][index_answer])
                index_answer = None
                print('====================================')
                break

            # if it's the answer, remember the position
            elif lines_list[counter][index].startswith('^'):
                # remember where the answer is
                index_answer = index

            # if it's the question, print it
            else:
                print(lines_list[counter][index])
            index = index + 1

    round_count = round_count + 1