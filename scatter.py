import csv
import matplotlib.pyplot as plt
import linereg as linrg

linrg.najmanji_kvadrat_lite("podaci3.csv",colour="blue",xlabel=r"$T$(K)", ylabel=r"$V$(m$^3$) ", title="Ovisnost volumena plina o temperaturi",linelegend="graf linearne regresije",scatterlegend="pravi podaci")   
