import sys
import os

# Import your specific modules
# (We assume you renamed your existing scripts to these names)
import stock_viz
import rag_chatbot

def main():
    print("--------------------------------------------------")
    print("   WELCOME TO THE AI INVESTMENT SCOUT (CLI)       ")
    print("--------------------------------------------------")

    # 1. User Input
    ticker = input("Enter Stock Ticker (e.g., AAPL, TSLA): ").upper().strip()
    
    # Map ticker to the specific text file for RAG context
    # In a real app, this might verify the file exists first
    data_file_path = f"data/{ticker}_10k.pdf"
    
    if not os.path.exists(data_file_path):
        print(f"Error: No data file found for {ticker}. Please add {ticker}_10k.pdf to /data.")
        sys.exit()

    # 2. The Visualization Phase
    print(f"\nGenerating Price Trends for {ticker}...")
    print("Check the popup window for the chart. Close it to proceed.")
    
    # Call the function from your Viz repo
    # You will pass the ticker so it knows what to download/plot
    stock_viz.generate_chart(ticker) 
    
    print(f"\n[Chart Closed] Transitioning to Analyst Mode...")

    # 3. The RAG/Chat Phase
    print(f"Loading {ticker} financial reports into the AI context...")
    
    # Call the function from your RAG repo
    # You pass the specific text file path so the RAG knows what to read
    rag_chatbot.start_chat_session(source_document=data_file_path)

if __name__ == "__main__":
    main()
