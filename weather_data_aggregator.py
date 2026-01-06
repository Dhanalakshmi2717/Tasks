def analyze_weather(weather):
    max_temp = weather[0]["temp"]
    hottest_day = weather[0]["day"]
    total_temp = 0
    rainy_days = 0

    for day in weather:
        total_temp += day["temp"]

        if day["temp"] > max_temp:
            max_temp = day["temp"]
            hottest_day = day["day"]

        if day["rain"] == True:
            rainy_days += 1

    avg_temp = total_temp / len(weather)

    print("Hottest Day =", hottest_day)
    print("Average Temp =", round(avg_temp, 1))
    print("Rainy Days  =", rainy_days)

if __name__ == "__main__":
    weather = [
        {"day": "Mon", "temp": 32, "rain": False},
        {"day": "Tue", "temp": 35, "rain": True},
        {"day": "Wed", "temp": 30, "rain": False}
    ]

    analyze_weather(weather)
