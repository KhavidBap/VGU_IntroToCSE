import pandas as pd
import matplotlib.pyplot as plt

class Task7:
    def __init__(self):
        print("Init task 7")
        self.path = 'weather.csv'
        self.dataframe = pd.read_csv(self.path)
        self.time = self.dataframe['Time'].head(12)
        self.humidity = pd.to_numeric(self.dataframe['Humidity'].str[0:2], downcast='integer')
        self.temperature = self.dataframe['Temperature'].head(12)
        self.cloud_cover = pd.to_numeric(self.dataframe['Cloud cover'].str[:-2], downcast= 'float')

    def Task7_Run(self):
        print("Task 7 is activated!")

        # Temperature
        fig = plt.figure(figsize=(7, 4))
        plt.plot(self.time[0:10], self.temperature[0:10], color='purple')
        plt.xlabel('Time')
        plt.ylabel('Temperature in Celcius')
        plt.title('Temperature vs. Time')
        plt.savefig("temperature.jpg")

        # Heat amplitute
        heat_amplitute = self.dataframe['Temperature'].max() - self.dataframe['Temperature'].min()
        print("Heat amplitute:", heat_amplitute)

        # Humidity
        fig = plt.figure(figsize=(7, 4))
        plt.plot(self.time[0:10], self.humidity[0:10], color='pink')
        plt.xlabel('Time')
        plt.ylabel('Humidity in %')
        plt.title('Humidity vs. Time')
        plt.savefig("humidity.jpg")

        # Average humidity
        avg_humidity = pd.to_numeric(self.dataframe['Humidity'].str[0:2], downcast='integer').mean()
        print("Average humidity:", avg_humidity)

        # UV database
        uv = self.dataframe['UV']
        high_uv = self.dataframe['High_UV'] = uv.apply(lambda x: 'Yes' if x >= 6 else 'No')
        status = self.dataframe['Status'] = high_uv.apply(lambda x: 'Harmful to skins' if x == 'Yes' else 'Not very harmful')
        df = pd.DataFrame({'Time': self.time, 'UV': uv, 'High_UV': high_uv, 'Status': status})
        df.to_csv('uv.csv', index=False, encoding='utf-8')

        # UV
        uv = self.dataframe['UV'].head(12)
        fig, ax = plt.subplots(figsize=(7, 6))
        bars = ax.bar(self.time[0:10], uv[0:10], color='grey')
        plt.xlabel('Time')
        plt.ylabel('UV')
        plt.title('UV vs. Time')
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3), textcoords='offset points',
                        ha='center', va='bottom')
        plt.savefig("UV.jpg")

        # Cloud cover
        fig, ax = plt.subplots(figsize=(7, 4))
        bars = ax.bar(self.time[0:10], self.cloud_cover[0:10], color='red')
        plt.xlabel('Time')
        plt.ylabel('Cloud cover in mm')
        plt.title('Cloud cover vs. Time')
        plt.savefig("cloud_cover.jpg")