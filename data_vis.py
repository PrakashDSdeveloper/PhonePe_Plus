import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector
import plotly.express as px
import pandas as pd
import folium
from streamlit_folium import st_folium
import geopandas as gpd
import folium
import json
from PIL import Image

my_connection = mysql.connector.connect(host = 'localhost',user = 'root',password='1234')
mycursor = my_connection.cursor()
mycursor.execute('use PhonePe_Pulse_DB')
with st.sidebar:
    selected = option_menu(
        menu_title='PhonePe Pluse',
        options=['Home','Explore','Reports','GeoVisuals','About'],
        icons=['house','book','bar-chart-fill','globe','exclamation-lg'],
        menu_icon="cast", default_index=0, orientation="verical",
        styles={'nav-link':{'font-size':'20px','margin':'-2px','font-color':'#6739b7'},
                'nav-link-selected':{'font-color':'white','background':'#6739b7'}}
    )
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-color: #e1d7f2;
background-size :cover;
}
[data-testid="stSidebar"]{
background-image: url("https://www.phonepe.com/pulsestatic/708/pulse/static/edefed74f5885261b532120218811cfd/2c63f/insurance_thumbnail.png");
background-position :center;

}
[data-testid="stHeader"]{
background-color: #6739b7;
background-position :center;

}
[data-baseweb="tab"]{
background-color: #e1d7f2;
}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
if selected == 'Home':
    st.markdown("# :violet[Phonepe Pulse Data Visualization and Exploration:]")
    st.image('Image\—Pngtree—digital commerce 3d rendering of_6296009.jpg',width=600,)
    st.write('')
    st.write('')
    st.write('PhonePe Pulse highlights trends and insights on digital payments in India. PhonePe Pulse was launched in September 2021 with the aim to demystify data on the Indian digital payments landscape and give back to the ecosystem. Pulse is a novel interactive platform that is India’s goto destination for accurate and comprehensive data on digital payment trends. With over 46%market share, PhonePe’s data is representative of the country’s digital payment habits. With its rich repository of trends, insights, and in-depth analysis, Pulse showcases India’s beat of progress in the digital payment landscape.')
    st.write('')
    st.write('')
    tab1, tab2 = st.tabs(["$ DOMIN $", "$ TECHNOLOGY $"])
    st.write('')
    st.write('')

    with tab1:
        st.header("FinTech")
        st.image("Image\FINTEch.jpg", width=650)
        st.write('Financial technology (better known as fintech) is used to describe new technology that seeks to improve and automate the delivery and use of financial services. ​​​At its core, fintech is utilized to help companies, business owners, and consumers better manage their financial operations, processes, and lives. It is composed of specialized software and algorithms that are used on computers and smartphones. Fintech, the word, is a shortened combination of “financial technology.When fintech emerged in the 21st century, the term was initially applied to the technology employed at the backend systems of established financial institutions, such as banks. From 2018 or so to 2022, there was a shift to consumer-oriented services. Fintech now includes different sectors and industries such as education, retail banking, fundraising and nonprofit, and investment management, to name a few.Fintech also includes the development and use of cryptocurrencies, such as Bitcoin. While that segment of fintech may see the most headlines, the big money still lies in the traditional global banking industry and its multitrillion-dollar market capitalization.')
    with tab2:
        st.header("Technolgy used")
        st.subheader('Github Cloning, Python, Pandas, MySQL,mysql-connector-python, Streamlit, and Plotly.')
   
if selected == 'Explore':
    st.subheader(':violet[Data Visualization for Transaction and User]')
    option_selected = st.selectbox('Amount',['Transaction', 'User'])
    if option_selected == 'Transaction':
        col1,col2,col3,col4 = st.tabs(['Aggregated_Transaction','Map_Transaction','Top_Transaction_District','Top_Transaction_Pincodes'])
        with col1:
            query = mycursor.execute('select State, sum(Count) as Total_Transactions_Count, sum(Amount) as Amount from aggregated_transaction where Year group by State order by Amount')
            datas = mycursor.fetchall()
            states = []
            counts =[]
            amounts = []
            for data in datas:
                states.append(data[0])
                counts.append(int(data[1]))
                amounts.append(int(data[2]))
            fig = px.pie(data,names=states,values=amounts,title="Distribution of Categories State wise Transaction Amount",color_discrete_sequence=px.colors.sequential.RdBu)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(paper_bgcolor='#e1d7f2')
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            query = mycursor.execute('select District_Name, sum(Count) as Total_Transactions_Count, sum(Amount) as Amount from map_transaction where Year group by District_Name order by Amount desc limit 20')
            datas = mycursor.fetchall()
            district = []
            counts =[]
            amounts = []
            for data in datas:
                district.append(data[0])
                counts.append(int(data[1]))
                amounts.append(int(data[2]))
            fig = px.pie(data,names=district,values=amounts,title="Distribution of Categories District wise Transaction Amount",color_discrete_sequence=px.colors.sequential.Agsunset)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(paper_bgcolor='#e1d7f2')
            st.plotly_chart(fig, use_container_width=True)
        with col3:
            query = mycursor.execute("select District, sum(Amount) as Amount, sum(Count) as Count from top_trans_district where Year group by District order by Amount ")
            datas = mycursor.fetchall()
            district = []
            counts = []
            amounts = []
            for data in datas:
                district.append(data[0])
                counts.append(data[1])
                amounts.append(data[2])
            fig = px.pie(data,names=district,values=amounts,title="Distribution of Categories District wise Top Transactions",color_discrete_sequence=px.colors.sequential.Agsunset)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(paper_bgcolor='#e1d7f2')
            st.plotly_chart(fig, use_container_width=True)
        with col4:
            query = mycursor.execute("select District, sum(Amount) as Amount, sum(Count) as Count from top_trans_pincode where Year group by District order by Amount desc limit 20 ")
            datas = mycursor.fetchall()
            district = []
            counts = []
            amounts = []
            for data in datas:
                district.append(data[0])
                counts.append(data[1])
                amounts.append(data[2])
            fig = px.pie(data,names=district,values=amounts,title="Distribution of Categories District wise Top transaction Pincode",color_discrete_sequence=px.colors.sequential.Agsunset)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(paper_bgcolor='#e1d7f2')
            st.plotly_chart(fig, use_container_width=True)
    elif option_selected == 'User':
        col1,col2,col3,col4 = st.tabs(['Aggregated_User','Map_User','Top_User_District','Top_User_Pincode'])
        with col1:
            query = mycursor.execute('select State,sum(Count) as Count from aggregated_user WHERE Year group by State order by Count')
            datas = mycursor.fetchall()
            states = []
            counts =[]
            brand = []
            percentage = []
            for data in datas:
                states.append(data[0])
                counts.append(int(data[1]))
            fig = px.pie(data,names=states,values=counts,title="Distribution of Categories State wise Use Counts",color_discrete_sequence=px.colors.sequential.RdBu)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(paper_bgcolor='#e1d7f2')
            st.plotly_chart(fig, use_container_width=True)         
        with col2:
            query = mycursor.execute('select District, sum(Register_user) as Register_user from map_user WHERE Year group by District order by Register_user desc limit 20')
            datas = mycursor.fetchall()
            district = []
            registered_user = []
            for data in datas:
                district.append(data[0])
                registered_user.append(int(data[1]))
            fig = px.pie(data,names=district,values=registered_user,title="Distribution of Categories District wise User Details",color_discrete_sequence=px.colors.sequential.Agsunset)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(paper_bgcolor='#e1d7f2')
            st.plotly_chart(fig, use_container_width=True)
        with col3:
            query = mycursor.execute('select District, sum(RegisteredUser) as RegisteredUser from top_user_district WHERE Year group by District order by RegisteredUser desc limit 20')
            datas = mycursor.fetchall()
            district = []
            registered_user = []
            for data in datas:
                district.append(data[0])
                registered_user.append(int(data[1]))
            fig = px.pie(data,names=district,values=registered_user,title="Distribution of Categories District wise user Details",color_discrete_sequence=px.colors.sequential.Agsunset)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(paper_bgcolor='#e1d7f2')
            st.plotly_chart(fig, use_container_width=True)
        with col4:
            query = mycursor.execute('select Pincode, sum(RegisteredUser) as RegisteredUser from top_user_pincode WHERE Year group by Pincode order by RegisteredUser desc limit 20')
            datas = mycursor.fetchall()
            district = []
            registered_user = []
            for data in datas:
                district.append(data[0])
                registered_user.append(int(data[1]))
            fig = px.pie(data,names=district,values=registered_user,title="Distribution of Categories Pincode wise",color_discrete_sequence=px.colors.sequential.Agsunset)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(paper_bgcolor='#e1d7f2')
            st.plotly_chart(fig, use_container_width=True)

if selected == 'Reports':
    st.subheader(':violet[Data Visualization for Transaction and User]')
    option_selected = st.selectbox('Amount',['Transaction', 'User'])
    if option_selected == 'Transaction':
        col1,col2,col3 = st.tabs(['Aggregated_Transaction','map_transaction','top_transaction'])
        with col1:
            query = mycursor.execute('select State, sum(Count) as Total_Transactions_Count, sum(Amount) as Amount from aggregated_transaction where Year group by State order by Amount desc limit 20')
            datas = mycursor.fetchall()
            states = []
            counts =[]
            amounts = []
            for data in datas:
                states.append(data[0])
                counts.append(int(data[1]))
                amounts.append(int(data[2]))
            fig = px.bar(data,x=states,y=amounts,title="Distribution of Categories State wise",orientation='v',color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            query = mycursor.execute('select District_Name, sum(Count) as Total_Transactions_Count, sum(Amount) as Amount from map_transaction where Year group by District_Name order by Amount desc limit 20')
            datas = mycursor.fetchall()
            states = []
            counts =[]
            amounts = []
            for data in datas:
                states.append(data[0])
                counts.append(int(data[1]))
                amounts.append(int(data[2]))
            fig = px.bar(data,x=states,y=amounts,title="Distribution of Categories District wise",orientation='v',color_discrete_sequence=px.colors.sequential.Agsunset)
            st.plotly_chart(fig, use_container_width=True)
        with col3:
            query = mycursor.execute('select District, sum(Count) as Total_Transactions_Count, sum(Amount) as Amount from top_trans_district where Year group by District order by Amount desc limit 20')
            datas = mycursor.fetchall()
            states = []
            counts =[]
            amounts = []
            for data in datas:
                states.append(data[0])
                counts.append(int(data[1]))
                amounts.append(int(data[2]))
            fig = px.bar(data,x=states,y=amounts,title="Distribution of Categories District wise",orientation='v',color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig, use_container_width=True)
    if option_selected == 'User':
        col1,col2,col3 = st.tabs(['Aggregated_User','map_User','top_User_district'])
        with col1:
            query = mycursor.execute('select Brands, sum(Count) as Count from aggregated_user where Year group by Brands order by Count desc limit 20')
            datas = mycursor.fetchall()
            states = []
            brand =[]
            counts = []
            for data in datas:
                brand.append(data[0])
                counts.append(int(data[1]))
            fig = px.bar(data,x=brand,y=counts,title="Distribution of Categories State wise",orientation='v',color_discrete_sequence=px.colors.sequential.Agsunset)
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            query = mycursor.execute('select District, sum(Register_user) as Register_user from map_user where Year group by District order by Register_user desc limit 20')
            datas = mycursor.fetchall()
            registered_users =[]
            districts = []
            for data in datas:
                districts.append(data[0])
                registered_users.append(int(data[1]))
            fig = px.bar(data,x=districts,y=registered_users,title="Distribution of Categories District wise",orientation='v',color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig, use_container_width=True)
        with col3:
            query = mycursor.execute('select District, sum(RegisteredUser) as RegisteredUser from top_user_district where Year group by District order by RegisteredUser desc limit 20')
            datas = mycursor.fetchall()
            registered_users =[]
            districts = []
            for data in datas:
                districts.append(data[0])
                registered_users.append(int(data[1]))
            fig = px.bar(data,x=districts,y=registered_users,title="Distribution of Categories District wise",orientation='v',color_discrete_sequence=px.colors.sequential.Agsunset)
            st.plotly_chart(fig, use_container_width=True)

if selected == 'GeoVisuals':
    selection = st.radio( "What you wany to show ",('Transaction Amount', 'Number of Transaction'))
    if selection == 'Transaction Amount':
        st.markdown("## :violet[Transaction Amount State wise display]")
        mycursor.execute("SELECT State, SUM(Count) AS Count, SUM(Amount) AS Amount FROM map_transaction WHERE Year GROUP BY State ORDER BY State")
        datas = mycursor.fetchall()
        state = []
        counts = []
        amounts = []
        for data in datas:
            state.append(data[0])
            counts.append(int(data[1]))
            amounts.append(int(data[2]))
        with open("data/states_india.geojson") as geojson_file:
            geojson_data = json.load(geojson_file)
        code =[]
        for feature in geojson_data['features']:
            code.append(feature['properties']['st_nm'])
        location_df = pd.DataFrame({"State": state, "LocationCode": code})
        state_data = pd.DataFrame({"State": state, "Count": counts, "Amount": amounts})
        merged_data = pd.merge(location_df,state_data)
        fig = px.choropleth(merged_data, geojson=geojson_data,
                            locations="LocationCode",
                            featureidkey="properties.st_nm",
                            color="Amount",
                            width=600,
                            height=750)
        fig.update_geos(fitbounds="locations", visible=False,)
        st.plotly_chart(fig, use_container_width=True)
    if selection == 'Number of Transaction':
        st.markdown("## :violet[Number of Transactions State wise display]")
        mycursor.execute("SELECT State, SUM(Count) AS Count, SUM(Amount) AS Amount FROM map_transaction WHERE Year GROUP BY State ORDER BY State")
        datas = mycursor.fetchall()
        state = []
        counts = []
        amounts = []
        for data in datas:
            state.append(data[0])
            counts.append(int(data[1]))
            amounts.append(int(data[2]))
        with open("data/states_india.geojson") as geojson_file:
            geojson_data = json.load(geojson_file)
        code =[]
        for feature in geojson_data['features']:
            code.append(feature['properties']['st_nm'])
        location_df = pd.DataFrame({"State": state, "LocationCode": code})
        state_data = pd.DataFrame({"State": state, "Count": counts, "Amount": amounts})
        merged_data = pd.merge(location_df,state_data)
        fig = px.choropleth(merged_data, geojson=geojson_data,
                            locations="LocationCode",
                            featureidkey="properties.st_nm",
                            color="Count",
                            width=450,
                            height=500)
        fig.update_geos(fitbounds="locations", visible=False,)
        st.plotly_chart(fig, use_container_width=True)


if selected == 'About':
    st.subheader(":violet[About this project]")
    st.write('')
    st.write('')
    st.write('The result of this project will be a live geo visualization dashboard that displays information and insights from the Phonepe pulse Github repository in an interactive and visually appealing manner. The dashboard will have different dropdown options for users to select different facts and figures to display. The data will be stored in a MySQL database for efficient retrieval and the dashboard will be dynamically updated to reflect the latest data. Users will be able to access the dashboard from a web browser and easily navigate the different visualizations and facts and figures displayed. The dashboard will provide valuable insights and information about the data in the Phonepe pulse Github repository, making it a valuable tool for data analysis and decision-making. Overall, the result of this project will be a comprehensive and user-friendly solution for extracting, transforming, and visualizing data from the Phonepe pulse Github repository')
    st.write("")
    st.write('Video url :https://youtu.be/gy8uW6y2SMw')  
    st.write('Linked In url : www.linkedin.com/in/prakash-t-n-894307282')  
 

    