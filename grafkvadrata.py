import linereg as linrg
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

with open ("podaci4.csv", "r") as csv_file:
        csv_reader=csv.reader(csv_file)
        xy=[[float(line[0]),float(line[1]),float(line[2]),float(line[3])] for line in csv_reader]
        x_data=[(i[0]) for i in xy]
        y_data=[i[1]/1000 for i in xy]
        x2_data=[(i[2]) for i in xy]
        y2_data=[i[3]/1000 for i in xy]

def exponential_model(x,a,b):
       Iks=0.0035+0.0003*(np.exp(4.404))*((75/100)**(-1.903))
       return Iks-a*(np.exp(b*x)-1)
fit_params,covariance_matrix=curve_fit(exponential_model, x_data, y_data,p0=(0.0035,3))
a_fit, b_fit = fit_params
a_error, b_error= np.sqrt(np.diag(covariance_matrix))
x_fit = np.linspace(min(x_data), max(x_data), 200)
y_fit = exponential_model(x_fit, a_fit, b_fit)
print([a_fit, b_fit])
print([a_error, b_error])
plt.scatter(x_data,y_data,color="black")
plt.plot(x_fit,y_fit,color="cyan")
plt.ylabel("I[A]",fontsize=14)
plt.xlabel("U[V]",fontsize=14)
plt.title("Ovisnost struje o naponu",fontsize=18)
fit_params2,covariance_matrix2=curve_fit(exponential_model, x2_data, y2_data,p0=(0.0035,3))
a_fit2, b_fit2 = fit_params2
a_error2, b_error2= np.sqrt(np.diag(covariance_matrix2))
x_fit2 = np.linspace(min(x2_data), max(x2_data), 200)
y_fit2 = exponential_model(x_fit2, a_fit2, b_fit2)
plt.scatter(x2_data,y2_data,color="gray")
plt.plot(x_fit2,y_fit2,color="lime")
plt.legend(["podaci za T=33°C","regresija za T=33°C","podaci za T=45°C","regresija za T=45°C"])
plt.savefig("privremeno2.png")
plt.show()

print([a_fit2, b_fit2])
print([a_error2, b_error2])