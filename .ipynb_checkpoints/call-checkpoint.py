import http.client

# consume coincap /rates api
conn = http.client.HTTPSConnection("api.coincap.io")
payload = ''
headers = {}
conn.request("GET", "/v2/rates/bitcoin", payload, headers)
res = conn.getresponse()
data = res.read()
print("response from coincap:")
print(data.decode("utf-8"))

conn = http.client.HTTPSConnection("pro.openweathermap.org")
payload = ''
headers = {}

# consume weather api - Climatic Forecast 30 days
conn.request("GET", "/data/2.5/forecast/climate?lat=59.911491&lon=10.757933&appid=92c10b80548ec149560efd34691d03ee", payload, headers)
res = conn.getresponse()
data = res.read()
print("response from weather api - Climatic Forecast 30 days:")
print(data.decode("utf-8"))

# consume weather api - Hourly Forecast 4 days:
conn.request("GET", "/data/2.5/forecast/hourly?lat=59.911491&lon=10.757933&appid=92c10b80548ec149560efd34691d03ee", payload, headers)
res = conn.getresponse()
data = res.read()
print("response from weather api - Hourly Forecast 4 days:")
print(data.decode("utf-8"))