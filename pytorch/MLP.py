import torch
class TwoLayer(torch.nn.Module):
	def __init__(self,D_in,H,D_out):
		super(TwoLayer,self).__init__()
		self.linear1=torch.nn.Linear(D_in,H)
		self.linear2=torch.nn.Linear(H,D_out)

	def forward(self,x):
		h_relu=self.linear1(x).clamp(min=0)
		y_pred=self.linear2(h_relu)
		return y_pred


N=64
D_in=1000
D_out=10
D=100
x=torch.randn(N,D_in)
y=torch.randn(N,D_out)
Model=TwoLayer(D_in,H,D_out)
optimizer=torch.optim.SGD(model.parameters(),lr=0.001)
for i in range(500):
	y_pred=model(x)
	loss=torch.nn.functional.mse_loss(y_pred,y)
	loss.backward()
	optimizer.step()
	optimizer.zero_grad()
	