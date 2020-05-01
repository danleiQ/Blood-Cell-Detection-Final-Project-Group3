import ast
import os
import numpy as np
import pandas as pd

# python 3.5
# pip install keras==2.1.6
# pip install tensorflow==1.13.1
# pip install opencv-python
if "train" not in os.listdir():
    os.system("wget https://storage.googleapis.com/exam-deep-learning/train-Exam2.zip")
    os.system("unzip train-Exam2")
DATA_DIR = os.getcwd() + "/train/"

train = []

for file in os.scandir(DATA_DIR):

    if file.name.endswith('png'):

        # img = cv2.imread(os.path.join(DATA_DIR, file.name))
        json_ = file.name[:-4]+'.json'
        b = open(os.path.join(DATA_DIR, json_))
        loc = b.read()
        loc = ast.literal_eval(loc)
        # print(loc)
        b.close()

        for i in range(len(loc)):
            # filepath,x1,y1,x2,y2,class_name
            train.append([DATA_DIR+file.name, loc[i]['bounding_box']['minimum']['r'], loc[i]['bounding_box']['minimum']['c'],
                          loc[i]['bounding_box']['maximum']['r'], loc[i]['bounding_box']['maximum']['c'], loc[i]['category']])

print(len(train))  # len(data)=59456

train = pd.DataFrame(np.array(train).reshape(-1, 6))

train.to_csv('annotate.txt', header=None, index=None, sep=',')

# cd keras-frcnn
# python train_frcnn.py -o simple -p annotate.txt

