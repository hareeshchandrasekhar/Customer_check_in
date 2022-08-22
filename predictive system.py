# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 02:54:49 2022

@author: chandra shekhar
"""

import numpy as np
import pickle

##loading the saved model
loaded_model=pickle.load(open(r'C:\Users\chandra shekhar\Desktop\NextLabs\Deployment\trained_model.sav','rb'))


input_data=(137,51,150,45,1,0,8,5,151,1074,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,476.30)

input_data_as_numpy_array=np.asarray(input_data)

input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

prediction=loaded_model.predict(input_data_reshaped)

print(prediction)

if(prediction[0]==0):
    print('The Customer will not CheckIn')
else:
    print('The Customer will CheckIn')