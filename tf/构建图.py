import tensorflow as tf
g=tf.graph()
with g.as_default():
	input_data=tf.placeholder(tf.float32,[None,2],'input_data')
	input_label=tf.placeholder(tf.float32,[None,2],'input_label')
	W1=tf.Variable(tf.truncated_normal([2,2]),name='W1')
	B1=tf.Variable(tf.zeros([2]),name='B1')
	output=tf.add(tf.matmul(input_data,W1),B1,name='output')
	cross_entropy=tf.nn.softmax_cross_entropy_with_logits(logits=output,labels=input_label)
	train_step=tf.train.AdamOptimizer().minimize(cross_entropy,name='train_step')
	initer=tf.global_variables_initializer()
	