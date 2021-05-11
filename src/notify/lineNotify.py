import requests
#use user token to connect line notify => msg
class LineNotify:
    def notify(msg,token):
        url = "https://notify-api.line.me/api/notify"
        headers = {"content-type":"application/x-www-form-urlencoded","Authorization":"Bearer "+token}
        response = requests.post(url,headers=headers,data={"message":msg})
        status = response.status_code
        return status

