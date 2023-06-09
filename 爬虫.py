import requests
from bs4 import BeautifulSoup
import csv
import time


def spider():
    # 设置要爬取的小说数量
    num_novels = 1000

    # 创建csv文件并写入表头
    with open('novels.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['小说类型', '作者名称', '小说名称', '小说URL', '小说状态', '最后更新时间'])

    # 循环爬取小说信息
    for i in range(1000, num_novels + 1000):
        try:
            url = f'http://www.biqugse.com/{i}/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # print(soup)

            # 获取小说信息
            category = soup.find('meta', {'property': 'og:novel:category'})['content']
            author = soup.find('meta', {'property': 'og:novel:author'})['content']
            book_name = soup.find('meta', {'property': 'og:novel:book_name'})['content']
            read_url = soup.find('meta', {'property': 'og:novel:read_url'})['content']
            status = soup.find('meta', {'property': 'og:novel:status'})['content']
            update_time = soup.find('meta', {'property': 'og:novel:update_time'})['content']
            print(f"第{i}部小说完成")
            if category == "":
                continue
            # 将小说信息写入csv文件
            with open('novels.csv', mode='a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([category, author, book_name, read_url, status, update_time])
        except:
            continue


if __name__ == '__main__':
    start_time = time.time()
    spider()
    end_time = time.time()
    total_time = end_time - start_time
    print("总耗时：", total_time, "秒")
