# E-Commerce Data Visualization with Streamlit Hosted on AWS EC2


This project consists of a web scraper for collecting product data from Trendyol's mobile phone category, followed by a data cleaning process, and visualizations of the scraped and cleaned data. The scraping, cleaning, and visualization processes are handled by different Python modules, and the results can be analyzed using Streamlit for interactive data exploration.

## Project Structure

```plaintext
├── src/
│   ├── cleaner.py               # Data cleaning logic
│   ├── trendyol_scraper.py      # Web scraping logic
│   └── streamlit_data_visualization.py  # Streamlit app for data visualization
├── assets/
│   └── favicon.png              # Favicon for Streamlit app
├── data/
│   └── raw_data.csv             # Raw scraped data (generated during scraping)
├── requirements.txt             # List of required packages
└── README.md                    # This file
```

## Features

### 1. Web Scraping
- The `trendyol_scraper.py` script is designed to scrape product data from Trendyol's mobile phone category.
- It retrieves essential information about each product, such as:
  - Brand
  - Name
  - Description
  - Price
  - Rating
  - Number of reviews
  - Link to the product page
- The scraping process supports scraping multiple pages concurrently to improve performance.

### 2. Data Cleaning
- The `cleaner.py` script performs the following data cleaning steps:
  - Formats numeric values such as prices and ratings to ensure consistency.
  - Removes rows with missing or incomplete data.
  - Drops duplicates to maintain a clean dataset.
  - Standardizes the data for easy analysis.
- After cleaning, the data is saved into a new file `cleaned_data.csv` for further analysis.

### 3. Data Visualization
- The `streamlit_data_visualization.py` script uses Streamlit to create interactive data visualizations.
- Users can interact with the visualizations and explore:
  - Product ratings by brand
  - Average price by brand
  - Product distribution by category
  - Price vs rating scatter plot
- Streamlit's interactive widgets allow filtering and dynamic exploration of the dataset.
