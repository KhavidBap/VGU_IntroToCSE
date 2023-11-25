import tkinter as tk
from tkinter import ttk
import random

class Task6:
    def __init__(self):
        print("Init task 6")
        return

    def Task6_Run(self):
        print("Task 6 is activated!")

        def predict_weather_condition(temperature, humidity, uv, cloud_cover):
            if temperature > 30 and uv > 5:
                return "Sunny"
            elif temperature < 20 or (temperature < 25 and humidity > 80):
                return "Cloudy"
            elif cloud_cover > 2:
                return "Rainy"
            else:
                return "Clear"

        def create_section_label(frame, label_text):
            label = ttk.Label(frame, text=label_text, font=("Arial", 12, "bold"))
            label.pack(pady=5, padx=10, anchor="w")

        def create_table(window, data):
            frame = ttk.Frame(window)
            frame.pack(pady=20, padx=20)
            for row in data:
                section_frame = ttk.Frame(frame, relief="solid", borderwidth=1)
                section_frame.pack(pady=10, padx=10, anchor="w", fill="x")
                create_section_label(section_frame, row[0])
                value_label = ttk.Label(section_frame, text=row[1], font=("Arial", 10))
                value_label.pack(pady=5, padx=10, anchor="w")

        def generate_random_data():
            temperature = random.randint(20, 35)
            humidity = random.randint(50, 95)
            uv = random.randint(0, 10)
            cloud_cover = random.uniform(0, 5)
            weather_condition = predict_weather_condition(temperature, humidity, uv, cloud_cover)
            data = [
                ("Time", f"{random.randint(0, 23):02}:00"),
                ("Temperature", f"{temperature} °C"),
                ("Humidity", f"{humidity}%"),
                ("UV", str(uv)),
                ("Cloud Cover", f"{cloud_cover:.1f} mm"),
                ("Weather Condition", weather_condition)
            ]
            return data

        def main():
            random_data = generate_random_data()
            window = tk.Tk()
            window.title("Weather Information")
            create_table(window, random_data)
            window.mainloop()

        if __name__ == "__main__":
            main()