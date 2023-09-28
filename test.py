import requests
from bs4 import BeautifulSoup

def get_temperature(country, city):
    url = "https://www.worldweatheronline.com/weather/{}/{}/".format(country, city)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # 気温を取得
    temperature = soup.find("span", class_="temp-value")
    return temperature.text

def main():
    # 国名と都市名を入力
    country = input("国名を入力してください: ")
    city = input("都市名を入力してください: ")

    # 気温を取得
    temperature = get_temperature(country, city)
    print("{}の{}の気温は{}です。".format(country, city, temperature))

if __name__ == "__main__":
    main()
