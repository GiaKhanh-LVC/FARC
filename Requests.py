import requests

url = "https://partyrock.aws/api/updateApp"
payload = {
    "appId": "a9elPUU9p",
    "title": "new-app-a9elPUU9p",
    "definition": {
        "version": 1,
        "widgets": [
            {
                "x": 0,
                "y": 0,
                "max": 100,
                "min": 0,
                "step": 1,
                "type": "number-input",
                "unit": "",
                "title": "widget0",
                "width": 12,
                "height": 2,
                "markLabels": [
                    "Low",
                    "Medium",
                    "High"
                ],
                "numberWidgetMode": "both"
            },
            {
                "x": 0,
                "y": 2,
                "type": "select",
                "title": "widget1",
                "width": 12,
                "height": 2,
                "options": [
                    "Option 1",
                    "Option 2",
                    "Option1"
                ],
                "placeholder": "a",
                "defaultValue": "Option 1"
            },
            {
                "x": 0,
                "y": 4,
                "type": "static-text",
                "title": "SCIENCE LAB",
                "width": 12,
                "height": 4,
                "content": "## HELLO ."
            }
        ]
    }
}
headers = {
    "Content-Type": "application/json",
    "Cookie": "pr_refresh_token=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.UOTkioSAkJjRNR4ctgQnaFuJpmzWR7lp0DRHcVVHc4yDX5ESv3XLHHj_AsiOSkVZFwra6oiTWQX7E95J11z0N-rYKuNeCifXTTXsuS2uvz26umQ6GWHKcMEJEcRmqm7-3GYg-Bhu3Bjc2tldxJIY-JcMymLK5Lkxz1WoRx2Lk1lU15YHlJpY-a24r1UxMG_StuoRri5ZEjaz8JkK8CfjLaMpEE3k6n_4cBRgEuBoVEBGR4Qrtlv9z6vvnp4Q8s8gRTIXL5-d1KUUBZ7jxV6JKH7W-1FkFb8RtnfZdjZdHhLJR7RDbEP5fm4_LaSUZsfstG5ByZ-us3O_BADO2S9LqA.VRiLsjES1m43Ot66.C1BqR1Ja_9RzKy1iHkEn077-h3-XFSCnnIzPFgzCGPeCk6gAQNumwc-qGJArryApri2aVO4dG6acsdRjjHOFSjByZfbCxLoCJwEGQYA1Xsu3EPlfgO0qNAdYm_AgDw0wuOtYtPnV_dWdt80r9338yoCneQ01uwvx1NN92tE8BxlM0gwJO5zOVJK3PdMhUCNMg4TGXK_YswCouHC9Nxx1aqdAKxVqqsw2ukgkCvgM4pK36O9uUpY7ypekMw2kJn0FrNPQyAL61lydE2dsMCHZhp0TgaLm1lUBbhcEgGIyeLVk0VSuJz_-X1wRmzKSRnGQR4wcC2zgfFB3zBOEH13tq5358yA8cgDoabctYTHZvQXrj4SuKiVPB3WlcxrMIWd-6Po4lilxbsKA9rLEOAttyy9HBDRFSNHcYH5I62Qe0sGhM6XHmofWOT9Tv5JhUKddlqEC9XbT5Y5_cOfW07XTgbxZX3txEeoi__c9p2jkxmVEsYzy5PkElRNZya3o_jFn8cGAkvn9lJa-V-ZLk8zIogIjJ0KyQkRi_K98OQB_1bzWaydlH8pSVdOJrylZMZRCgFuBsdqT7lFNOFUvRDva18viI6P_NdQlbOBvxnaW8N9iskEcuDFODaRT-yI5XaWTkUgpaX3TeFDp_M1apmkG9n-H_lqGBRatKzojGykZ8oEbog2nXvpRogM5j33ZXAwyjV9Ka3kTf0MLw_pI73phZjN2lrvdL1jqgRJj0mBKgCQd8R6cjwP3SKrWOwjUDo_Y2QRfq2vY5M-FWiW0P3j71PUz76phksdGyTXNeEieSUQ3k2P_FE5L3KNvG9X038vYHN33qGfpdUaoOzdhoSvFoUuf7eNMwst2gEvmG7B85R49bm4H31qRmbe34lOi6bG3MabpJGlEZyNZwCmGY7KKRxYBfkVsurnuV9uw4TP73shmLD_pVDIxcruaMvNbIH9nloqOYooRF_7jXZ2gTvCdfaizBvimqqFC_dCslqkigiw9Ateh3ttdGJt32iAbD2_YFie2efeZkif2SAFPPwZd5-rLuQIHNvYYzr4HqQFvvyDmEtJWuSHkrPx1x6zlkPeS8ji-KiPlkX5fK2OcIwgk7Fw5keDDxJW4T92jJPrX1yQrtKrHdLsCHG1K7nLHCn4gL8LeaB4R5uJcrrsP1MI4UKWV8h8vu8sCPZOY2rEXQ1l20eG_Z08n5hqUHlLL5ImeOBYokrfHDoLtQ82wHUz9LkNSMB8vyddxsWKOSafLyr8iBhr-orEGBl_vub6_MnqDAVpaeKb_qiqGrEssQtGiWRBZ5g.9_KXVIvWSNRtt-kYBr6H3w; awsccc=eyJlIjoxLCJwIjoxLCJmIjoxLCJhIjoxLCJjY2JhIjoxLCJpIjoiZWM0ZTk4MDQtMTg2Yy00MDM3LWFmOGUtM2Y3MGVjM2FhMjY1IiwidiI6IjEifQ==; cwr_u=78d4f0ef-ec7c-4aaf-a1ec-1446fc3eaecc; aws-waf-token=73b67ab7-4385-4097-b43c-ed77912cf65e:NQoAgctfvkZ2AAAA:i4zq4b9eemnnWGI6zMTVvJmrQ/bOnSZRrkUgDUb0qG2Mg6ypyC3TUigLFgxiR7hGHAUSbsjKVnry4qY7ckJgo0DY8DW3a1cv37rWsCXSnXwUCyLbL1FImXX2aNEFD7azWdKGeQ60GnUrg+Pu33hbhKgv37nlQ2Bjsk+bY9DKxIZluicu5JNGOrA7mSYjRn9AZh+WgQgpGw==; idToken=eyJraWQiOiJORFk0VnpldkxaWmFBOGVDb3lCb0l0YTQ1VHZaNmhtZUoxaTZzSTUwb1lnPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiT1N4bTdFQ1ZCSkpybVNpR1djX0ZRdyIsInN1YiI6ImZjMjBhMDYzLWE1NjQtNDY3My04ZmMzLTIyZjBlZmE2MjIwNiIsImNvZ25pdG86Z3JvdXBzIjpbInVzLWVhc3QtMV9FQXFPd0g0S3hfR29vZ2xlIl0sImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfRUFxT3dINEt4IiwiY29nbml0bzp1c2VybmFtZSI6Ikdvb2dsZV8xMDMyMjg0NTIyODc5ODQ2Mzc5OTMiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJHaWFLaGFuaCIsImdpdmVuX25hbWUiOiJLaMOhbmgiLCJjdXN0b206dXNlcklkIjoiNDE1OTQxIiwiY3VzdG9tOmNpdHkiOiJUdXkgSG9hIiwib3JpZ2luX2p0aSI6IjAyM2JkNDg4LTFmNjMtNDI2MS05ODQzLTZkODFkODBhY2Y0MyIsImF1ZCI6IjV2ZWE0dWc5bnRwcXR1cGhrNWlydDBkYjBtIiwiY3VzdG9tOmNvdW50cnlDb2RlIjoiVk4iLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMDMyMjg0NTIyODc5ODQ2Mzc5OTMiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNzQzMDc4OTgxMzU0In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTc0MzA3ODk4MiwibmFtZSI6Iktow6FuaCBOZ3V54buFbiIsImV4cCI6MTc0NDI5MzUyMywiaWF0IjoxNzQ0MjkyNjIzLCJmYW1pbHlfbmFtZSI6Ik5ndXnhu4VuIiwianRpIjoiMDFhOTEzMGItZDYwMy00ZmIxLTg5NzQtMWQ2MWNiNDM2MGMyIiwiZW1haWwiOiJnaWFraGFuaGNhZmV0dW5nQGdtYWlsLmNvbSJ9.zFcdy0uBUK2zj7ukajTlQmO5dOo-mg5D2FlJ5h96pRfBuE345WpPOc8ohGbgrgUFmsc117MsiVQx_UBM8Sgn8BCfmmOXYRrgJdvvFIn3k-tiMlGDy8P-idS-nL6LJSB9IZ6URAWn6xlR_EOr15PumgBJQT53fbt-Ey3gopt0md8W0vROBuq9L-WPim5w20YVy4TFsfp8y6TLc3QfuFtONZ77KU-EnZWDlRNMn_0wIxbeMQa3X2cbj56ZgeYqPpKlrei4if8ckJbc3op47fqa1q3e5FZ-s9d51sStQ8cJHicv5UD8OA2O9TLgMtylZQxTgGymb3oiR8wRpwzsU_7LIQ; cwr_s=eyJzZXNzaW9uSWQiOiI5YTQ3ZGNhNi0zZWQ2LTQzYmItOTE1NS04Y2FhZGYxYTZiMDciLCJyZWNvcmQiOnRydWUsImV2ZW50Q291bnQiOjczLCJwYWdlIjp7InBhZ2VJZCI6Ii91L0dpYUtoYW5oL2E5ZWxQVVU5cC9uZXctYXBwLWE5ZWxQVVU5cCIsImludGVyYWN0aW9uIjowLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3LmJpbmcuY29tLyIsInJlZmVycmVyRG9tYWluIjoid3d3LmJpbmcuY29tIiwic3RhcnQiOjE3NDQyODg3MDk0MzB9fQ==",  # token bạn có
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36 Edg/135.0.0.0",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://partyrock.aws/u/GiaKhanh/a9elPUU9p/new-app-a9elPUU9p",
    "Origin": "https://partyrock.aws",
    "Anti-Csrftoken-A2z":"hE16Wm5rYU5kenFxT0NJdjFrbVZ6eUpwWjMrbmlPVzJRZ/fLDwAAAABmMjZkNGI3YS0xMTdkLTQ1MDEtOTMwNS02MWNmMDczODM5NGM="
}


response = requests.post(url, json=payload, headers=headers)

print("Status code:", response.status_code)
print("Response body:", response.text)  

