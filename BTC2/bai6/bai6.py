import requests
import xml.etree.ElementTree as ET
import csv


url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"
response = requests.get(url)

# Lưu nội dung về máy
with open("rssfeed.xml", "wb") as file:
    file.write(response.content)

print(" Đã tải và lưu file rssfeed.xml thành công!")


tree = ET.parse("rssfeed.xml")
root = tree.getroot()

# Mỗi mục tin nằm trong <item> (chuẩn RSS)
items = root.findall(".//item")

news_list = []

for item in items:
    title = item.find("title").text if item.find("title") is not None else ""
    link = item.find("link").text if item.find("link") is not None else ""
    description = item.find("description").text if item.find("description") is not None else ""
    pubDate = item.find("pubDate").text if item.find("pubDate") is not None else ""

    news = {
        "title": title.strip(),
        "link": link.strip(),
        "description": description.strip(),
        "pubDate": pubDate.strip()
    }
    news_list.append(news)

print(f" Đã phân tích {len(news_list)} tin tức.")


with open("tintuc.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["title", "link", "description", "pubDate"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(news_list)

print(" Đã lưu danh sách tin tức vào file tintuc.csv thành công!")
