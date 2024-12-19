import streamlit as st
import os
import pandas as pd
import plotly.express as px
from trendyol_scraper import TrendyolScraper
from cleaner import DataCleaner
import tempfile
import shutil
import seaborn as sns
import matplotlib.pyplot as plt

# Configure the Streamlit page
st.set_page_config(page_title="Trendyol Data Visualization", page_icon= "assets/favicon.png" ,layout="wide")

# Sidebar for page selection
page = st.sidebar.selectbox("Select Page", ["Data Visualization", "Cleaned Data"])

# Create two columns for visualizations
col1, col2 = st.columns(2)

# Sidebar inputs for scraping settings
st.sidebar.header("Scraping Settings")
base_url = st.sidebar.text_input(
    "Trendyol Category URL:", 
    "https://www.trendyol.com/cep-telefonu-x-c103498"
)
max_pages = st.sidebar.number_input(
    "Number of Pages:", min_value=1, max_value=200, value=10
)

# Custom button styling for a better UI experience
button_style = """ 
    <style>
        .stButton > button {
            background-color: #1abc9c;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            background-color: #16a085;
        }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# Add a scraping button to the sidebar
if st.sidebar.button("Collect Data"):
    st.sidebar.info("Starting the scraping process...")

    # Create a temporary directory for raw data storage
    temp_dir = tempfile.mkdtemp()
    output_file = os.path.join(temp_dir, "raw_data.csv")

    # Initialize and run the Trendyol scraper
    scraper = TrendyolScraper(base_url=base_url, max_pages=int(max_pages), output_file=output_file)
    scraper.run()

    # If scraping is successful, move to data cleaning
    if os.path.exists(output_file):
        st.sidebar.success("Scraping completed. Cleaning data...")

        # Initialize the data cleaner and clean the scraped data
        cleaner = DataCleaner(output_file)
        cleaned_data = cleaner.clean()

        if cleaned_data is not None:
            st.sidebar.success("Data cleaning completed successfully.")
            
            # Save cleaned data to the session state
            st.session_state.cleaned_data = cleaned_data

# Display content based on the selected page
if page == "Data Visualization":
    if 'cleaned_data' in st.session_state:
        # Filter data: Only include rows with a Rating Count of 75 or higher
        filtered_data = st.session_state.cleaned_data[st.session_state.cleaned_data['Rating Count'] >= 75]

        # Column 1: Brand-focused visualizations
        with col1:
            st.subheader("Brand Analysis")

            # Bar Chart: Average Rating by Brand
            avg_rating = filtered_data.groupby('Product Brand')['Rating Score'].mean().reset_index()
            avg_rating = avg_rating.sort_values(by=['Rating Score', 'Product Brand'], ascending=[False, True])
            fig1 = px.bar(
                avg_rating, x='Product Brand', y='Rating Score', 
                title='Average Rating by Product Brand', 
                labels={'Product Brand': 'Brand', 'Rating Score': 'Average Rating'},
                color='Product Brand', color_discrete_sequence=px.colors.qualitative.Set1
            )
            fig1.update_layout(title_x=0.5, template='plotly_dark', xaxis_tickangle=-45, plot_bgcolor='#194d61')
            st.plotly_chart(fig1, use_container_width=True)

            # Bar Chart: Average Price by Brand
            avg_price = filtered_data.groupby('Product Brand')['Price (TL)'].mean().reset_index()
            avg_price = avg_price.sort_values(by=['Price (TL)', 'Product Brand'], ascending=[False, True])
            fig2 = px.bar(
                avg_price, x='Product Brand', y='Price (TL)', 
                title='Average Price by Product Brand', 
                labels={'Product Brand': 'Brand', 'Price (TL)': 'Average Price (TL)'},
                color='Product Brand', color_discrete_sequence=px.colors.qualitative.Set2
            )
            fig2.update_layout(title_x=0.5, template='plotly_dark', xaxis_tickangle=-45, plot_bgcolor='#194d61')
            st.plotly_chart(fig2, use_container_width=True)

            # Bar Chart: Product Count by Brand
            product_count = filtered_data['Product Brand'].value_counts().reset_index()
            product_count.columns = ['Product Brand', 'Product Count']
            product_count = product_count.sort_values(by='Product Count', ascending=False)
            fig3 = px.bar(
                product_count, x='Product Brand', y='Product Count', 
                title='Product Count by Brand', 
                labels={'Product Brand': 'Brand', 'Product Count': 'Number of Products'},
                color='Product Brand', color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig3.update_layout(title_x=0.5, template='plotly_dark', xaxis_tickangle=-45, plot_bgcolor='#194d61')
            st.plotly_chart(fig3, use_container_width=True)

            # Display a table of top-rated products by brand
            st.subheader("Top Rated Products by Brand")
            top_rated_products = filtered_data.loc[filtered_data.groupby('Product Brand')['Rating Score'].idxmax()]
            top_rated_products = top_rated_products[['Product Brand', 'Product Name', 'Rating Score', 'Price (TL)']]
            st.write(top_rated_products)

        # Column 2: Product-focused visualizations
        with col2:
            st.subheader("Product Analysis")

            # Scatter Plot: Price vs Rating
            fig4 = px.scatter(
                filtered_data, x='Price (TL)', y='Rating Score', 
                color='Product Brand', size_max=10, 
                title='Price vs Rating', 
                labels={'Price (TL)': 'Price (TL)', 'Rating Score': 'Rating'}
            )
            fig4.update_layout(template='plotly_dark', plot_bgcolor='#194d61')
            st.plotly_chart(fig4, use_container_width=True)

            # Pie Chart: Product Share by Brand
            product_share = filtered_data['Product Brand'].value_counts().reset_index()
            product_share.columns = ['Product Brand', 'count']
            product_share = product_share.sort_values(by='Product Brand', ascending=True)
            fig5 = px.pie(
                product_share, names='Product Brand', values='count', 
                title='Product Share by Brand', 
                color='Product Brand', color_discrete_sequence=px.colors.qualitative.Pastel
            )
            fig5.update_layout(title_x=0.5, template='plotly_dark')
            st.plotly_chart(fig5, use_container_width=True)
            
            # Box Plot: Price Distribution by Brand
            fig6 = px.box(
                filtered_data, x='Product Brand', y='Price (TL)', 
                title='Price Distribution by Brand', 
                labels={'Product Brand': 'Brand', 'Price (TL)': 'Price (TL)'},
                color='Product Brand', color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig6.update_layout(template='plotly_dark', xaxis_tickangle=-45, plot_bgcolor='#194d61')
            st.plotly_chart(fig6, use_container_width=True)

            # Correlation Heatmap
            st.subheader("Correlation Analysis")
            fig7, ax7 = plt.subplots(figsize=(8, 6))
            correlation = filtered_data[['Price (TL)', 'Rating Score', 'Rating Count']].corr()
            sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax7, vmin=-1, vmax=1)
            ax7.set_title("Correlation Heatmap", fontsize=16)
            ax7.set_facecolor('#194d61')
            st.pyplot(fig7)

elif page == "Cleaned Data":
    st.markdown("<h1 style='text-align: center; color: #2c3e50;'>Cleaned Data</h1>", unsafe_allow_html=True)
    if 'cleaned_data' in st.session_state:
        # Display the cleaned data in a table
        st.dataframe(st.session_state.cleaned_data, use_container_width=True)
