import requests

API_KEY = ""   # your key
MODEL_ID = "" # your model id

url = f"https://app.nanonets.com/api/v2/OCR/Model/{MODEL_ID}/LabelFile/"
files = {'file': open('./pdf/2.pdf', 'rb')}
params = {'async': 'false'}

response = requests.post(
    url,
    auth=requests.auth.HTTPBasicAuth(API_KEY, ''),
    files=files,
    data=params
)

print(response.status_code)
print(response.text)  # or response.json()
