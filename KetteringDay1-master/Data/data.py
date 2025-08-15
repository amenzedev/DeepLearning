import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
import pathlib


def data_provider(img_height, img_width, batch_size, split, mpath=''):

    data_dir = pathlib.Path(mpath + 'dataset')
    data_dir_face = pathlib.Path(mpath + 'dataset/face/')
    image_count = len(list(data_dir_face.glob('*')))
    print(data_dir_face)

    face = list(data_dir_face.glob('*'))
    im1 = PIL.Image.open(str(face[0]))
    # plt.imshow(im1)
    # plt.show()

    data_dir_car = pathlib.Path(mpath + 'dataset/car/')
    image_count = len(list(data_dir_car.glob('*')))
    print(image_count)
    car = list(data_dir_car.glob('*'))
    im2 = PIL.Image.open(str(car[0]))



    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(im1)
    ax[1].imshow(im2)

    plt.show()

    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=split,
        subset='training',
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size
    )

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=split,
        subset='validation',
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size
    )
    print(len(train_ds), len(val_ds))

    return train_ds, val_ds



#data_provider(200, 200, 32, 0.2)