### Stock Checker Bot
This Python script monitors product stock on two websites and alerts you if the stock changes. It checks every 10 minutes. The stock is checked via particular website elements and colors (in this instance, <p> element tag and color: #ff009b)

## Requirements
- Python 3
- "requests", "beautifulsoup4", "playsound"

## Setup
1. Install dependencies:
pip install requests beautifulsoup4 playsound
2. Run the script:
python stock_checker.py

Make sure you have "Recording.mp3" in the same folder as the script.