class KNN:
	def __init__(self,x,y,n_neighbors=3,p=2):
		self.n=n_neighbors
		self.p=p
		self.x=x
		self.y=y

	def predict(self,x):
		knn_list=[]
		for i in range(self.n):
			dist=np.linalg.norm(x-self.x[i],ord=self.p)
			knn_list.append((dist,self.y[i]))
		for i in range(self.n,len(self.x)):
			max_index=knn_list.index(max(knn_list, key=lambda x:x[0]))
			dist=np.linalg.norm(x-self.x[i],ord=self.p)
			if knn_list[max_index][0]>dist:
				knn_list[max_index]=[dist,self.y[i]]

		knn=[k[-1] for k in knn_list]
		count_pairs=Counter(knn)
		maxcount=count_pairs.most_common(1)[0][0]
		return maxcount

	def score(self,test_x,test_y):
		right_count=0
		for x,y in zip(test_x,text_y):
			label=self.predict(x)
			if label==y:
				right_count+=1
		return right_count/len(text_y)
