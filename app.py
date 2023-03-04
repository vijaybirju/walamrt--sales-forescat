import streamlit as st 
import pickle 
import datetime 
import pandas as pd

#step 1
def extract_week(df):
    Date='Date' 
    df[Date] = pd.to_datetime(df[Date], infer_datetime_format=True) 
    df['week'] = pd.DatetimeIndex(df[Date]).week 
    df['month'] = pd.DatetimeIndex(df[Date]).month 
    df['year'] = pd.DatetimeIndex(df[Date]).year
    return df

#step 2
def maping_type(df):
    # map Type 
    df['Type'] = df['Type'].map({'A':'1',
                                'B':'2',
                                'C':'3'})
    return df

#step 3
def convert_to_int(df):
    ## convert them into integer  
    df['Type']=df['Type'].astype(int)
    df['IsHoliday']=df['IsHoliday'].astype(int)
    return df

#step 4
def input_col_sel(df): 
    input_col = ['Store', 'IsHoliday', 'Type', 'Size', 'week','Dept','year']
    #df.drop(columns=temp3,inplace=True)
    return df[input_col]



pipe = pickle.load(open('pipe.pkl','rb')) 
df = pickle.load(open('train.pkl','rb'))
st.title("walmart-sales-predictor")


#store
store = st.selectbox('Store',df['Store'].unique())

#Dept
Dept = st.selectbox('Dept',df['Dept'].unique())

#Date
Date =st.date_input( "When to predict", datetime.date(2011,11,11))

#IsHoliday
IsHoliday = st.selectbox('IsHoliday',[True,False])

#Type
Type = st.selectbox('Type',["A","B","C"])

#Size
Size = st.number_input("Size" )

if st.button("Predict Sales Amount"): 
    query = pd.DataFrame({"Store":store,'Dept':Dept,'Date':Date,'IsHoliday':IsHoliday,'Type':Type,'Size':Size}, index=[0]) 
    st.title(f'Predicted sales Amount{pipe.predict(query)}')

