import csv
import matplotlib.pyplot as plt
with open("podaci.csv", "r") as f:
    reader = csv.reader(f)
    x = []
    y = []
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))
plt.scatter(x, y, color='blue', label='Podaci')
plt.xlabel(r'$\lambda$ [nm]',fontsize=14)       
plt.ylabel(r'$n$',fontsize=14)
plt.title('Ovisnost indeksa loma o valnoj duljini svjetlosti',fontsize=18)
plt.legend(["Podaci"], fontsize=10)
plt.show()        
plt.savefig("scatter_plot.png")