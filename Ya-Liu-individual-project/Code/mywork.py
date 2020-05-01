import os
import numpy as np
import tensorflow as tf
import cv2
import torch
import torch.nn as nn
import pandas as pd
import matplotlib.pyplot as plt
from torchvision import datasets
import json
import ast
from matplotlib import patches
from PIL import Image

if "train-Exam2.zip" not in os.listdir():
    os.system("wget https://storage.googleapis.com/exam-deep-learning/train-Exam2.zip")
    os.system("unzip train-Exam2.zip")

DATA_DIR = os.getcwd() + "/train/"

data = []

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
           if loc[i]['category'] != 'red blood cell':
            # filepath,x1,y1,x2,y2,class_name
              data.append([DATA_DIR+file.name, loc[i]['bounding_box']['minimum']['r'], loc[i]['bounding_box']['minimum']['c'],
                          loc[i]['bounding_box']['maximum']['r'], loc[i]['bounding_box']['maximum']['c'], loc[i]['category']])

print(len(data))

imgs = []
for i in range(len(data)):
  if data[i][0] not in imgs:
    imgs.append(data[i][0])


# Data to plot
labels = 'difficult', 'gametocyte', 'leukocyte', 'ring', 'schizont', 'trophozoite'
sizes = [328, 109, 67, 354, 143, 1099]
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
explode = (0, 0, 0, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()

def drawBox(data, img_name):
    fig = plt.figure()

    # add axes to the image
    ax = fig.add_axes([0, 0, 1, 1])

    # read and plot the image
    image = plt.imread(os.path.join(DATA_DIR, img_name))
    plt.imshow(image)

    # iterating over the image for different objects
    # for _,row in train[train.image_names == "cells_1.png"].iterrows():
    for i in range(len(data)):
        # xmin = row.xmin
        # xmax = row.xmax
        # ymin = row.ymin
        # ymax = row.ymax
        (x1, y1, x2, y2) = (data[i][1], data[i][2], data[i][3], data[i][4])

        width = x2 - x1
        height = y2 - y1

        # assign different color to different classes of objects
        # if data[i][5] == 'red blood cell':
        #     edgecolor = 'red'
        #     ax.annotate('red blood cell', xy=(x2-40,y1+20))
        if data[i][5] == 'difficult':
            edgecolor = 'blue'
            ax.annotate('difficult', xy=(x2 - 40, y1 + 20))
        elif data[i][5] == 'gametocyte':
            edgecolor = 'green'
            ax.annotate('gametocyte', xy=(x2 - 40, y1 + 20))
        elif data[i][5] == 'leukocyte':
            edgecolor = 'yellow'
            ax.annotate('leukocyte', xy=(x2 - 40, y1 + 20))
        elif data[i][5] == 'ring':
            edgecolor = 'black'
            ax.annotate('ring', xy=(x2 - 40, y1 + 20))
        elif data[i][5] == 'schizont':
            edgecolor = 'orange'
            ax.annotate('schizont', xy=(x2 - 40, y1 + 20))
        elif data[i][5] == 'trophozoite':
            edgecolor = 'red'
            ax.annotate('trophozoite', xy=(x2 - 40, y1 + 20))

        # add bounding boxes to the image
        rect = patches.Rectangle((x1, y1), width, height, edgecolor=edgecolor, facecolor='none')

        ax.add_patch(rect)

drawBox(data, 'cells_2.png')