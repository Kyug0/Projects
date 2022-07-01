import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from scipy import stats
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="MileStone 1",
    layout="centered", #wide, centered
    initial_sidebar_state="expanded", #expanded, wide
    menu_items={
        'Get Help': 'https://karoseriambulance.com/wp-content/uploads/2021/10/Fakta-Kode-Warna-Ambulance-yang-Berbeda-Beda.jpg',
        'Report a bug': "https://i0.wp.com/sinttesis.co.id/wp-content/uploads/2017/11/fantastic-pest-control-895x1024.png?resize=500%2C572&ssl=1",
        'About': "https://64.media.tumblr.com/61b50b5815de107661d5c4cb313a130f/tumblr_inline_psu9wqocyg1uulg0x_540.jpg"
    }
)

 
st.title('Supermarket Data')
selected = st.sidebar.selectbox('Select Page:', options=['Data Visualization', 'Hypothesis Testing'])
df = pd.read_csv('supermarket_sales - Sheet1.csv')
df1 = df.copy()
df1.rename(columns = {'Customer type':'Customer'}, inplace = True)

if selected == 'Data Visualization':
    st.caption('''These are Data Visualisations that are taken from data from a Supermarket. The dataset is one 
    of the historical sales of supermarket company which has recorded in 3 different branches / cities for 3 months 
    data''')
    if st.checkbox('Show raw data'):
            st.subheader('Raw data')
            st.write(df)

    #First Graph
    st.subheader('Product Lines bought by each Gender')
    #Code
    pls = df1[['Product line', 'Gender', 'Quantity']]
    #End Code
    st.text('''This Chart tells us which Product Lines are bought more by each Gender which allows the supermarket to lean in one gender 
    more, if the other one isn't buying as much as the other''')
    if st.checkbox('Show Data of Product Lines bought by each Gender'):
            st.subheader('The data')
            st.write(pls)
    fig = px.histogram(pls, x="Quantity", y="Product line",color='Gender', barmode='group')
    st.plotly_chart(fig)


    #Second Graph
    st.subheader('Most Popular Product Line in each city')
    #Code
    something = df1[['Product line', 'City', 'Quantity']]
    #End Code
    st.text('''This Chart allows the supermarkets to focus more on a Product Line in a specific 
    City to make up sales in the other''')
    if st.checkbox('Show Data of Most Popular Product'):
            st.subheader('The data')
            st.write(something)
    fig2 = px.histogram(something, x="Quantity", y="City",color='Product line', barmode='group')
    st.plotly_chart(fig2)


    #Third Graph
    st.subheader('Payment Method by Total and City')
    #Code
    pay_method = df1[['Payment', 'City', 'Total']]
    #End Code
    st.text('''This Chart allows supermarkets to accurately use promotional events based on Payment 
    Method to benefit themselves''')
    if st.checkbox('Show Data of Payment Method'):
            st.subheader('The data')
            st.write(pay_method)
    fig3 = px.histogram(pay_method, x="Total", y="City",color='Payment', barmode='group')
    st.plotly_chart(fig3)


    #Fourth Graph
    st.subheader('Purchase made sorted by Date and Time')
    #Code
    crowded = df1[['Date', 'Time', 'Total', 'City']]
    crowded = crowded.sort_values(by="Time", ascending=True)
    #End Code
    st.text('''This Chart allows supermarkets to check which time is the most 
    crowded and least crowded in each City. This can help in increasing promos 
    on the least crowded times to boost foot traffic''')
    if st.checkbox('Show Data of Crowdedness'):
            st.subheader('Raw data')
            st.write(crowded)
    city_filter = st.selectbox('Which City?', ('Yangon', 'Naypyitaw', 'Mandalay'))
    selected = crowded[crowded['City'] == city_filter]
    fig4 = px.scatter(selected, x="Time", y="Date")
    st.plotly_chart(fig4)
    
#################################################
else:
    st.header('Hypothesis Testing')
    st.caption('''This page is for Hypothesis Testing a certain data which will be Purchase made by Customer 
    Type sorted with Total / Gross Income / Quantity''')
    st.text('H0 : IF Customer Type = Member, Gross Income is more than the average.')
    st.text('H1 : If Customer Type != Member, Gross Income is less than the average')
    st.text('The purpose of this Hypothesis Testing is to check if a member-ed customer gives us more gross income or not')

    st.subheader('Purchase made by Customer Type sorted with Total / Gross Income / Quantity')
    purchase_type = df1[['Customer', 'Quantity', 'Total', 'gross income']]
    if st.checkbox('Show Data of Hypothesis'):
            st.subheader('The data')
            st.write(purchase_type)
    fig5 = px.histogram(purchase_type, x="Total", y="gross income",color='Customer',barmode='group')
    st.plotly_chart(fig5)
    

    st.header('Analysis')
    st.caption('The analysis was done by Python Code')

    #Central Tendency
    st.subheader('Central Tendency')
    #Code
    mean = purchase_type['gross income'].mean()
    median = purchase_type['gross income'].median()
    modus = purchase_type['gross income'].mode()
    maximum = purchase_type['gross income'].max()
    minimum = purchase_type['gross income'].min()
    #End Code
    st.code('''print('Mean: ', purchase_type['gross income'].mean())
print('Median: ', purchase_type['gross income'].median())
print('Modus: ', purchase_type['gross income'].mode())
print('Maximum: ', purchase_type['gross income'].max())
print('Minimum: ', purchase_type['gross income'].min())''')
    st.text(f'Mean: {mean}')
    st.text(f'Median: {median}')
    st.text(f'Modus: {modus}')
    st.text(f'Maximum: {maximum}')
    st.text(f'Minimum: {minimum}')

    #Outliers
    st.subheader('Removing Outliers')
    #Code
    Q1 = np.percentile(purchase_type['gross income'], 25,
                    interpolation = 'midpoint')
    Q3 = np.percentile(purchase_type['gross income'], 75,
                    interpolation = 'midpoint')
    IQR = Q3 - Q1

    upper = np.where(purchase_type['gross income'] >= (Q3+1.5*IQR))
    lower = np.where(purchase_type['gross income'] <= (Q1-1.5*IQR))
    
    purchase_type.drop(upper[0], inplace = True)
    purchase_type.drop(lower[0], inplace = True)
    #End Code
    st.code('''#membuat quartiles 
Q1 = np.percentile(purchase_type['gross income'], 25,
                   interpolation = 'midpoint')
 
Q3 = np.percentile(purchase_type['gross income'], 75,
                   interpolation = 'midpoint')
IQR = Q3 - Q1

#Melihat size data dengan Outlier backers
print("With Outlier: ", purchase_type.shape)
 
# Upper bound 
upper = np.where(purchase_type['gross income'] >= (Q3+1.5*IQR))
# Lower bound 
lower = np.where(purchase_type['gross income'] <= (Q1-1.5*IQR))
 
#Hilangkan Outliers-nya
purchase_type.drop(upper[0], inplace = True)
purchase_type.drop(lower[0], inplace = True)
 
#Melihat size data tanpa Outlier backers
print("Without Outlier: ", purchase_type.shape)''')
    st.text('With Outlier:  (1000, 4)')
    st.text('Without Outlier:  (991, 4)')

    #Variance
    st.subheader('Variance and Standard Deviation')
    #Code
    vari = purchase_type['gross income'].var()
    stad = purchase_type['gross income'].std()
    #End Code
    st.code('''print('Variance: ', purchase_type['gross income'].var())
print('Standard Deviation: ', purchase_type['gross income'].std())''')
    st.text(f'Variance: {vari}')
    st.text(f'Standard Deviation: {stad}')

    #Numerical Value for Customer
    st.subheader('Putting a Numerical Value for each Customer Type')
    #Code
    refined_purchase = purchase_type.copy()
    refined_purchase.Customer[refined_purchase.Customer == 'Member'] = 1
    refined_purchase.Customer[refined_purchase.Customer == 'Normal'] = 0
    #End Code
    st.code('''refined_purchase = purchase_type.copy()
refined_purchase.Customer[refined_purchase.Customer == 'Member'] = 1
refined_purchase.Customer[refined_purchase.Customer == 'Normal'] = 0''')
    st.text('This allows me to determine the P-Value which will help determine which Hypothesis gets rejected')

    #Grouping Mean
    st.subheader('Grouping the Data to match the Hypothesis')
    st.code('refined_purchase = refined_purchase[refined_purchase["gross income"] >= 15.37]')
    st.text('By doing this, this allows me use it in counting the P-Value as it matches H0 better')

    st.subheader('P-Value')
    #Code
    t_stat,p_val = stats.ttest_rel(refined_purchase['gross income'].sample(200),refined_purchase['Customer'].sample(200))
    #End Code
    st.code('''t_stat,p_val = stats.ttest_rel(refined_purchase['gross income'].sample(200),refined_purchase['Customer'].sample(200))
print('P-value:',p_val)''')
    st.text(f'P-Value: {p_val}')


    st.header('Conclusion')
    st.text('''From the Data above, I can conclude that Hypothesis 0 is rejected because the P-Value is lower than 0.05 (Assuming we use 
the standard Confidence Level = 95%). That means there is no correlation between a Membered and Normal Customer in terms of Gross 
Income for the Supermarket''')