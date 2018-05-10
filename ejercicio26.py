import numpy as np
import matplotlib.pyplot as plt

p_velocidad= np.random.uniform(35.0,45.0,1000000)
p_theta= np.random.uniform(0,np.pi/2.0,1000000)

g=9.8

def funcion(v0,t,g):
    d=(v0*v0*np.sin(2*t))/g
    return d

 
def funcion2(dis,c,b):
    a=np.where((dis < c) & (dis > b))
    return a

distancia1= funcion(p_velocidad,p_theta,g)

d1= funcion2(distancia1,66.0,56.0)
v1 = p_velocidad[d1]
x1=len(v1)
t1 = np.random.uniform(35.0,45.0,x1)
distancia2= funcion(v1,t1,g)

d2= funcion2(distancia2,120.0,110.0)
v2 = p_velocidad[d2]
x2=len(v2)
t2 = np.random.uniform(35.0,45.0,x2)
distancia3= funcion(v2,t2,g)

d3= funcion2(distancia3,36.0,26.0)
v3 = p_velocidad[d3]
x3=len(v3)
t3 = np.random.uniform(35.0,45.0,x3)
distancia4= funcion(v3,t3,g)

d4= funcion2(distancia4,172.0,182.0)
v4 = p_velocidad[d4]
x4=len(v4)
t4 = np.random.uniform(35.0,45.0,x4)
distancia4= funcion(v4,t4,g)






plt.figure()        
g_d1= plt.hist(d1, bins = 50)
plt.savefig("d1.png")

plt.figure()        
g_d2= plt.hist(d2, bins = 50)
plt.savefig("d2.png")

plt.figure()        
g_d3= plt.hist(d3, bins = 50)
plt.savefig("d3.png")

plt.figure()        
g_d4= plt.hist(d4, bins = 50)
plt.savefig("d4.png")
        

