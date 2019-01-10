

import os
import cv2
from random import shuffle
from tqdm import tqdm
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import *
from keras.optimizers import *


# vi ~/.matplotlib/matplotlibrc
# ----> backend: TkAgg

# urls obtained from http://imagenet.stanford.edu/
# saved as cat_all_urls
# saved as jellyfish_all_urls


# cat cat_all_urls | grep flickr > cat_flickr_urls
# head -400 cat_flickr_urls > train/cat/cat_train_urls
# tail -n +401 cat_flickr_urls | head -30 > test/cat/cat_test_urls

# cat jellyfish_all_urls | grep flickr > jellyfish_flickr_urls
# head -400 jellyfish_flickr_urls > train/jellyfish/jellyfish_train_urls
# tail -n +401 jellyfish_flickr_urls | head -30 > test/jellyfish/jellyfish_test_urls

# to download the images
# cd train/cat/cat_train_urls
# wget -i cat_train_urls


train_data = 'train'
test_data = 'test'


def rename_images(directory, label):
    index = 0
    for filename in os.listdir(os.path.join(directory, label)):
        if filename.endswith(".jpg"):
            index += 1
            os.rename(os.path.join(directory, label, filename), os.path.join(directory, label+'.'+str(index)+'.jpg'))
            continue
        else:
            continue


# rename_images(train_data, 'jellyfish')
# rename_images(train_data, 'cat')
# rename_images(test_data, 'jellyfish')
# rename_images(test_data, 'cat')


def one_hot_label(filename):
    label = filename.split('.')[0]
    if label == 'jellyfish':
        return np.array([1, 0])
    elif label == 'cat':
        return np.array([0, 1])


def train_data_with_label():
    train_images = []
    for filename in tqdm(os.listdir(train_data)):
        if filename.endswith(".jpg"):
            path = os.path.join(train_data, filename)
            image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (64, 64))
            train_images.append([np.array(image), one_hot_label(filename)])
    shuffle(train_images)
    return train_images


def test_data_with_label():
    test_images = []
    for filename in tqdm(os.listdir(test_data)):
        if filename.endswith(".jpg"):
            path = os.path.join(test_data, filename)
            image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (64, 64))
            test_images.append([np.array(image), one_hot_label(filename)])
    shuffle(test_images)
    return test_images


training_images = train_data_with_label()
testing_images = test_data_with_label()

tr_img_data = np.array([i[0] for i in training_images]).reshape(-1, 64, 64,1)
tr_lbl_data = np.array([i[1] for i in training_images])

tst_img_data = np.array([i[0] for i in testing_images]).reshape(-1,64,64,1)
tst_lbl_data = np.array([i[1] for i in testing_images])

model = Sequential()
model.add(InputLayer(input_shape=[64,64,1]))
model.add(Conv2D(filters=32, kernel_size=5, strides=1, padding='same', activation='relu'))
model.add(MaxPool2D(pool_size=5, padding='same'))

model.add(Conv2D(filters=50, kernel_size=5, strides=1, padding='same', activation='relu'))
model.add(MaxPool2D(pool_size=5, padding='same'))

model.add(Conv2D(filters=80, kernel_size=5, strides=1, padding='same', activation='relu'))
model.add(MaxPool2D(pool_size=5, padding='same'))

model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512, activation = 'relu'))
model.add(Dropout(rate=0.5))
model.add(Dense(2, activation = 'softmax'))
optimizer = Adam(lr=1e-3)

model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x=tr_img_data, y=tr_lbl_data, epochs=50, batch_size=100)
model.summary()


fig = plt.figure(figsize=(14, 14))

for cnt, data in enumerate(testing_images[10:40]):

    y = fig.add_subplot(6, 5, cnt+1)
    img = data[0]
    data = img.reshape(1, 64, 64, 1)
    model_out = model.predict([data])

    if np.argmax(model_out) == 1:
        str_label = 'Cat'
    else:
        str_label = "Jellyfish"

    y.imshow(img, cmap='gray')
    plt.title(str_label)
    y.axes.get_xaxis().set_visible(False)
    y.axes.get_yaxis().set_visible(False)

plt.show()



