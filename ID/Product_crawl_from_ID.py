import pandas as pd
import requests
import time
import random
import numpy as np
from tqdm import tqdm


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, /',
    'Accept-Language': 'en-GB,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,en-US;q=0.6',
    #referer là link
    'Referer': 'https://tiki.vn/21-bai-hoc-cho-the-ky-21-p35191892.html?itm_campaign=CTP_YPD_TKA_PLA_UNK_ALL_UNK_UNK_UNK_UNK_X.272700_Y.1855020_Z.3853374_CN.AUTO---21-Bai-Hoc-Cho-The-Ky-21---2023%2F09%2F20-05%3A50%3A56&itm_medium=CPC&itm_source=tiki-ads&spid=35191894',
    'X-Guest-Token': '1ZBfTy8h952Oi3MpJLsd7mRUltb0owQH',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}
 
params = (
  ('platform', 'web'),
  ('spid','35191894')
)


def parser_product(json):
    
    d = dict()
    try:
        d['id'] = int(json.get('id'))
        d['name'] = json.get('name')
        d['price'] = int(json.get('price'))
        d['original_price'] = int(json.get('original_price'))
        d['discount'] = int(json.get('discount'))
        d['discount_rate'] = int(json.get('discount_rate'))
        d['days_created'] = json.get('day_ago_created')
        d['review_count'] = int(json.get('review_count'))
        for i in json.get('authors'):
          d['authors'] = i.get('name')
        for i in json.get('images'):
          d['images'] = i.get('base_url')
        d['categories'] = json.get('categories').get('name')
    except:
        d['id'] = np.nan
        d['name'] = np.nan
        d['price'] = np.nan
        d['original_price'] = np.nan
        d['discount'] = np.nan
        d['discount_rate'] = np.nan
        d['review_count'] = np.nan
        d['order_count'] = np.nan
        d['authors'] = np.nan
        d['categories'] = np.nan
         
    return d


df_id = pd.read_csv('ID_Bookdata.csv')#tên file ID
p_ids = df_id.id.to_list()
print(p_ids)
result = []
for pid in tqdm(p_ids, total=len(p_ids)):
     try:
        response = requests.get('https://tiki.vn/api/v2/products/{}'.format(pid), headers=headers, params=params)#, cookies=cookies)
        if response.status_code == 200:
            print('Crawl data {} success !!!'.format(pid))
            result.append(parser_product(response.json()))
    # time.sleep(random.randrange(3, 5))
     except:
        pass
df_product = pd.DataFrame(result)
df_product.to_csv('Bookdata.csv', index=False) #tên file sản phẩm