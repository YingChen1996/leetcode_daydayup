import numpy as np 
import pandas as pd 

def find_closest_center(x,center):
	m=x.shape[0]
	k=center.shape[0]
	idx=np.zeros(m)
	for i in range(m):
		min_dist=10000000
		for j in range(k):
			dist=np.sum((x[i,:]-center[j,:])**2)
			if dist<min_dist:
				min_dist=dist
				idx[i]=j
	return idx

def compute_center(x, idx, k):
	m,n=x.shape
	center=np.zeros((k,n))
	for i in range(k):
		indices=np.where(idx==i)
		center[i,:]=(np.sum(x[idx,:],axis=0)/len(indices[0])).ravel()
	return center

def run_kmeans(x,initial_center,max_iter):
	m,n=x.shape
	k=initial_center.shape[0]
	idx=np.zeros(m)
	center=initial_center
	for i in range(max_iter):
		idx=find_closest_center(x,center)
		center=compute_center(x,idx,k)
	return idx,center