import requests

API_KEY = "c03e427e-96d6-11f0-bbac-364ad0a655a4"   # your key
MODEL_ID = "eeea72a6-ca04-4c5a-bc22-c032a84e9b2f" # your model id

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
