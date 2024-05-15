import requests
import time
import random
import pandas as pd



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, /',
    'Accept-Language': 'en-GB,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,en-US;q=0.6',
    'Referer': 'https://tiki.vn/nha-sach-tiki/c8322?sort=top_seller',
    'X-Guest-Token': '1ZBfTy8h952Oi3MpJLsd7mRUltb0owQH',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = {
    'limit':'40',
    'include':'advertisement',
    'aggregations':'2',
    'version':'home-persionalized',
    'trackity_id': '8f99f7c6-2955-b4ec-fc43-66297998c66c',
    'category':'8322',
    'page':'1',
    'src': 'c8322',
    'sort':'top_seller',
    'urlKey':'nha-sach-tiki',
}
product_id = []

for i in range(1, 51):
  params['page'] = i
  response = requests.get('https://tiki.vn/api/personalish/v1/blocks/listings', headers = headers, params = params) #, cookies = cookies)
  if response.status_code == 200:
    print('request success!!')
    for record in response.json().get('data'):
      product_id.append({id: record.get('id')})
  else:
    print('NOT SUCCESS!')
  time.sleep(random.randrange(3,10))

df = pd.DataFrame(product_id)
df.columns=['id']
df.to_csv('ID_Bookdata.csv', index = False) #tên file ID