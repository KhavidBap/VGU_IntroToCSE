from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

class Task2:
    def __init__(self):
        print("Init task 2")
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.weather25.com/asia/vietnam?page=today")
        self.content = self.driver.page_source
        self.soup = BeautifulSoup(self.content, "html.parser")

    def Task2_Run(self):
        print("Task 2 is activated!")
        time = []
        temperature = []
        humidity = []
        UV = []
        cloud_cover = []

        time_tags = self.soup.find('thead').find_all('td')
        for time_value in time_tags:
            time.append(time_value.text)

        temperature_tags = self.soup.find('tr', attrs={'id': 'line1'}).find_all('span', attrs={'class': 'day_temp'})
        for temperature_value in temperature_tags:
            temperature.append(temperature_value.text)

        humidity_tags = self.soup.find('tr', attrs={'id': 'line5'}).find_all('td')
        for humidity_value in humidity_tags:
            humidity.append(humidity_value.text)

        UV_tags = self.soup.find('tr', attrs={'id': 'line11'}).find_all('td')
        for UV_value in UV_tags:
            UV.append(UV_value.text)

        cloud_cover_tags = self.soup.find('tr', attrs={'id': 'line3'}).find_all('td')
        for cloud_cover_value in cloud_cover_tags:
            cloud_cover.append(cloud_cover_value.text)

        df = pd.DataFrame({'Time': time, 'Temperature': temperature, 'Humidity': humidity, 'UV': UV, 'Cloud cover': cloud_cover})
        df.to_csv('weather.csv', index=False, encoding='utf-8')
