# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 16:12:42 2014

@author: ankur
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 12:29:43 2014

@author: ankur
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 10:10:05 2014

@author: ankur
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline



energy=np.array([23.938,33.935,39.364,46.372,46.837,48.456,49.635,50.600,52.549,60.172,65.541,66.827,67.856])
heat= np.array([15.749,23.756,28.233,32.289,32.381,33.349,34.130,34.866,36.435,42.674,46.743,47.550,48.189])


#convert them to matrix form
energy_mat = energy[:, np.newaxis]


#need to predict the curve for this data
plot_data = np.array([10.60048659  ,10.78402003 , 12.74295856  ,13.02762266 , 13.3834528,  15.2337695 ,  16.51475798 , 16.85186021,  17.85567575,  19.219067,  19.80712311 , 20.60118615 , 21.00945441,  21.1442953 ,  23.57517695,  25.55658896 , 27.28704709 , 27.44436146,  30.38089646,  33.04025852,  37.16414249 , 44.36314794 , 44.60661066,  45.77897731])
plot_mat = plot_data[:, np.newaxis]

for degree in [1,2,3,4,5,6,7]:
    plt.clf()
    plt.plot(energy, heat, label="ground truth")
    plt.scatter(energy, heat, label="training points")
    model = make_pipeline(PolynomialFeatures(degree), Ridge())
    model.fit(energy_mat, heat)
    y_plot = model.predict(plot_mat)
    #print y_plot, degree,"\nnow tws\n"
    plt.plot(plot_mat, y_plot, label="degree %d" % degree)
    #plt.legend(loc='lower left')
    plt.savefig(str(degree))
 
