###Relu
#https://blog.csdn.net/qq_36607894/article/details/99650302
class Relu:
	def __init__(self):
		self.mask=None

	def forward(self,x):
		self.mask=(x<=0)
		out=x.copy()
		out[self.mask]=0
		return out

	def backward(self,dout):
		dout[self.mask]=0
		dx=dout
		return dx


class Sigmoid:
	def __init__(self):
		self.out=None

	def forword(self,x):
		out=1/1+np.exp(-x)

	def backward(self,dout):
		dx=dout*self.out*(1-self.out)
		return dx


def Affine:
	def __init__(self,w,b):
		self.w=w
		self.b=b
		self.x=None
		self.dw=None
		self.db=None

	def forward(self,x):
		self.x=x
		out=np.dot(x,self.w)+self.b
		return out

	def backward(self,dout):
		dx=np.dot(dout,self.w.T)
		self.dw=np.dot(self.x.T,dout)
		self.db=np.sum(dout,axis=0)
		return dx



def softmax(a):
	c=np.max(a)
	exp_a=np.exp(a-c) # 防溢出
	sum_exp_a=np.sum(exp_a)
	y=exp_a/sum_exp_a

def cross_entropy_error(y,t):
	if y.ndim==1:
		t=t.reshape(1,t.size)
		y=y.reshape(1,y.size)

	if t.size==y.size:
		t=t.argmax(axis=1)

	batch_size=y.shape[0]
	return -np.sum(np.log(y[np.arange(batch_size),t]+1e-7))/batch_size


class SoftmaxWithLoss:
	def __init__(self):
		self.loss=None
		self.y=None
		self.t=None

	def forward(self,x,t):
		self.t=t
		self.y=softmax(x)
		self.loss=cross_entropy_error(self.y,self.t)

	def backward(self,dout=1):
		batch_size=self.t.shape[0]
		dy=(self.y-self.t)/batch_size
		return dy

