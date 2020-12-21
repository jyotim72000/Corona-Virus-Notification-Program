from plyer import notification
import requests
import time


def notify(mystr):
    notification.notify(
        # title='COVID-19 Update for INDIA',
        title='COVID-19 Update for BHOPAL',
        message=mystr,
        # app_icon="D://PycharmProjects//firstProg//corona_outbreak//iicon.ico",
        # app_icon="https://findicons.com/icon/615731/virus_cell_infection_coronavirus",
        timeout=50)


if __name__ == '__main__':
    # url = "https://corona.lmao.ninja/v2/countries/India?yesterday&strict&query"
    url = "https://api.covid19india.org/state_district_wise.json"
    response = requests.get(url)
    var = response.json()
    print(var)
    while True:
#         message = f'''
# Total Cases = {var['cases']}
# Active Cases = {var['active']}
# Total Deaths = {var['deaths']}
# Source : NovelCOVID API'''
        message = f'''
Confirmed Cases = {var['Madhya Pradesh']['districtData']['Bhopal']['confirmed']}
Active Cases = {var['Madhya Pradesh']['districtData']['Bhopal']['active']}
Total Deaths = {var['Madhya Pradesh']['districtData']['Bhopal']['deceased']}
Total recovered = {var['Madhya Pradesh']['districtData']['Bhopal']['recovered']}
'''
        notify(message)
        time.sleep(60*60)
