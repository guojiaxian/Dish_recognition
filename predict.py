import os
import keras
from PIL import Image
import numpy as np
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.optimizers import SGD, RMSprop, Adam
from keras.layers import Conv2D, MaxPooling2D
from matplotlib import pyplot as plt

def prepicture(picname):
    img = Image.open('./pic/'+picname)
    new_img = img.resize((224, 224), Image.BILINEAR)
    new_img.save(os.path.join('./pic/', os.path.basename(picname)))

def read_image2(filename):
    img = Image.open('./pic/'+filename).convert('RGB')
    return np.array(img)

picname = input("请输入图片：")

# 图片预处理
prepicture(picname)
x_test = []
x_test.append(read_image2(picname))
x_test = np.array(x_test)
x_test = x_test.astype('float32')
x_test /= 255

keras.backend.clear_session()

model = Sequential()
model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(224, 224, 3), padding='SAME'))
model.add(Conv2D(64, (3, 3), activation='relu', padding='SAME'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3, 3), activation='relu', padding='SAME'))
model.add(Conv2D(128, (3, 3), activation='relu', padding='SAME'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(256, (3, 3), activation='relu', padding='SAME'))
model.add(Conv2D(256, (3, 3), activation='relu', padding='SAME'))
model.add(Conv2D(256, (3, 3), activation='relu', padding='SAME'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(512, (3, 3), activation='relu', padding='SAME'))
model.add(Conv2D(512, (3, 3), activation='relu', padding='SAME'))
model.add(Conv2D(512, (3, 3), activation='relu', padding='SAME'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(512, (3, 3), activation='relu', padding='SAME'))
model.add(Conv2D(512, (3, 3), activation='relu', padding='SAME'))
model.add(Conv2D(512, (3, 3), activation='relu', padding='SAME'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(11, activation='softmax'))

# 梯度下降
sgd = SGD(lr=0.001, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

model.load_weights('train_weights.h5')
classes = model.predict_classes(x_test)[0]
print(classes)
