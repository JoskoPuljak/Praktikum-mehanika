import linereg as linrg
import csv
import matplotlib.pyplot as plt
import numpy as np
def r_perp(x):
      n=1.5
      return -(np.sqrt(n**2-(np.sin(x))**2)-np.cos(x))**2/(n**2-1)
with open ("podaci.csv", "r") as csv_file:
        csv_reader=csv.reader(csv_file)
        xy=[[float(line[0]),float(line[1]),float(line[2])] for line in csv_reader]
        x=[np.radians(i[0]) for i in xy]
        y=[-np.sqrt(i[1]/70) for i in xy]
        y_real=[r_perp(i) for i in x]
        plt.scatter(x,y)
        plt.plot(x,y_real)
        
def r_par(x):
       n=1.376
       return (n**2*(np.cos(x))-np.sqrt(n**2-(np.sin(x))**2))/(n**2*(np.cos(x))+np.sqrt(n**2-(np.sin(x))**2))
with open ("podaci2.csv", "r") as csv_file2:
        csv_reader2=csv.reader(csv_file2)
        xy2=[[float(line[0]),float(line[1]),float(line[2])] for line in csv_reader2]
        x2=[np.radians(i[0]) for i in xy2]
        y2=[(-1)**((xy2.index(i)//16)+1)*np.sqrt(i[1]/89) for i in xy2]
        x_real=np.linspace(x2[0],x2[-1],1000)
        y_real2=r_par(x_real)
        plt.scatter(x2,y2)
        plt.plot(x_real,y_real2)
        
        plt.savefig("privremeno.png")
        plt.show()