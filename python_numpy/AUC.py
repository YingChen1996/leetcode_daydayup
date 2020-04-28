#积分做法
auc=0
height=0
for x_i,y_i in each_train_example :
	if y_i==1.0:
		height+=1/(tp+fn)
	else:
		auc+=height*(1/(fp+tn))
return auc

###############################################

import numpy as np 
label_all=np.random.randint(0,2,[10,1]).tolist()
pred_all=np.random.randint((10,1)).tolist()

posNum=len(list(filter(lambda s:s[0]==1, label_all)))
if posNum>0:
	negNum=len(label_all)-posNum
	sorted_pred=sorted(enumerate(pred_all), key=lambda s:x[1])

	posRankSum=0
	for j in range(len(pred_all)):
		if label_all[j][0]==1:
			posRankSum+=list(map(lambda x:x[0], sorted_pred)).index(j)+1
	auc=(posRankSum-posNum*(posNum+1)/2)/(posNum+negNum)

