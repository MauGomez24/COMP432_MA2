import os
import random

dataset_dir = 'archive'
sample_size = 1000

for class_name in os.listdir(dataset_dir):
    class_path = os.path.join(dataset_dir, class_name)

    if os.path.isdir(class_path):
        files = os.listdir(class_path)

        if len(files) > sample_size:
            keep = random.sample(files, sample_size)
            delete = set(files) - set(keep)

            for file in delete:
                file_path = os.path.join(class_path, file)
                os.remove(file_path)

print("Files deleted successfully")