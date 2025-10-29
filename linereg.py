import math as mt
import csv
import matplotlib.pyplot as plt
import scipy.optimize as opt
import numpy as np
def aritm_sred(lista):
    sum=0
    for a in lista:
        sum=sum + a
    sredina=sum/len(lista)
    return(sredina)
def najmanji_kvadrat(file,colour="red",barcolour="black", xlabel="x os", ylabel="y os", title="x/y graf",linelegend="graf linearne regresije",scatterlegend="pravi podaci"):
    with open (file, "r") as csv_file:
        csv_reader=csv.reader(csv_file)
        xy=[[float(line[0]),float(line[1]),float(line[2])] for line in csv_reader]
        #x=[i[0] for i in xy]
        x=[mt.log(i[0]) for i in xy]
        y=[i[1] for i in xy]
        yerror=[i[2] for i in xy]
        x_mean=aritm_sred(x)
        y_mean=aritm_sred(y)
        product=[i*j for i,j in zip(x,y)]
        product_mean=aritm_sred(product)
        xsquaredlist=[i**2 for i in x]
        xsquaredmean=aritm_sred(xsquaredlist)

        koeficijent_smjera=(product_mean-(x_mean*y_mean))/(xsquaredmean-(x_mean**2))
        odsjecak=y_mean-koeficijent_smjera*x_mean
        kx=[koeficijent_smjera*i for i in x]
        graf=[i + odsjecak for i in kx]

        plt.plot(x,graf,color=colour)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.errorbar(x,y,color=barcolour, yerr=[abs(x) for x in yerror], fmt='o', barsabove=True, capsize=5)
        #plt.scatter(x,y,color="black")
        plt.legend([linelegend,scatterlegend])
        plt.savefig("graf najmanjeg kvadrata.png")
        plt.show()

        ysquaredlist=[i**2 for i in y]
        ysquaredmean=aritm_sred(ysquaredlist)
        print("a=",koeficijent_smjera)
        print("b=",odsjecak)
        sigma_a=mt.sqrt(1/len(x)*((ysquaredmean-(y_mean**2))/(xsquaredmean-(x_mean**2))-(koeficijent_smjera**2)))
        sigma_b=sigma_a*mt.sqrt(xsquaredmean-(x_mean**2))
        print("pogreška a=",sigma_a)
        print("pogreška b=",sigma_b)
def najmanji_kvadrat_lite(file,colour="red",xlabel="x os", ylabel="y os", title="x/y graf",linelegend="graf linearne regresije",scatterlegend="pravi podaci"):
    with open (file, "r") as csv_file:
        csv_reader=csv.reader(csv_file)
        xy=[[float(line[0]),float(line[1])] for line in csv_reader]
        x=[mt.radians(i[0]) for i in xy]
        y=[(i[1]/1000)*9.81*0.20 for i in xy]
        x_mean=aritm_sred(x)
        y_mean=aritm_sred(y)
        product=[i*j for i,j in zip(x,y)]
        product_mean=aritm_sred(product)
        xsquaredlist=[i**2 for i in x]
        xsquaredmean=aritm_sred(xsquaredlist)
        ysquaredlist=[i**2 for i in y]
        ysquaredmean=aritm_sred(ysquaredlist)

        koeficijent_smjera=(product_mean/xsquaredmean)
        sigma_a=mt.sqrt((1/len(x))*((ysquaredmean/xsquaredmean)-(koeficijent_smjera**2)))
        kx=[koeficijent_smjera*i for i in x]

        plt.plot(x,kx,color=colour)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.scatter(x,y,color=colour)
        plt.legend([linelegend,scatterlegend])
        plt.savefig("grafkvadrata2.png")
        plt.show()

        
        print("a=",koeficijent_smjera)
        
        print("pogreška a=",sigma_a)
        
def stand_dev(lista):
    sum=0
    for i in lista:
        sum+=(i-aritm_sred(lista))**2
    standardna=mt.sqrt(sum/((len(lista)-1)*len(lista)))
    return(standardna)
def plot(file,colour="red",xlabel="x os", ylabel="y os", title="x/y graf",linelegend="graf ovisnosti",scatterlegend="pravi podaci"):
    with open (file, "r") as csv_file:
        csv_reader=csv.reader(csv_file)
        xy=[[float(line[0]),float(line[1])] for line in csv_reader]
        x=[i for i in xy]
        y=[y for i in xy]
        plt.plot(x,graf,color=colour)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.scatter(x,y,color=colour)
        plt.legend([linelegend,scatterlegend])
        plt.savefig("graf.png")
        plt.show()
def sci_fitting(file,colour="red",barcolour="black",xlabel="x os", ylabel="y os", title="x/y graf",linelegend="graf ovisnosti",scatterlegend="pravi podaci"):
    with open (file, "r") as csv_file:
        csv_reader=csv.reader(csv_file)
        xy=[[float(line[0]),float(line[1]),float(line[2])] for line in csv_reader]
        x=[np.log(i[0]) for i in xy]
        y=[i[1] for i in xy]
        yerror=[i[2] for i in xy]
        def func(x,a,b):
            return a*x + b
        popt, pcov = opt.curve_fit(func, x, y)
        print("a=",popt[0])
        print("b=",popt[1])
        perr = np.sqrt(np.diag(pcov))
        print("pogreška a=",perr[0])
        print("pogreška b=",perr[1])
        #print(*popt)
        plt.plot(x, [func(i,popt[0],popt[1]) for i in x], color=colour)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.errorbar(x,y,yerr=[abs(x) for x in yerror],fmt='o',color=barcolour, barsabove=True, capsize=5)
        plt.legend([linelegend,scatterlegend])
        plt.savefig("graf scipy.png")
        plt.show()

