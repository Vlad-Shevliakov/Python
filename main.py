import http.client
conn = http.client.HTTPConnection("localhost:3000")
conn.request("GET", "/ru/latest/")
r1 = conn.getresponse()
print(r1.status)

data1 = r1.read()
conn.request("GET", "/parrot.spam")
r2 = conn.getresponse()
print(r2.status)

data2 = r2.read()
conn.close()