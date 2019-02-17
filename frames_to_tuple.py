import numpy as np
import random
import os
def get_file_count(letter):
    letter = letter.upper()
    return len(os.listdir(letter))

def get_trimmed_data(letter, number):
    file_name = "%s/frame%04d.txt" % (letter.upper(), number)
    frame_file = open(file_name, "r")
    lines = frame_file.readlines()
    return [line.strip() for line in lines]

def classname_to_number(classname):
    return ["R","P","S"].index(classname)


def get_random_dataset():
    letter = random.choice(["R","P","S"])
    max_file = get_file_count(letter)
    file_num = random.randrange(max_file)
    return (clean_to_nparray(letter, file_num) , letter)
    
    
def generate_random_data_sets(cases):
    labels = []
    data_sets = []
    for i in range(cases):
        data_set, letter = get_random_dataset()
        labels.append(classname_to_number(letter))
        data_sets.append(data_set)
    return (np.array(data_sets), labels)
        

def clean_to_nparray(letter, number):
    array_lines = []
    trimmed_data = get_trimmed_data(letter,number)
    for line in trimmed_data:
        fields = line.split(",")
        fields = [float(field.strip()) for field in fields]
        field_count = len(fields)
        if field_count == 6:
            array_lines.append(fields[0:3])
            array_lines.append(fields[3:6])
        else:
            array_lines.append(fields)

    return array_lines

def construct_data_classifier_tuple():
    letters = ["R", "P", "S"]
    labels = []
    data_sets = []
    for letter in letters:
        for number in range(get_file_count(letter)):
            labels.append(classname_to_number(letter))
            data_sets.append(clean_to_nparray(letter, number))
    return (np.array(data_sets), labels)

def numbered_construct_data_classifier_tuple(upperbound):
    letters = ["R", "P", "S"]
    labels = []
    data_sets = []
    for letter in letters:
        for number in range(upperbound):
            labels.append(classname_to_number(letter))
            data_sets.append(clean_to_nparray(letter, number))
    return (np.array(data_sets), labels)


