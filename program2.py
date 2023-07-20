import numpy as np
import matplotlib.pyplot as plt
import random
class PythonGraph2:
    def graphPlot():
        axis=np.random.randint(10,90,30)
        axis_2=np.array(['vhaT', 'WFiO', 'tqqW', '36RC', 'ZrSZ', 'Mg5I', 'lUHw', 'ugZj', 'vsae', 'R0kr', 'ZSkG', 'N9ox', 'BCdG', 'gYRE', 'F5s1', 'umpl', 'MnpD', 'XkmX', 'erZy', 'tlKt', '4RKu', 'rW9m', 'eU35', 's9ur', '6XV5', 'EBgM', '4wUI', 'qiL1', '73nE', 'ISA3'])
        explode_array=np.zeros(26)
        explode_array2=np.array([1,1,1,1])
        explode_array3=np.concatenate((explode_array,explode_array2),axis=None)
        # explode_array2=np.array()
        plt.pie(axis,labels=axis_2,shadow=True,explode=explode_array3)
        plt.legend(axis,title="Techno India",loc='upper left')
        plt.figure(figsize=(100,20))
        plt.show()
PythonGraph2.graphPlot()