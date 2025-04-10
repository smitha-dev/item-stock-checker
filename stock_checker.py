import time
import requests
from bs4 import BeautifulSoup
import re
from playsound import playsound

# Function to extract stock from a webpage
def check_stock(url, max_stock):
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for <p> tags with style="color:#ff009b;"
        # stock count is the only <p> tag with this defined color
        stock_text = soup.find("p", style="color:#ff009b;")
        
        # Print out the stock text to see if we're finding it correctly
        if stock_text:
            print(stock_text.text)  # Print the full stock text

            # Adjust regex to handle extra spaces between stock numbers
            match = re.search(r"(\d+)\s*/\s*\d+\s*SALES", stock_text.text)
            
            if match:
                stock_number = int(match.group(1))  # Extract and convert the number
                
                # Check if stock is less than max stock, alert user
                if stock_number != max_stock:
                    print(f"ITEM IN STOCK ITEM IN STOCK! Current stock: {stock_number}")
                    print(f"ITEM IN STOCK ITEM IN STOCK! Current stock: {stock_number}")
                    print(f"ITEM IN STOCK ITEM IN STOCK! Current stock: {stock_number}")
                    playsound("Recording.mp3") 

                else:
                    print(f"Amount sold is {stock_number}.")
            else:
                print("Could not extract stock number from the text.")
        else:
            print("Could not find stock information. Checking again...")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    
    # US website URL and max static stock of 4700
    us_url = "https://bodega.lomavistarecordings.com/products/blasphemyheresymystery"
    us_max_stock = 4700

    # UK website URL and max static stock of 1000
    uk_url = "https://intlbodega.lomavistarecordings.com/products/blasphemyheresymystery"
    uk_max_stock = 1000

    while True:
        print("----- CHECKING US SITE -----")
        check_stock(us_url, us_max_stock)  # Check US site

        print("\n----- CHECKING UK SITE -----")
        check_stock(uk_url, uk_max_stock)  # Check UK site

        print("\n\n\n")
        
        time.sleep(600)  # Check every 10 minutes