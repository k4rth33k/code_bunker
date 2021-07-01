import requests

resp = requests.get('https://docs.determined.ai/latest/reference/cli.html')
print(resp.status_code)
