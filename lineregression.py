import math as mt
def aritm_sred(lista):
    sum=0
    for i in lista:
        sum+=i
    sredina=sum/len(lista)
    return(sredina)


def stand_dev(lista):
    sum=0
    for i in lista:
        sum+=(i-aritm_sred(lista))**2
    standardna=mt.sqrt(sum/(len(lista)*(len(lista)-1)))
    return(standardna)
import math as mt
import matplotlib.pyplot as plt
def lin_regress(x,y,colour="red",xlabel="x os", ylabel="y os", title="x/y graf",linelegend="graf linearne regresije",scatterlegend="pravi podaci"):
    #koeficijent smjera
    prod_list=[i*j for i,j in zip(x,y)]
    product_mean=art.aritm_sred(prod_list)
    x_square_list=[i**2 for i in x]
    x_square_mean=art.aritm_sred(x_square_list)
    slope=product_mean/x_square_mean
    kx=[slope*i for i in x]

    #standardna devijacija koeficijenta smjera
    y_square_list=[i**2 for i in y]
    y_square_mean=art.aritm_sred(y_square_list)

    Dt_deviation=mt.sqrt((1/len(x))*((y_square_mean/x_square_mean)-slope**2))
    print("Dt = {} \u00B1 {}".format(slope,Dt_deviation ))
    
    plt.plot(x,kx,color=colour)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.scatter(x,y)
    plt.legend([linelegend,scatterlegend])
    plt.show()