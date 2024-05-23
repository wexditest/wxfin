import requests 
from bs4 import BeautifulSoup 
  
  
# Making a GET request 
r = requests.get('https://stocks.zerodha.com/etfs/icici-prudential-nifty-100-etf-ICIC/events?type=dividends') 
  
# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 
  
s = soup.find('div', class_='event-upcoming') 
content = s.find_all() 
  
print(content)