
# 爬虫学习案例-----------------公开数据


# 用 ‌Requests + BeautifulSoup 自动爬取公开数据‌，核心就是“用 requests 拿网页、用 BeautifulSoup 解析提取”，入门成本很低，适合中小规模的静态页面抓取。‌‌

# 🛠️ 基础步骤
# ‌安装库‌：pip install requests beautifulsoup4 lxml，其中 lxml 是推荐的高性能解析器。
# ‌发送请求‌：用 requests.get(url, headers=headers, timeout=10) 获取网页，建议加上 User-Agent 请求头模拟浏览器，避免被拒。
# ‌处理编码‌：设置 response.encoding = response.apparent_encoding，可避免中文乱码。
# ‌解析网页‌：soup = BeautifulSoup(response.text, "lxml") 把 HTML 转成可搜索的对象树。
# ‌提取数据‌：用 find()、find_all() 或 CSS 选择器 select() 定位目标标签，再取文本或属性。
# ‌保存结果‌：写入 CSV、JSON 或数据库，方便后续分析


# 常用方法速查
# 表格
# 方法	作用	示例
# find()	找第一个匹配标签	soup.find('h1')
# find_all()	找所有匹配标签	soup.find_all('div', class_='item')
# select()	CSS 选择器，更灵活	soup.select('div.content > p')
# get_text()	提取标签内纯文本	element.get_text(strip=True)
# tag['href']	获取属性值	a_tag['href']


#  Selenium 或 Scrapy


# from pathlib import Path
# movies_top250 = Path(__file__).with_name('movies_top250.csv')

import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def get_movies(page):
    # url = f"https://?start={page * 25}&filter="
    response = requests.get(url, headers=headers, timeout=10)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    print(soup)
    
    movies = []
    for item in soup.select(".grid_view.item"):
        title = item.select_one(".title").text
        rating = item.select_one(".rating_num").text
        quote = item.select_one(".inq").text if item.select_one(".inq") else ""
        movies.append([title, rating, quote])
    return movies

# 爬取前5页
all_movies = []
for page in range(5):
    all_movies.extend(get_movies(page))
    print(f"第{page+1}页完成，共{len(all_movies)}部")

# 保存到CSV
with open("movies_top250.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["标题", "评分", "引言"])
    writer.writerows(all_movies)
