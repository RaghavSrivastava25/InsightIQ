from sec_edgar_downloader import Downloader
import os

# Function to download 10-K filings for a specified list of companies from 1995 to 2023
def download_10k_filings(company_tickers, start_year, end_year):
    user_agent_company = "XXXXX"  
    user_agent_email = "XXXXX"  
    output_folder = "/content/sec_filings"  

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    dl = Downloader(user_agent_company, user_agent_email, output_folder)

    # Loop through each company and download the 10-K filings from start_year to end_year
    for ticker in company_tickers:
        for year in range(start_year, end_year + 1):
            # Define the date range for the year
            start_date = f"{year}-01-01"
            end_date = f"{year}-12-31"
            try:
                # Download 10-K filings for the year
                num_files_downloaded = dl.get("10-K", ticker, after=start_date, before=end_date)
                print(f"Downloaded {num_files_downloaded} 10-K filings for {ticker} for the year {year}.")
            except Exception as e:
                print(f"Error downloading 10-K filings for {ticker} for the year {year}: {e}")

# Define the list of company tickers to download filings for
company_tickers = ["AAPL", "GOOGL", "MSFT"]  # Add or change tickers as needed

# Call the function to download 10-K filings from 1995 to 2023
download_10k_filings(company_tickers, 1995, 2023)
