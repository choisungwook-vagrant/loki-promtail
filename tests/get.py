import requests
import json

api = "http://192.168.25.43:3100/loki/api/v1/query_range"

params = {
    "query": '{filename="/var/log/alternatives.log"}'
}

response = requests.get(api, params=params)
if not response.ok:
    print(response.status_code)
    print(response.content.decode("utf-8"))
else:
    response_data = response.json()
    streams = response_data["data"]["result"]
    
    with open("get_result.json", "w") as f:
        f.write(json.dumps(streams))