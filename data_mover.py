import shutil
import os
import random

ORIGIN_PATH = 'ORIGIN/PATH/TO/THE/IMAGE/'
MOVE_PATH = 'NEW/PATH/TO/THE/IMAGE/'
number_of_moving_data = 200 #number of images to be moved

for class_name in os.listdir(ORIGIN_PATH):
    data_dir = ORIGIN_PATH + class_name + '/'
    class_list = os.listdir(data_dir)
    random.shuffle(class_list)
    for i in range(int(number_of_moving_data/len(os.listdir(ORIGIN_PATH)))):
        move_image_path = data_dir + class_list[i]
        move_path = MOVE_PATH + class_name
        if os.path.isdir(move_path):
            shutil.move(move_image_path, move_path)
        else:
            os.mkdir(move_path)
            shutil.move(move_image_path, move_path)
