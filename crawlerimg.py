import requests
import shutil
import sqlite3 as lite

# url 配置要抓取的圖片連結
url = "https://i1.kknews.cc/SIG=274gml/ctp-vzntr/1538563660190spq3or3622.jpg"

# 使用stream = True將檔案視為2進位的資料
response = requests.get(url, stream=True)

print(response)
print(response.raw) 
print(response.text)

# 檔案下載
file_name = url.split('/')[-1]
with open(file_name, 'wb') as file:
    shutil.copyfileobj(response.raw, file)

# 連結sqlite資料庫，並創建游標物件
conn = lite.connect('test.db')
cur = conn.cursor()

# 讀取檔案的記憶體內容
with open(file_name, 'rb') as file:
    ablob = file.read()

# 將2進位資料儲存至資料庫
cur.execute('insert into images(filename) values (?)', [lite.Binary(ablob)])

# 提交commit才能儲存改變
conn.commit()

