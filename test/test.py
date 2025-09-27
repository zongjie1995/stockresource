import requests

if __name__ == '__main__':
    url = "https://push2.eastmoney.com/api/qt/stock/get"
    params={
        "secid": f"1.000001",
        "fields":"f120"
    }
    r = requests.get(url, params=params)
    data_json = r.json()
    print(data_json)