import tensorflow as tf 
with tf.name_scope('input'):
	x=tf.placeholder(tf.float32,[None,in_unit])
	y=tf.placeholder(tf.float32,[None,out_unit])
	keep_prob=tf.placeholder(tf.float32)

with tf.name_scope('hidden_layer'):
	w1=tf.Variable(tf.random_normal([in_unit,h_unit]))
	b1=tf.Variable(tf.zeros([h_unit])+0.01)
	hidden1=tf.nn.relu(tf.matmul(x,w1)+b1)
	hidden1_dropout=tf.nn.dropout(hidden1,keep_prob)

with tf.name_scope('output_layer'):
	w2=tf.Variable(tf.random_normal([h_unit,out_unit]))
	b2=tf.Variable(tf.zeros([out_unit])+0.01)
	y_pred=tf.nn.softmax(tf.matmul(hidden1_dropout,w2)+b2)

with tf.name_scope('loss'):
	loss_=tf.losses.log_loss(y_pred,y)

with tf.name_scope('train'):
	train=tf.train.Adam(0.01).minimize(loss)


init=tf.global_variables_initializer()
with tf.Session() as sess:
	sess.run(init)
	for i in range(3000):
		loss_val,_=sess.run([loss_,train],feed_dict={x:np.random.randn((N,in_units)),y:np.random.randn(N,out_unit),keep:0.5})
