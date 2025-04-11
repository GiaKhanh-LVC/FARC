import requests
import urllib.parse

original = '{"appId":"<điền vào mục này>"}'
encoded = urllib.parse.quote(original)
url = f"https://partyrock.aws/api/getApp?input={encoded}"

headers = {
    "Content-Type": "application/json",
    "Cookie": "",
    "User-Agent": "",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "",
    "Origin": "https://partyrock.aws",
    "Anti-Csrftoken-A2z":""
}

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)
print("Response body:", response.text)
