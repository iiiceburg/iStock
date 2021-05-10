import requests

class LineNotify:
    def notify(msg):
        url = "https://notify-api.line.me/api/notify"
        token = "AuQiZeHCkED43oGO1IyoxWax7NOGo7kUqoWxjYBRWsl"
        headers = {"content-type":"application/x-www-form-urlencoded","Authorization":"Bearer "+token}
        requests.post(url,headers=headers,data={"message":msg})
