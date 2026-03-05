# 날씨 정보를 요청해서 csv로 저장하는 코드
import requests
import csv
from datetime import datetime
import os

MY_API_KEY = os.getenv("WEATHER_API_KEY")
city_name = "Seoul"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={MY_API_KEY}"
url += "&units=metric"

# get 방식으로 요청할 때 사용하는 라이브러리 requests
response = requests.get(url)
result = response.json()
temp = result["main"]["temp"]
weather = result["weather"][0]["main"]
humidity = result["main"]["humidity"]

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# weather.csv를 만들가
# 최초 생성 시 -> 헤더도 추가
# 파일이 존재하면 -> 덮어쓰기

csv_exist = os.path.exists("weather.csv")
header = ["current_time", "temp", "humidity", "weather"]

with open("weather.csv", "a", newline="") as f:
    writer = csv.writer(f)
    if not csv_exist:
        writer.writerow(header)

    writer.writerow([current_time, temp, humidity, weather])

print("날씨 저장 완료")
