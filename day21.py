import requests

# url = "https://markets.onlinekhabar.com/smtm/stock_live/sector-performance"

# r = requests.get(url=url)
# if r.status_code == 200:
#     data = r.json() ['response']
#     for i in data:
#         print (i['indices'], i['percentage_change'])
# else:
#     print("fail")


# url = "https://markets.onlinekhabar.com/smtm/home/most-searched-stocks"

# r = requests.get(url=url)
# if r.status_code == 200:
#     data = r.json() ['response']
#     # print(data.keys())
#     for i in data:
#         print(i['ticker'], i['pointChange'], i['ltp'])


# else:
#     print('fail')


url =  "https://markets.onlinekhabar.com/smtm/home/gainers-losers/microfinance"

r = requests.get(url=url)
if r.status_code == 200:
    data = r.json() ['response']
    print(data.keys())
    print(type(data))
    data1 = data

else:
    print('fail')