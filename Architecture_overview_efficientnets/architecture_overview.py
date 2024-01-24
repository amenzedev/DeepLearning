import tensorflow as tf

IMG_SHAPE = (224, 224, 3)

model0 = tf.keras.applications.EfficientNetB0(input_shape=IMG_SHAPE,include_top=False, weights="imagenet")

tf.keras.utils.plot_model(model0)
model0.summary()