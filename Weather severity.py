total_rain = 0
total_wind = 0
count = 0
# corrected
while True:
    data = input()
    rain, wind = map (float, data.split())
    if rain == -1.0 and wind == 0:
        break
    total_rain += rain
    total_wind += wind
    count += 1
avg_rain = total_rain / count
avg_wind = total_wind / count

weather_severity = (avg_rain * 10) + avg_wind

print(f"The weather rain is {avg_rain:1f} inches")
print(f"The weather wind is {avg_wind:1f} mph")
print(f"The weather severity is for these {count} readings is {weather_severity:.1f} %")