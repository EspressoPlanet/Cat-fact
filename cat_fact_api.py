import requests
import json

api_url = "https://catfact.ninja/fact?max_length=1000"

response = requests.get(api_url)
data = response.text
parse_json = json.loads(data)
main_text = parse_json['fact']


