

# https://www.jamendo.com/settings

#
import json
import os

import requests
def get_track_list():
    url = "https://www.jamendo.com/api/tags"
    params = {
        "order": "featuredRank",
        "limit": 40,
        "lang": "en",
        "category[]": "genre"
    }

    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "cookie": "jammusiclang=en; _ga=GA1.2.588949051.1718088397; _gid=GA1.2.1799560132.1718088397; jamapplication=true; _hjSession_837371=eyJpZCI6IjYxY2IwYTkxLTRjYTgtNGY3NS05NjZmLTU3ODM4MjU4NmVlMiIsImMiOjE3MTgwODgzOTc3NzUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; jamAcceptCookie=true; jammusicconnection=9006079; jammusicsession=s%3ALOp1COneipihX5yQFsDD4WIA-1_qhU6M.dH1pyCdAOKYHCj%2BDSRDw9bNv5viETn16MQJ6ey117as; _hjSessionUser_837371=eyJpZCI6Ijk0NzgwODE1LWZmYmUtNTYzNi04ZWVhLTIyMjhlNTc2ODk2MiIsImNyZWF0ZWQiOjE3MTgwODgzOTc3NzQsImV4aXN0aW5nIjp0cnVlfQ==; _ga_6XE4DBPD2H=GS1.2.1718088397.1.1.1718091603.60.0.0",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.jamendo.com/start",
        "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "x-jam-call": "$5934968720837ccdbbb32c38bc55a33b54916adb*0.62341900822938~",
        "x-jam-version": "3mfh4w",
        "x-requested-with": "XMLHttpRequest"
    }

    response = requests.get(url, params= params,headers=headers)

    if response.status_code == 200:
        data = response.json()  # 假设响应为JSON格式

        print(data)
    else:
        print(f"请求失败，状态码: {response.status_code}")


def detail():
    url = "https://www.jamendo.com/api/albums?id%5B%5D=570554"

    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "cookie": "jammusiclang=en; _ga=GA1.2.588949051.1718088397; _gid=GA1.2.1799560132.1718088397; jamapplication=true; _hjSession_837371=eyJpZCI6IjYxY2IwYTkxLTRjYTgtNGY3NS05NjZmLTU3ODM4MjU4NmVlMiIsImMiOjE3MTgwODgzOTc3NzUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; jamAcceptCookie=true; jammusicconnection=9006079; jammusicsession=s%3ALOp1COneipihX5yQFsDD4WIA-1_qhU6M.dH1pyCdAOKYHCj%2BDSRDw9bNv5viETn16MQJ6ey117as; _hjSessionUser_837371=eyJpZCI6Ijk0NzgwODE1LWZmYmUtNTYzNi04ZWVhLTIyMjhlNTc2ODk2MiIsImNyZWF0ZWQiOjE3MTgwODgzOTc3NzQsImV4aXN0aW5nIjp0cnVlfQ==; _gat_UA-108987-19=1; _ga_6XE4DBPD2H=GS1.2.1718093864.2.0.1718093864.60.0.0",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.jamendo.com/track/2181597/be-without-u",
        "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "x-jam-call": "$723c8b93d551fb815ea294cf0a057f6119cdee81*0.44853591772094115~",
        "x-jam-version": "3mfh4w",
        "x-requested-with": "XMLHttpRequest"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()  # 假设响应为JSON格式

        # 将数据写入JSON文件
        with open('detail.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(data)
    else:
        print(f"请求失败，状态码: {response.status_code}")
detail()

def down_one():
    os.makedirs("mp3", exist_ok=True)

    url = 'https://prod-1.storage.jamendo.com/download/track/2181597/mp32/'  # 替换成你要下载的音乐文件的 URL

    # 发送GET请求并获取响应
    response = requests.get(url)

    if response.status_code == 200:
        # 解析URL获取文件名

        # 指定保存音乐文件的目录
        save_directory = "mp3"
        # 拼接完整的保存路径
        save_path = os.path.join(save_directory, "2181597.mp3")
        # 以二进制写入模式打开文件，并写入响应内容
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print('音乐文件下载成功，并保存到', save_path)
    else:
        print('下载音乐文件失败')


# https://storage.jamendo.com/download/p500305299/mp32/
# https://prod-1.storage.jamendo.com/download/track/2161171/mp32/


