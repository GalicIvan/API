from urllib.request import urlopen
import json
import pandas as pd

dataList = []
for i in range(1, 100):
    response = urlopen(f'https://api.openf1.org/v1/drivers?driver_number={i}&session_key=9158')
    data = json.loads(response.read().decode('utf-8'))
    if data:
        dataList.append(data)

# df = pd.DataFrame(dataList)
# print(df)
        
for item in dataList:
    for driver in item:
        print(f"Name of driver: {driver['full_name']} | Car number: {driver['driver_number']}")