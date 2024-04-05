from urllib.request import urlopen
import json
import matplotlib.pyplot as plt

response = urlopen('https://api.openf1.org/v1/intervals?session_key=9165')
data = json.loads(response.read().decode('utf-8'))

driverNumber = []
lap_times = []

for lap in data['lap']:
    if lap['driver_number'] not in driverNumber:
        driverNumber.append(lap['driver_number'])
    lap_times.append(lap['interval'])

plt.plot(driverNumber, lap_times)
plt.xlabel('Driver number')
plt.ylabel('Interval')
plt.title('Interval vs Driver Number')
plt.grid(True)
plt.show()