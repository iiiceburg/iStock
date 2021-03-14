import requests

class LineNotify():
    def notify():
        url = "https://notify-api.line.me/api/notify"
        token = "AuQiZeHCkED43oGO1IyoxWax7NOGo7kUqoWxjYBRWsl"
        headers = {"content-type":"application/x-www-form-urlencoded","Authorization":"Bearer "+token}
        msg="ผู้ใช้ : Test"
        req = requests.post(url,headers=headers,data={"message":msg})
        print(req.text)
LineNotify.notify()
