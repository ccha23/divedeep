import tensorflow_datasets as tfds
import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfjs
import os, datetime, pytz
from tqdm.keras import TqdmCallback
import tensorboard as tb
import numpy as np
import tensorflow.compat.v2 as tf
import numpy as np
from IPython import display
import matplotlib.pyplot as plt
import subprocess, time


# Function to start ollama serve and return the Popen object if successful
def start_ollama_serve(timeout=0.1):
    # Start ollama serve in the background
    proc = subprocess.Popen(
        ["ollama", "serve"], stderr=subprocess.PIPE, start_new_session=True
    )

    # Wait a bit for the service to initialize
    time.sleep(timeout)

    # Check if the process has started successfully
    if proc.poll() is None:  # None means the process is still running
        print("ollama serve started successfully.")
        return proc
    else:
        error_output = proc.stderr.read().decode("utf-8").strip()
        print(
            f"The command 'ollama serve' exited prematurely with exit code {proc.returncode}: {error_output}"
        )

# set the jupyter service prefix to access jupyter-www and tensorboard
JUPYTER_SERVICE_PREFIX = os.environ["JUPYTERHUB_SERVICE_PREFIX"] or "/"
os.environ["TENSORBOARD_PROXY_URL"] = JUPYTER_SERVICE_PREFIX + "proxy/%PORT%/"

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
        tf.keras.layers.Input(shape=(28, 28, 1)),
        tf.keras.layers.Flatten(),
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


log_root = os.path.join(user_home, "log")  # log folder
save_log_params = {'update_freq': 100, 'histogram_freq': 1}
save_model_params = {'save_weights_only': True, 'verbose': 1}
debug_params = {'tensor_debug_mode': "FULL_HEALTH", 'circular_buffer_size': -1}