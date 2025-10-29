import linereg as linrg
import csv
import numpy as np
linrg.najmanji_kvadrat("podaci7.csv","purple","black","log(n)","log(L))/m","Ovisnost mase o duljini","graf ovisnosti","pravi podaci")
with open("podaci6.csv","r") as f:
     csv_reader=csv.reader(f)
     for line in csv_reader:
          average=linrg.aritm_sred([np.log(float(line[1])),np.log(float(line[2]))])
          error=linrg.stand_dev([np.log(float(line[1])),np.log(float(line[2]))])
          print(line[0],",",average,",",error)
#linrg.sci_fitting("podaci3.csv","blue","black","log(n)","log(m)/kg","log(n)/log(m) graf","graf ovisnosti","pravi podaci")