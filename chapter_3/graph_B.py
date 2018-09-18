import tensorflow as tf
import numpy as np

a = tf.constant(90)
b = tf.constant(100)
c = tf.multiply(a, b)

d = tf.sin(tf.cast(c, tf.float32))

e = tf.divide(tf.cast(d, tf.int32), b)

with tf.Session() as sess:
	fetches = [a, b, c, d, e]
	outs = sess.run(fetches)

sess.close()

print("outs = {}".format(outs))