N=64
D_in=1000
H=100
D_out=10

x=np.random.randn(N,D_in)
y=np.random.randn(N,D_out)
w1=np.random.randn(D_in,H)
w2=np.random.randn(H,D_out)
learning_rate=1e-6

for i in range(500):
	h=x.dot(x,w1)
	h_relu=np.maximum(h,0)
	y_pred=h_relu.dot(w2)
	loss=np.square(y_pred,y).sum()

	grad_y_pred=2*(y_pred-y)
	grad_w2=h_relu.T.dot(grad_y_pred)
	grad_h_relu=grad_y_pred.dot(w2.T)
	grad_h=grad_h_relu.copy()
	grad_h[h<0]=0
	grad_w1=x.T.dot(grad_h)
	w1-=learning_rate*grad_w1
	w2-=learning_rate*grad_w2
	