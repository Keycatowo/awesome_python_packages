from pytube import YouTube

# 要下載的影片網址
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# 建立 YouTube 物件
yt = YouTube(url)

# 取得影片資訊
title = yt.title # 標題
length = yt.length # 長度（秒）
rating = yt.rating # 評分

# 顯示影片資訊
print(f"標題：{title}")
print(f"長度：{length} 秒")
print(f"評分：{rating}")

# 選擇要下載的串流格式（這裡選擇最高解析度的 mp4 格式）
stream = yt.streams.filter(file_extension="mp4").get_highest_resolution()

# 下載影片到目前資料夾（也可以指定其他路徑）
stream.download()