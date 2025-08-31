# http://books.toscrape.com
from bs4 import BeautifulSoup
import  requests

content = requests.get('http://books.toscrape.com').text
soup = BeautifulSoup(content,'html.parser')
all_ps = soup.findAll('p',attrs={'class':'price_color'})
for p in all_ps:
    print(p.string)