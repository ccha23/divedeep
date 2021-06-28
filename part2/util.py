import tensorflow_datasets as tfds
import tensorflow.compat.v2 as tf
import os, datetime, pytz
import tensorboard as tb
import numpy as np
import tensorflow.compat.v2 as tf
from matplotlib import pyplot as plt
import numpy as np
from IPython import display
import matplotlib.pyplot as plt
# produce vector inline graphics
from matplotlib_inline.backend_inline import set_matplotlib_formats
set_matplotlib_formats('svg')

user_home = os.getenv("HOME")  # get user home directory
data_dir = os.path.join(user_home, "data")  # download folder for data

ds, ds_info = tfds.load(
    'mnist',
    data_dir=data_dir,  # download location
    as_supervised=True,  # separate input features and label
    with_info=True,  # return information of the dataset
)

def normalize_mnist(ds):
    """
  Returns:
  MNIST Dataset with image pixel values normalized to float32 in [0,1].
  """
    ds_n = dict.fromkeys(ds.keys())  # initialize the normalized dataset
    for part in ds.keys():
        # normalize pixel values to [0,1]
        ### BEGIN SOLUTION
        ds_n[part] = ds[part].map(
            lambda image, label: (tf.cast(image, tf.float32) / 255, label),
            num_parallel_calls=tf.data.experimental.AUTOTUNE)
        # - `tf.cast(image, tf.float32) / 255` converts each element of `image` 
        #    to a float and then normalize it to within the unit interval [0,1];
        # - `map` applies the conversion to each example in the dataset.
        ### END SOLUTION
    return ds_n


ds_n = normalize_mnist(ds)

def batch_mnist(ds_n):
    ds_b = dict.fromkeys(ds_n.keys())  # initialize the batched dataset
    for part in ds_n.keys():
        ds_b[part] = (
            ds_n[part].batch(
                128)  # Use a minibatch of examples for each training step
            .shuffle(
                ds_info.splits[part].num_examples,
                reshuffle_each_iteration=True)  # shuffle data for each epoch
            .cache()  # cache current elements 
            .prefetch(tf.data.experimental.AUTOTUNE)
        )  # preload subsequent elements
    return ds_b


ds_b = batch_mnist(ds_n)

def create_simple_model():
    tf.keras.backend.clear_session() # clear keras cache. 
                        # See https://github.com/keras-team/keras/issues/7294
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28, 1)),
        tf.keras.layers.Dense(16, activation=tf.keras.activations.relu),
        tf.keras.layers.Dense(16, activation=tf.keras.activations.relu),
        tf.keras.layers.Dense(10, activation=tf.keras.activations.softmax)
    ], 'Simple_sequential')
    return model


model = create_simple_model()


def compile_model(model):
    model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                  optimizer=tf.keras.optimizers.Adam(0.001),
                  metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])
    return model


compile_model(model)


import tqdm.keras
import os, datetime, pytz

fit_params = {'epochs': 6, 'callbacks': [tqdm.keras.TqdmCallback()], 'verbose': 0}
log_root = os.path.join(user_home, "log")  # log folder
save_log_params = {'update_freq': 100, 'histogram_freq': 1}
save_model_params = {'save_weights_only': True, 'verbose': 1}
debug_params = {'tensor_debug_mode': "FULL_HEALTH", 'circular_buffer_size': -1}
