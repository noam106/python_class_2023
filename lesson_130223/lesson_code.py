import time
import requests
def count_down(sec):
    print("Counting down")
    while sec > 0:
        print(round(sec, 1))
        time.sleep(0.1)
        sec -= 0.1




def api_request(sec):
    response = requests.get("https://kanye.rest/")
    if response == '200':
        print(response)
    else:
        print('no')

api_request(2)