# 抓ptt八卦版網頁原始碼
import urllib.request as req
import bs4
from selenium import webdriver
import urllib.request


def getData(url):
    request = req.Request(url, headers={
        "cookie": "over18=1",  # 十八歲以上方可進入
        "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # print(data)

    # 解析原始碼，取得每篇文章的標頭
    # 讓beautifulsoup 協助我們解析 html 格式文件
    root = bs4.BeautifulSoup(data, "html.parser")
    print(root.title.string)
    titles = root.find_all("div", class_="title")  # 尋找所有 class="title" 的標籤
    for title in titles:
        if title.a != None:  # 如果標頭包含 a 標籤(沒有被珊除)，印出來
            print(title.a.string)
    # 抓取上一頁的連結
    nextlink = root.find('a', string="‹ 上頁")  # 找到內文是上頁的 a標籤
    # print(nextlink["href"])
    return nextlink["href"]


# 抓取一個網頁的標題
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 5:
    pageURL = "https://www.ptt.cc"+getData(pageURL)
    count += 1
getData(pageURL)
# print(pageURL)
