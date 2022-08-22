# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 03:35:18 2022

@author: chandra shekhar
"""


import numpy as np
import pickle
import streamlit as st
import pandas as pd

st.set_option('deprecation.showPyplotGlobalUse', False)

st.write("""
# Customer CheckIn Prediction App
This app predicts the **Customer CheckIn or Not**!
""")

st.write('---')
st.write('**Description of Dataset**')


st.write('**Nationality** -Nationality of the Customer')           
st.write('**Age**-Age of the customer')
st.write('**DaysSinceCreation**-number of days elapsed between the creation date and the last day of the extraction period')      
st.write ('**AverageLeadTime**  -average number of days elapsed between the customers booking date and arrival date')       
st.write ('**   BookingsCanceled** -customer cancelled booking')     
st.write ('**   BookingsNoShowed**-customer did not cancel but did not show up')  
st.write ('** BookingsCheckedIn**  -customer checked in or not')     
st.write ('** PersonsNights**  ')       
st.write ('** RoomNights **    ')        
st.write ('** DaysSinceLastStay**')       
st.write ('** DaysSinceFirstStay**')      
st.write('** DistributionChannel**')    
st.write('** MarketSegment**      ')   
st.write('** SRHighFloor**-customer requested for higher floor')      
st.write('** SRLowFloor** ')             
st.write('** SRAccessibleRoom**')        
st.write('** SRMediumFloor** ')          
st.write('** SRBathtub**   ')            
st.write('** SRShower**  ')             
st.write('** SRCrib**    ')              
st.write('** SRKingSizeBed**')           
st.write('** SRTwinBed**    ')           
st.write('** SRNearElevator**')          
st.write('** SRAwayFromElevator**')    
st.write('** SRNoAlcoholInMiniBar**')  
st.write('** SRQuietRoom**   ')
st.write('** Totalrevenue**')
  
  
  # Load the Dataset
url='https://github.com/hareeshchandrasekhar/Customer_check_in/blob/main/file1.csv'
df_customer = pd.read_csv(url)
X =df_customer.drop('BookingsCheckedIn',axis=1)
Y = df_customer[['BookingsCheckedIn']]





# Sidebar
# Header of Specify Input Parameters
#st.sidebar.header('Specify Input Parameters')
# st.sidebar.slider('Nationality',int(X.Nationality.min()), int(X.Nationality.max()))
# st.sidebar.slider('Age', int(X.Age.min()), int(X.Age.max()), int(X.Age.mean()))
# st.sidebar.slider('DaysSinceCreation', int(X.DaysSinceCreation.min()), int(X.DaysSinceCreation.max()), int(X.DaysSinceCreation.mean()))
# st.sidebar.slider('AverageLeadTime', int(X.AverageLeadTime.min()), int(X.AverageLeadTime.max()), int(X.AverageLeadTime.mean()))
# st.sidebar.slider('BookingsCanceled', int(X.BookingsCanceled.min()), int(X.BookingsCanceled.max()), int(X.BookingsCanceled.mean()))
# st.sidebar.slider('BookingsNoShowed',int(X.BookingsNoShowed.min()), int(X.BookingsNoShowed.max()), int(X.BookingsNoShowed.mean()))
# st.sidebar.slider('PersonsNights', int(X.PersonsNights.min()), int(X.PersonsNights.max()), int(X.PersonsNights.mean()))
# st.sidebar.slider('RoomNights', int(X.RoomNights.min()), int(X.RoomNights.max()), int(X.RoomNights.mean()))
# st.sidebar.slider('DaysSinceLastStay', int(X.DaysSinceLastStay.min()), int(X.DaysSinceLastStay.max()), int(X.DaysSinceLastStay.mean()))
# st.sidebar.slider('DaysSinceFirstStay', int(X.DaysSinceFirstStay.min()), int(X.DaysSinceFirstStay.max()), int(X.DaysSinceFirstStay.mean()))
# st.sidebar.slider('DistributionChannel', int(X.DistributionChannel.min()), int(X.DistributionChannel.max()), int(X.DistributionChannel.mean()))
# st.sidebar.slider('MarketSegment', int(X.MarketSegment.min()), int(X.MarketSegment.max()), int(X.MarketSegment.mean()))
# st.sidebar.slider('SRHighFloor', int(X.SRHighFloor.min()), int(X.SRHighFloor.max()), int(X.SRHighFloor.mean()))
# st.sidebar.slider('SRLowFloor', int(X.SRLowFloor.min()), int(X.SRLowFloor.max()), int(X.SRLowFloor.mean()))
# st.sidebar.slider('SRAccessibleRoom', int(X.SRAccessibleRoom.min()), int(X.SRAccessibleRoom.max()), int(X.SRAccessibleRoom.mean()))
# st.sidebar.slider('SRMediumFloor', int(X.SRMediumFloor.min()), int(X.SRMediumFloor.max()), int(X.SRMediumFloor.mean()))
# st.sidebar.slider('SRBathtub', int(X.SRBathtub.min()), int(X.SRBathtub.max()), int(X.SRBathtub.mean()))
# st.sidebar.slider('SRShower', int(X.SRShower.min()), int(X.SRShower.max()), int(X.SRShower.mean()))
# st.sidebar.slider('SRCrib', int(X.SRCrib.min()), int(X.SRCrib.max()), int(X.SRCrib.mean()))
# st.sidebar.slider('SRKingSizeBed', int(X.SRKingSizeBed.min()), int(X.SRKingSizeBed.max()), int(X.SRKingSizeBed.mean()))
# st.sidebar.slider('SRTwinBed', int(X.SRTwinBed.min()), int(X.SRTwinBed.max()), int(X.SRTwinBed.mean()))
# st.sidebar.slider('SRNearElevator', int(X.SRNearElevator.min()), int(X.SRNearElevator.max()), int(X.SRNearElevator.mean()))
# st.sidebar.slider('SRAwayFromElevator', int(X.SRAwayFromElevator.min()), int(X.SRAwayFromElevator.max()), int(X.SRAwayFromElevator.mean()))
# st.sidebar.slider('SRNoAlcoholInMiniBar', int(X.SRNoAlcoholInMiniBar.min()), int(X.SRNoAlcoholInMiniBar.max()), int(X.SRNoAlcoholInMiniBar.mean()))
# st.sidebar.slider('SRQuietRoom', int(X.SRQuietRoom.min()), int(X.SRQuietRoom.max()), int(X.SRQuietRoom.mean()))
# st.sidebar.slider('TotalRevenue', float(X.TotalRevenue.min()), float(X.TotalRevenue.max()), float(X.TotalRevenue.mean()))



# loading the saved model
loaded_model = pickle.load(open(r'C:\Users\chandra shekhar\Desktop\NextLabs\Deployment\trained_model.sav', 'rb'))

# creating a function for Prediction

def Customer_CheckIn_prediction(input_data):
    
    input_data=(137,51,150,45,1,0,8,5,151,1074,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,476.30)

    input_data_as_numpy_array=np.asarray(input_data)

    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshaped)

    print(prediction)

    if (prediction[0] == 0):
      return 'The Customer will not CheckIn'
    else:
      return 'The Customer will CheckIn'
    






def main():
    
    
    # giving a title
    st.title('Customer CheckIn Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Nationality = st.text_input('Enter the nationality of the customer')
    Age = st.text_input('Enter customers age')
    DaysSinceCreation= st.text_input('Enter number of days elapsed between the creation date and the last day of the extraction period')
    AverageLeadTime    =st.text_input('Enter average number of days elapsed between the customers booking date and arrival date')
    BookingsCanceled=st.text_input('Enter number of bookings the customer made but subsequently canceled')
    BookingsNoShowed=st.text_input('Enter number of bookings the customer made but didnt show up')
    PersonsNights=st.text_input('Enter total number of persons/nights that the custumer stayed at the hotel')
    RoomNights=st.text_input('Enter  total of room/nights the customer stayed at the hotel')
    DaysSinceLastStay=st.text_input('Enter number of days elapsed between the last day of the extraction and the customers last arrival date (-1 indicates the customer never stayed at the hotel).')
    DaysSinceFirstStay=st.text_input('Enter number of days elapsed between the last day of the extraction and the customers first arrival date (-1 indicates the customer never stayed at the hotel)')
    DistributionChannel=st.text_input('Enter distribution channel usually used by the customer to make bookings at the hotel.')
    MarketSegment    =st.text_input('Enter current market segment of a customer. ')
    SRHighFloor    =st.text_input('Enter whether customer demanded Top Floors')
    SRLowFloor    =st.text_input('Enter whether customer demanded lower floors ')
    SRAccessibleRoom=st.text_input('Enter whether customer usually asks for an accessible room')
    SRMediumFloor=st.text_input('Enter whether customer demanded medium floors ')
    SRBathtub=st.text_input('Enter whether customer requested Bathtub ')
    SRShower=st.text_input('Enter whether customer asks for shower ')
    SRCrib    =st.text_input('Enter whether customer asks for Crib')
    SRKingSizeBed=st.text_input('Enter whether customer asks for KingSizeBed ')
    SRTwinBed=st.text_input('Enter whether customer asks for TwinBed ')
    SRNearElevator=st.text_input('Enter whether customer needs room near elevator ')
    SRAwayFromElevator=st.text_input('Enter whether customer needs room away from elevator ')
    SRNoAlcoholInMiniBar=st.text_input('Enter whether customer needs Bar or not ')
    SRQuietRoom=st.text_input('Enter whether customer can tolerate noise or not')
    TotalRevenue=st.text_input('Enter the total expenses spent by the customer combined on lodging and other expenses ')




    # code for Prediction
    Customer_CheckIn_predict = ''

    # creating a button for Prediction

    if st.button('Customer CheckIn Result'):
         Customer_CheckIn_predict = Customer_CheckIn_prediction([Nationality,Age,DaysSinceCreation,AverageLeadTime,BookingsCanceled,BookingsNoShowed,PersonsNights,RoomNights,DaysSinceLastStay,DaysSinceFirstStay,DistributionChannel,MarketSegment,SRHighFloor,SRLowFloor,SRAccessibleRoom,SRMediumFloor,SRBathtub,SRShower,SRCrib,SRKingSizeBed,SRTwinBed,SRNearElevator,SRAwayFromElevator,SRNoAlcoholInMiniBar,SRQuietRoom,TotalRevenue])
    
    
    st.success(Customer_CheckIn_predict)




if __name__ == "__main__":
       main()




