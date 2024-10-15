import pandas as pd
import streamlit as st

# Load the data from Excel files
inflation_data = pd.read_excel('Inflation_event_stock_analysis_resultsOct.xlsx')
income_data = pd.read_excel('Inflation_IncomeStatement_correlation_results.xlsx')

# Set up Streamlit app
st.title('Stock Analysis Based on Inflation Events')

# Create a sidebar for user input
st.sidebar.header('Search for a Stock')
stock_name = st.sidebar.text_input('Enter Stock Symbol:', '')

# Function to fetch details for a specific stock
def get_stock_details(stock_symbol):
    inflation_row = inflation_data[inflation_data['Symbol'] == stock_symbol]
    income_row = income_data[income_data['Stock Name'] == stock_symbol]

    if not inflation_row.empty and not income_row.empty:
        inflation_details = inflation_row.iloc[0]
        income_details = income_row.iloc[0]

        st.subheader(f'Details for {stock_symbol}')
        
        # Display inflation event data
        st.write("### Inflation Event Data")
        st.write(inflation_row)

        # Display income statement data
        st.write("### Income Statement Data")
        st.write(income_row)

        # Additional interpretations based on conditions
        interpret_inflation_data(inflation_details)
        interpret_income_data(income_details)
    else:
        st.warning('Stock symbol not found in the data.')

# Function to interpret inflation data
def interpret_inflation_data(details):
    st.write("### Interpretation of Inflation Event Data")
    if details['Event Coefficient'] < -1:
        st.write("**1% Increase in Inflation:** Stock price decreases significantly. Increase portfolio risk.")
    elif details['Event Coefficient'] > 1:
        st.write("**1% Increase in Inflation:** Stock price increases, benefiting from inflation.")

    # Add more interpretations as per your conditions...

# Function to interpret income data
def interpret_income_data(details):
    st.write("### Interpretation of Income Statement Data")
    if details['Average Operating Margin'] > 0.2:
        st.write("**High Operating Margin:** Indicates strong management effectiveness.")
    elif details['Average Operating Margin'] < 0.1:
        st.write("**Low Operating Margin:** Reflects risk in profitability.")

    # Add more interpretations as per your conditions...

# Check if user has entered a stock symbol
if stock_name:
    get_stock_details(stock_name)
