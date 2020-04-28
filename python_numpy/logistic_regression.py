####logistic regression python implement
#https://github.com/lawlite19/MachineLearning_Python#%E4%B8%80%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92

def costfunction(initial_theda,X,y,initial_lambda):
	m=len(y)
	J=0
	h=sigmoid(np.dot(X,initial_theda))
	theda1=initial_theda.copy()
	theda1[0]=0

	tmp=np.dot(np.transpose(theda1),theda1)
	J=(-np.dot(np.transpose(y),np.log(h))-np.dot(np.transpose(1-y),np.log(1-h))+temp*initial_lambda/2)/m
	return J

def gradient(initial_theda,X,y,initial_lambda):
	m=len(y)
	grad=np.zeros(initial_theda.shape[0])

	h=sigmoid(np.dot(X,initial_theda))
	theda1=initial_theda.copy()
	theda1[0]=0

	grad=np.dot(np.transpose(X),h-y)/m+initial_lambda/m*theda1
	return grad

def sigmoid(z):
	h=np.zeros(len(z),1)
	h=1.0/(1.0+np.exp(z))
	return h