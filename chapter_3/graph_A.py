import tensorflow as tf

a = tf.constant(5)
b = tf.constant(2)
c = tf.multiply(a, b)
d = tf.add(b, a)
e = tf.subtract(d, c)
f = tf.add(d, c)
g = tf.divide(f, e)

sess = tf.Session()
outs = sess.run(g)

sess.close()

print("outs = {}".format(outs))