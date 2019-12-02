import matplotlib.pyplot as plt,matplotlib.animation as ani
import numpy as np

n,m=2,5; lr=np.random.rand(m)*0.1;
o=np.random.rand(n,1)
w=np.random.rand(n,n); y=w@o;
x=o+(np.random.rand(m,n,1)*2-1)*0.5
ex,ey=[],[]

fg,(ax,ay)=plt.subplots(2,1);
for i in range(1000):
 #for l,_ in zip(lr,x): _-=l*w@(w@_-y);
 x-=((w@(w@x-y)).reshape(m,n)*lr.reshape(m,1)).reshape(m,n,1)
 #print(np.sum((x-o).reshape(m,2)**2,axis=1))#_=(x-o).reshape(m,2); _*=_; print(_,np.sum(_,axis=1))
 ex.append(np.sum((  x-o).reshape(m,2)**2,axis=1))
 ey.append(np.sum((w@x-y).reshape(m,2)**2,axis=1))

for _ in zip(*ex): ax.plot(_);
for _ in zip(*ey): ay.plot(_);
#t=np.linspace(0,2*np.pi,100)
#plt.plot(t,np.sin(t),t,np.cos(t))
#plt.plot(t,np.sin(t));	plt.plot(t,np.cos(t))
#plt.plot(np.sin(t));	plt.plot(np.cos(t))

plt.show()

#a=np.array([[[1],[2]],[[3],[4]]])#.reshape(2,2)
#a=np.array([1,2]);
#print(a**2);
#print(a,np.sum(a,axis=1).reshape(2))
#w=np.array([[1,2],[3,4]]); x=np.array([[[1],[2]],[[3],[4]],[[5],[6]]]); lr=np.array([1,2,3]); print(w@x,((w@x).reshape(3,2)*lr.reshape(3,1)).reshape(3,2,1))