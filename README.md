# 來用爬蟲抓取圖片，並存到資料庫吧！
    參考學習影片: https://www.youtube.com/watch?v=kmaLelILvb8&list=PLohb4k71XnPaQRTvKW4Uii1oq-JPGpwWF&index=16
    
## 圖片下載參考學習文檔: 
    https://titangene.github.io/article/python-crawler-note.html#%E4%B8%8B%E8%BC%89%E5%9C%96%E7%89%87

## python with 的用法
    參考文獻: https://www.itread01.com/content/1549615343.html
    主要用with是可以去除f.close()的問題

## SQlite 輕量級資料庫
    如果你是對資料庫有資處概念的，例如用過MYSQL或是其他資料庫，想了解Sqlite差別在那的話，請直接參考下面的文章哦
    https://medium.com/erens-tech-book/sqlite-%E8%88%87-mysql-%E7%9A%84%E5%B7%AE%E5%88%A5-a14926030ddd

## 搭配DB Browser for SQLite來進行圖形化介面使用吧!!!
    下載連結: https://sqlitebrowser.org/

## 實作心得
    這次練習了解將圖片資料化並儲存到資料庫中
    1. 學習如何下載圖片
    2. 學習將圖片儲存到資料庫中
    3. 學習sqlite資料庫，記得使用游標執行任何行為時，一定要提交commit才能儲存
    4. 使用DB Browser for SQLite來進行資料庫開啟及創建資料表
    5. 了解requests的stream = true用法
    6. 將檔案處理的f.open f.close改為用with的寫法

    第一次知道原來整個圖片的內容可以存到資料庫裏面，覺得非常地有趣！
    歡迎大家也來嘗試看看