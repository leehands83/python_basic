import sys
import tensorflow as tf
import numpy as np

node1 = tf.constant(3.0,tf.float32)
node2 = tf.constant(4.0,tf.float32)

@tf.function
def forward():
    return node1 + node2

out_a = forward()
print(out_a)