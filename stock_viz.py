import matplotlib.pyplot as plt
import yfinance as yf

def generate_chart(ticker):
    """
    Fetches 1 year of historical data for the given ticker
    and displays a line chart of the Closing prices.
    """
    print(f"--- [stock_viz] Fetching data for {ticker} from Yahoo Finance... ---")
    
    # 1. Fetch Data
    # We download the last 1 year ('1y') of data.
    try:
        stock_data = yf.download(ticker, period="1y", progress=False)
        
        # Check if data was actually returned (e.g., if user typed a fake ticker)
        if stock_data.empty:
            print(f"Error: No data found for symbol '{ticker}'.")
            return
            
    except Exception as e:
        print(f"An error occurred while fetching data: {e}")
        return

    # 2. Create the Visualization
    plt.figure(figsize=(10, 6))
    
    # Plot the 'Close' column from the dataframe
    # We use the dataframe index (Date) for the X-axis automatically
    plt.plot(stock_data.index, stock_data['Close'], label='Close Price', color='blue', linewidth=2)

    # 3. Style the Chart (The "Product Polish")
    plt.title(f"{ticker} Stock Price - Last 1 Year", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Price (USD)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # 4. Display the Chart
    # This command halts the script until the window is closed by the user
    print("--- [stock_viz] Displaying Chart. Close the window to continue. ---")
    plt.show()

# This block allows you to test this file safely without running main.py
if __name__ == "__main__":
    # If I run 'python stock_viz.py' directly, test with AAPL
    generate_chart("AAPL")
