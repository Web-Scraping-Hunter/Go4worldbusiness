import requests
from bs4 import BeautifulSoup

keywords = input("Input Keyword : ")
page = input('Input Range Page : ')
page = int(page)

for page in range(page):
      url = 'https://www.go4worldbusiness.com/' \
            f'find?searchText={keywords}&pg_buyers={page}&pg_suppliers=1&_format=html&BuyersOrSuppliers=buyers'

      count = 0
      try:
            content = requests.get(url)
      except Exception:
            None

      if content.status_code == 200:
            print('PROGRAM RUNNING')

            soup = BeautifulSoup(content.text, 'html.parser')

            for buyer in soup.find_all('span', {'class':'pull-left subtitle text-capitalize'}):
                  buyer = buyer.text.strip().split()[2]
                  # print(buyer)

            for commodities in soup.find_all('div', {'class':'col-xs-12 entity-row-description-search xs-padd-lr-5'}):
                  commodities = commodities.text.strip()
                  # print(commodities)

            for date in soup.find_all('div', {'class':'col-xs-3 col-sm-2 xs-padd-lr-2 nopadding'}):
                  date = date.text.strip()
                  print(date)

            count+=1