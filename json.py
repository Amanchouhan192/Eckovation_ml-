import urllib
import json
res=urllib.urlopen("https://data.gov.in/node/263823/datastore/export/json")
json.loads(res.read())
ans = json.loads(res.read())
print(ans)
