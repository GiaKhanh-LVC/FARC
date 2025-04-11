import requests

#URL Của POST, KHÔNG SỬA
url = "https://partyrock.aws/api/updateApp"

# Cách lấy Playload/Headers:
# B1: Truy cập App cần chỉnh trên PartyRock, chuột phải rồi nhấn kiểm tra hoặc nhấn F12.
# B2: Vào Tab Network, sau đó tại phía màn hình website nhấn SAVE một Widget bất kì để hiện Request UpdateApp trên Network.
# B3: Mở Request UpdateApp đó lên, tại Tab Headers sẽ có những thông tin cần thiết mà Code yêu cầu bên dưới, lưu ý là chỉ lấy
# những thông tin yêu cầu ở dưới headers thôi, không thêm bớt và phần nào có sẵn rồi thì không cần lấy. Tại Tab Playload thì 
# tìm hàng thứ hai có định dạng { AppID:... gì đó thì chuột phải rồi nhấn Copy Object rồi Paste sang đây là lấy được thông tin
# hiện tại của App dưới dạng JSON.

payload = {
}

headers = {
    "Cookie": "",
    "User-Agent": "",
    "Referer": "",
    "Anti-Csrftoken-A2z":""
}


response = requests.post(url, json=payload, headers=headers)

print("Status code:", response.status_code)
print("Response body:", response.text)  

