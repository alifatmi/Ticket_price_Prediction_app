# imporitng the libraires
from re import X
import streamlit as st
import joblib
save=joblib.load('save.joblib')

st.title('Flight prediction app')
left, right=st.columns(2)


# booking date
date=st.date_input('enter the ticket booking date')
# split the date into the parts
day=date.day
month=date.month
year=date.year
st.write('you ticket booking date is',date)

# departure date
date=st.date_input('enter the date of departure')
# converting to parts
depart_day=date.day
depart_month=date.month
depart_year=date.year
st.write('your departure date is',date)

# ba
beg_peaice= left.slider('bag peaice',min_value=0,max_value=2,value=1,step=1  )
beg_weight= left.selectbox('bag weight',options=[0,15,20,35,32,40,45]  )

refund=right.selectbox('D you want to refund the ticket',options=['yes','No'])
# conveting to the digits
if refund == 'yes':
    refund=1
else:
    refund=0

# converting to digits
airline=right.selectbox('Which airline you want to travek',options=['alpha','gamma','beta','omega'])
if airline=='alpha':
    airline=0
elif airline=='gamma':
    airline=1
elif airline=='beta':
    airline=2
else:
    airline=3




# predict the results
submit = st.button('Predict')

if submit:
    pred=save.predict([[airline,refund,beg_weight,beg_peaice,day,month,year,depart_day,depart_month,depart_year]])
    st.write('your ticket price will be:',pred)
    
