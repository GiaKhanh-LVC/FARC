import requests

url = f"" #Lấy link theo định dạng https://partyrock.aws/api/getApp?input={Encoded JSON App ID}

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
