import linereg as linrg
import csv
import matplotlib.pyplot as plt
import numpy as np
linrg.najmanji_kvadrat_lite("podaci.csv",colour="red",xlabel=r'$\Delta T$ [K]', ylabel=r'$l-l_0$ [m]', title='Ovisnost duljine alumijiske šipke o promjeni temperature',linelegend="graf linearne regresije",scatterlegend="podaci")
#linrg.najmanji_kvadrat_lite("podaci2.csv",colour="blue",xlabel=r'$\Delta T$ [K]', ylabel=r'$\Delta l$ [m]', title='Ovisnost duljine čelične  šipke o promjeni temperature',linelegend="graf linearne regresije",scatterlegend="podaci")
#linrg.najmanji_kvadrat_lite("podaci3.csv",colour="green",xlabel=r'$\Delta T$ [K]', ylabel=r'$\Delta l$ [m]', title='Ovisnost duljine mjedene šipke o promjeni temperature',linelegend="graf linearne regresije",scatterlegend="podaci")
#linrg.najmanji_kvadrat_lite("podaci4.csv",colour="orange",xlabel=r'$\Delta T$ [K]', ylabel=r'$\Delta l$ [m]', title='Ovisnost duljine bakrene šipke o promjeni temperature',linelegend="graf linearne regresije",scatterlegend="podaci")