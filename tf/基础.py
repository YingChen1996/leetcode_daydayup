import tensorflow as tf 
x=tf.placeholder(dtype=tf.float32,shape=[],name='x')
y=tf.placeholder(dtype=tf.float32,shape=[],name='y')
z=x*y
with tf.Session() as sess:
	prod=sess.run(z,feed_dict={x:1,y:5.2})
	print(prod)



import tensorflow as tf
a=tf.Variable(2.)
b=tf.Variable(3.)
with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	print(sess.run(a*b))


