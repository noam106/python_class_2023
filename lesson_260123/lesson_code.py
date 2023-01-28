import json
from datetime import datetime
import pytz
import requests

if __name__ == '__main__':
    #
    # api_url = 'https://www.boredapi.com/api/activity'
    # response = requests.get(api_url)
    # if response.status_code == 200:
    #     # print (response)
    #     # response_as_dict = json.loads(response.text)
    #     # print(response_as_dict['activity'])
    #
    #     # same as
    #     my_data = response.json()

    def name_netsional(name: str) -> str:
        name_check_url = f'https://api.nationalize.io/?name={name}'
        response = requests.get(name_check_url)
        if response.status_code == 200:
            my_data = response.json()
            # print(my_data)
            propability_list = sorted(my_data['country'], key=lambda s: s['probability'], reverse=True)
            # print(propability_list)
            name_in_contry = propability_list[0]['country_id']

            # print(name_in_contry)
            return name_in_contry


    def country_full_name(country_id: str) -> str:
        return pytz.country_names[country_id]


    def get_continent(contry: str) -> str:
        contry_info_url = f'https://restcountries.com/v3.1/alpha/{contry}'
        response = requests.get(contry_info_url)
        if response.status_code == 200:
            my_data = response.json()
            # print(my_data)
            continent = my_data[0]["region"]
            return continent


    def spoken_language(country: str) -> str:
        country_info_url = f'https://restcountries.com/v3.1/alpha/{country}'
        response = requests.get(country_info_url)
        if response.status_code == 200:
            my_data = response.json()
            language = my_data[0]["languages"]
            return language


    def current_time_in_country(country: str) -> str:
        country_timezone = pytz.country_timezones.get(country)
        # Current time in UTC
        format_1 = "%Y-%m-%d %H:%M:%S %Z%z"
        # Current time in UTC
        now_utc = datetime.now(pytz.timezone('UTC'))
        # Convert to Asia/Kolkata time zone
        now_country = now_utc.astimezone(pytz.timezone(country_timezone[0]))
        return now_country.strftime(format_1)


    def user_interface():

        user_name = input('Hello there, what is your name? ')
        country_name = name_netsional(user_name)
        full_country_name = country_full_name(country_name)
        continent = get_continent(country_name)
        language = spoken_language(country_name)
        current_time = current_time_in_country(country_name)
        answer_to_user = f' Hi {user_name}, it most likely you are from {full_country_name}\n.' \
                         f' {full_country_name} is located in ' \
                         f'{continent} and the formal languages are {language}.\n' \
                         f' you current time there is {current_time}'
        return answer_to_user

print(user_interface())
