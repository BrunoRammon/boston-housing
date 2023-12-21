import requests
import json

url = 'http://localhost:5000/predict'
input_data = {
    "CHAS": { "0": 0 }, "RM": { "0": 6.575 },
    "TAX": { "0": 296 }, "PTRATIO": { "0": 15.3 },
    "B": { "0": 396.9 }, "LSTAT": { "0": 4.98 }
}
response = requests.post(url,json=input_data)
# input_data = json.dumps(input_data)
# headers = {"Content-Type": "application/json"}
# response = requests.post(url,data=input_data, headers=headers)

print(response.text)
