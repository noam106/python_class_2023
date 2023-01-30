import json
from datetime import datetime

# import requests
# import text2emotion
import requests
from nrclex import NRCLex

def name_valid(name: str) -> bool:
    if name.isalpha():
        return True
    else:
        return False

# print(name_valid('noam'))


def name_netsional(name: str) -> bool:
    name_check_url = f'https://api.nationalize.io/?name={name}'
    response = requests.get(name_check_url)
    if response.status_code == 200:
        my_data = response.json()
        # print(my_data)
    if len(my_data['country']) < 3:
        return False
    else:
        return True

# def how_do_you_feel(post: str) -> str:
#     print(te.get_emotion('like'))
#
# how_do_you_feel('noam')
#
# # print(name_netsional(''))
# #
# # # function that check if name is real
# #
# #
# #
# text = "I was asked to sign a third party contract a week out from stay. If it wasn't an 8 person group that took a lot of wrangling I would have cancelled the booking straight away. Bathrooms - there are no stand alone bathrooms. Please consider this - you have to clear out the main bedroom to use that bathroom. Other option is you walk through a different bedroom to get to its en-suite. Signs all over the apartment - there are signs everywhere - some helpful - some telling you rules. Perhaps some people like this but It negatively affected our enjoyment of the accommodation. Stairs - lots of them - some had slightly bending wood which caused a minor injury."
def usre_feeling(text: str) -> str:

    for i in range(len(text)):
        emotion = NRCLex(text[i])
    return emotion.top_emotions



import requests

url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

querystring = {"text":"great value in its price range!"}

headers = {
	"X-RapidAPI-Key": "0ec5c54452msh6ee1b06fcbb0e70p1ef796jsnec2138a2d776",
	"X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)