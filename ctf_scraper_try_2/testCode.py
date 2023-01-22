import http.client
conn = http.client.HTTPSConnection("google.com")
conn.request("GET", "/")
res = conn.getresponse()
print(res.status, res.reason)
data = res.read()
print(data.decode("utf-8"))