import os
from os import path
import shutil

''' RUN at upper directory of your working directory '''
old_dir_name = '220929_microk8s'
new_dir_name = '220929_microk8s_fixed'
current_path = os.getcwd()
old_path = current_path + '/' + old_dir_name
new_path = current_path + '/' + new_dir_name

files = os.listdir(old_path)
dirs = []

for file in files:
    if os.path.isdir(old_path + '/' + file):
        dirs.append(file)

if not path.isdir(new_path):
    os.makedirs(new_path)

for dir in dirs:
    old_dir_path = old_path + '/' + dir
    new_dir_path = new_path + '/' + dir
    files = os.listdir(old_path + '/' + dir)

    if not path.isdir(new_dir_path):
        os.makedirs(new_dir_path)

    for file in files:
        old_file_path = old_path + '/' + dir + '/' + file
        new_file_path = new_path + '/' + dir + '/' + file

        if not path.exists(new_file_path):
            a = os.stat(old_file_path).st_size
            if not os.stat(old_file_path).st_size == 0:
                shutil.copyfile(old_file_path, new_file_path)