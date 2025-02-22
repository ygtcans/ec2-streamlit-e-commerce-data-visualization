import streamlit as st

st.set_page_config('Hello Forum', initial_sidebar_state='collapsed')

st.markdown(
    """
    <style>
    [data-testid="stHeader"]{
        display: none
    }
    [data-testid="stSidebarNavLink"] {
        display: none
    }
    [data-testid="stSidebar"] {
        display: none
    }

    [data-testid="stSidebarCollapsedControl"] {
        display: none
    }
    .st-emotion-cache-yw8pof {
        width: 90%;
        max-width: initial;
    }
    </style>
    """, unsafe_allow_html=True)



button_style = """ 
    <style>
        .stButton > button {
            background-color: #2e2d2d;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px 20px;
            width: 140px;
        }
        .stButton > button:hover {
            background-color: #191919;
            color: white;
        }
    </style>
"""
# Custom CSS to center the title
st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
    }
    .st-emotion-cache-1104ytp h1{
        margin-top: -130px;
        margin-bottom: 40px;
        
    </style>
    """, unsafe_allow_html=True)
# Main title with custom class for centering and space
st.markdown('<h1 class="centered-title">Welcome to My Portfolio</h1>', unsafe_allow_html=True)


# Split the page into two columns
col1, col2, col3 = st.columns([1, 0.15,  1])

# First column (Introduce yourself and list your project)
with col1:
    st.header("About Me")
    st.write("Hello, I'm Yiğitcan Dursun. I'm a Software Engineer and Data Engineer with a passion for solving problems through technology and continuously learning new things. I graduated from the Software Engineering department at Kırklareli University with a GPA of 3.78 out of 4, and during my internships at Luxoft, I gained valuable experience in Python, SQL, AWS, and various data engineering tools.In addition to my technical skills, I enjoy staying up to date with the latest developments in the tech world and continuously discovering new concepts. I also had the opportunity to study abroad in Poland through the Erasmus+ program, where I completed the semester with a GPA of 4.90 out of 5. This experience contributed greatly to both my personal and professional growth.If you’d like to get in touch with me, feel free to reach out anytime.")

    # Separator after Introduction
    st.html(
    '''
        <div class="divider-horizontal-line"></div>
        <style>
            .divider-horizontal-line {
                border-top: 2px solid rgba(49, 51, 63, 0.2);
                width: 100%;  /* Full width */
                margin: auto;
            }
        </style>
    ''')

    st.header("Projects")
    
    # Project 1
    st.subheader(" 1 - E-Commerce Data Visualization with Streamlit Hosted on AWS EC2")
    st.write("This project features a web scraper designed to collect product data from Trendyol, initially focused on the mobile phone category but also adaptable to other categories. The collected data goes through a cleaning process, followed by visualizations of both the raw and cleaned data. The scraping, cleaning, and visualization tasks are handled by separate Python modules, and the results can be interactively explored using Streamlit for data analysis.")
    st.markdown(button_style, unsafe_allow_html=True)
    if st.button("Go to Project", type="tertiary"):
        st.switch_page("pages/streamlit_data_visualization.py")

# Second column (AI chatbot placeholder)
with col2:
# Custom HTML and CSS to create a vertical divider that switches to horizontal on smaller screens
    st.html(
    '''
        <div class="divider-vertical-line"></div>
        <style>
            .divider-vertical-line {
                border-left: 2px solid rgba(49, 51, 63, 0.2);
                height: 600px;
                margin: auto;
            }

            /* Media query for smaller screens */
            @media screen and (max-width: 800px) {
                .divider-vertical-line {
                    border-left: none;
                    border-top: 2px solid rgba(49, 51, 63, 0.2);  /* Make it horizontal */
                    height: 2px;
                    width: 100%;
                    margin: 0;
                }
            }
        </style>
    ''')


with col3:
    st.header("AI Chatbot")
    st.write("AI Chatbot coming soon.")
