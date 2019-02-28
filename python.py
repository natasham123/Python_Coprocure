try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
from bs4 import BeautifulSoup
import json

quote_page = 'https://www.sourcewell-mn.gov/cooperative-purchasing/022217-wex'
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find(‘h1’, attrs={‘class’: ‘h2’})
h2 = name_box.text.strip()
print (h2)
jsonData1 = json.loads(element.attrs[{‘class’: ‘h2’}])
print (jsonData1)

contract = soup.find(‘div’, attrs={‘class’:’vendor-contract-body’})
vendor-contract-body = contract.text
print (vendor-contract-body)
jsonData2 = json.loads(element.attrs[{‘class’:’vendor-contract-body’}])
print (jsonData2)


"""from pprint import pprint
import pandas as pd

data = "https://www.sourcewell-mn.gov/cooperative-purchasing/022217-wex"

df = pd.read_html(data, flavor="lxml")[0]

new_header = df.iloc[0]
df = df[1:]
df.columns = new_header

pprint(df.to_dict('records'))"""

"""from bs4 import BeautifulSoup
import json
data = 'https://www.sourcewell-mn.gov/cooperative-purchasing/022217-wex'
soup = BeautifulSoup(data)

inner_ul = soup.find('a', class_='flexContainer flexColumn')
inner_items = [.text.strip() for li in inner_ul.ul.find_all('li')]

outer_ul_text = soup.ul.span.text.strip()
inner_ul_text = inner_ul.span.text.strip()

result = {outer_ul_text: {inner_ul_text: inner_items}}
print (result)

data = 'https://www.sourcewell-mn.gov/cooperative-purchasing/022217-wex'
soup = BeautifulSoup(data, 'html.parser')
element = soup.find('div', class_='dialog-off-canvas-main-canvas')
#print (element.attrs['data-off-canvas-main-canvas'])
jsonData = json.loads(element.attrs['data-off-canvas-main-canvas'])
print (jsonData['sku'])"""
