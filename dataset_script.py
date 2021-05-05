import os, sys
import shutil
import random

original_dataset = "Hands/"
filename = "HandInfo.txt"

# set to dorsal, palmar or both
hand_type = "dorsal"

dataset_folder_name = "dataset2/"
dataset_folder_path = os.path.join(dataset_folder_name, hand_type)

# mode
mode = 0o777

try: 
    os.mkdir(dataset_folder_name, mode)
except OSError as error:
    print(error)

try: 
    os.makedirs(dataset_folder_path)
except OSError as error:
    print(error)


f = open(filename, "r")

male_list = []
female_list = []

for line in f:
    ting = line.split(",")
    subject = ting[0]
    gender = ting[2]
    if (gender == "male"):
        if (subject not in male_list):
            male_list.append(subject)
    else:
        if (subject not in female_list):
            female_list.append(subject)

percentage = float(80)

k = len(male_list) * percentage / 100
k = int(k)
indicies = random.sample(range(len(male_list)), k)
training_male = [male_list[i] for i in indicies]
valid_male = list(set(male_list)-set(training_male))

k1 = len(female_list) * percentage / 100
k1 = int(k1)
indicies1 = random.sample(range(len(female_list)), k1)
training_female = [female_list[i] for i in indicies1]
valid_female = list(set(female_list)-set(training_female))

f = open(filename, "r")

for line in f:
    ting = line.split(",")
    subject = ting[0]
    gender = ting[2]
    image_name = ting[7]

    try: 
        os.makedirs(os.path.join(dataset_folder_path, "train", gender), mode)
    except OSError as error:
        print(error)

    try: 
        os.makedirs(os.path.join(dataset_folder_path, "valid", gender), mode)
    except OSError as error:
        print(error)

    if (hand_type in ting[6] or hand_type == "both"):
        if (subject in training_female or subject in training_male):
            shutil.copy2(original_dataset + image_name, os.path.join(dataset_folder_path, "train", gender))
        elif (subject in valid_female or subject in valid_male):
            shutil.copy2(original_dataset + image_name, os.path.join(dataset_folder_path, "valid", gender))
            
        
