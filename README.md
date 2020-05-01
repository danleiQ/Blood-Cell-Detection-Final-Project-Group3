# Blood Cells Detection Using Faster R-CNN

With the evolvement of malaria, different kinds of cells would present. So if we can tell which kind of cells they are by the image, we will know which stage the malaria infection is in. This project aims to detect the malaria infected cells in the images using Faster R-CNN.

## Dataset

The link of dataset we use is [here](https://storage.googleapis.com/exam-deep-learning/train-Exam2.zip). This dataset contains a bunch of images, and their corresponding jason files, which include the coordinates of bounding boxes and labels. Here are some examples.

  ![cells_1](https://github.com/danleiQ/Final-Project-Group3/blob/master/images/cells_1.png)
![cells_2](https://github.com/danleiQ/Final-Project-Group3/blob/master/images/cells_2.png)

## Develope Faster R-CNN Model

The paper we refer to is [Faster R-CNN](https://arxiv.org/pdf/1506.01497.pdf), and the link of implementation we use is [here](https://github.com/kbardool/keras-frcnn.git). Some predicted images we get are shown below. 

 ![pred_cells_1](https://github.com/danleiQ/Final-Project-Group3/blob/master/images/pred_cells_1.png)
![pred_cells_2](https://github.com/danleiQ/Final-Project-Group3/blob/master/images/pred_cells_2.png)
