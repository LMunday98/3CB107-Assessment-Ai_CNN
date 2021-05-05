import os, sys
import shutil
import random

original_dataset = "Hands/"
filename = "HandInfo.txt"
dataset_folder_name = "dataset_final/"
hand_types = ['palm', 'dorsal', 'both']
mode = 0o777

def create_dir(folder_path, type, mode, gender):
    try: 
        os.makedirs(os.path.join(folder_path, type, gender), mode)
    except OSError as error:
        print(error)

def sort_image(type, info_dict, dataset_folder_name):
    if ("palmar" in info_dict['hand_aspect']):
        shutil.copy2(original_dataset + info_dict['image_name'], os.path.join(dataset_folder_path, "palm" , type, info_dict['gender']))
    elif ("dorsal" in info_dict['hand_aspect']):
        shutil.copy2(original_dataset + info_dict['image_name'], os.path.join(dataset_folder_path, "dorsal", type, info_dict['gender']))
    shutil.copy2(original_dataset + image_name, os.path.join(dataset_folder_path, "both", type, info_dict['gender']))

for hand_type in hand_types:
    dataset_folder_path = os.path.join(dataset_folder_name, hand_type)
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

for hand_type in hand_types:
    dataset_folder_path = os.path.join(dataset_folder_name, hand_type)
    
    for gender in ['male', 'female']:
        create_dir(dataset_folder_path, "train", gender, mode)
        create_dir(dataset_folder_path, "valid", gender, mode)

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

    if (subject in training_female or subject in training_male):
        if ("palmar" in ting[6]):
            shutil.copy2(original_dataset + image_name, os.path.join(dataset_folder_path, "palm" ,"train", gender))
        elif ("dorsal" in ting[6]):
            shutil.copy2(original_dataset + image_name, os.path.join(dataset_folder_path, "dorsal", "train", gender))
        shutil.copy2(original_dataset + image_name, os.path.join(dataset_folder_path, "both", "train", gender))
    elif (subject in valid_female or subject in valid_male):
        if ("palmar" in ting[6]):
            shutil.copy2(original_dataset + image_name, os.path.join(dataset_folder_path, "palm", "valid", gender))
        elif ("dorsal" in ting[6]): 
            shutil.copy2(original_dataset + image_name, os.path.join(dataset_folder_path, "dorsal", "valid", gender))
        shutil.copy2(original_dataset + image_name, os.path.join(dataset_folder_path, "both", "valid", gender))
