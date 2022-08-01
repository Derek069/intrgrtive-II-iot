
import requests
import serial
from getSerial import getSerial

def post():
    while True:
    # atendance = 6520150022
        data = {
            "student_id":getSerial()
        }
        post = requests.post(f"https://intregrative-api.herokuapp.com/date/", headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}, data=data)
        print (post.text)

if __name__ == "__main__":
    post()