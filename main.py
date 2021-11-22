import requests
from bs4 import BeautifulSoup
import pandas as pd

print('--- WEB SCRAPING GO4WORLDBUSINESS ---')
keywords = input("\nInput Keyword : ")

# print('\nSelect a time range')
# print('a = 3 days')
# print('b = 7 days')
# print('c = 30 days')
# print('d = 60 days')
# print('e = older than 60 days')
#
# daterange = input('Input Range Date : ')
# daterange = str(daterange)

rangepage = input('Input Range Page : ')
rangepage = int(rangepage)
# data = []

for page in range(1,rangepage+1):
      url = f'https://www.go4worldbusiness.com/find?searchText={keywords}&pg_buyers={page}&pg_suppliers=1&_format=html&BuyersOrSuppliers=buyers'

      try:
            content = requests.get(url)
      except Exception:
            None

      if content.status_code == 200:
            # print('PROGRAM RUNNING')

            soup = BeautifulSoup(content.text, 'html.parser')

            for result in soup.find_all('div','col-xs-12 nopadding search-results'):

                  ######## DISPLAYING BUYER'S COUNTRY ########
                  dbuyer = result.find('span', 'pull-left subtitle text-capitalize').text
                  buyer = dbuyer.split()
                  buyer = buyer[2:]
                  buyer = ''.join(buyer)

                  ######## DISPLAYING DATE BUYING ########
                  ddate = result.find('div', 'col-xs-3 col-sm-2 xs-padd-lr-2 nopadding').text
                  date = ddate.strip()

                  print('Date : ',date, 'Country : ',buyer)

                  # for commodities in soup.find_all('div', {'class': 'col-xs-12 entity-row-description-search xs-padd-lr-5'}):
                  #       commodities = commodities.text.strip()
                  #       # print(commodities)
                  #
                  #       for date in soup.find_all('div', {'class': 'col-xs-3 col-sm-2 xs-padd-lr-2 nopadding'}):
                  #             date = date.text.strip()
                  #             # print(date)

                              # print('Buyer:', buyer, 'Date:', date)

            #                   data.append({
            #                         'Buyer': buyer,
            #                         'Commodities': commodities,
            #                         'Date' : date

#                   })
#
# df = pd.DataFrame(data)
# df.to_csv(f'{keywords}.csv', index=False, encoding='utf-8')