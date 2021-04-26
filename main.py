from plyer import notification
import requests
import time
from bs4 import BeautifulSoup as bs


def notifyMe(title, message, app_icon=None):
    notification.notify(
        title = title,
        message = message,
        app_icon = app_icon,
        timeout = 5
    )

def getData(url):
    return requests.get(url).text

if __name__ == "__main__":
    myData = getData("https://www.worldometers.info/coronavirus/country/india/")
    soup = bs(myData, 'html.parser')

    while True:
        list=[]
        i = 4
        while i<=8:
            div = soup.find_all('div')[5].find_all('div')[2].find_all('div')[0].find_all('div')[0].find_all('div')[i].find_all('div')[0].find_all('span')[0]
            list.append(div.get_text())

            i = i+2

        notifyMe("Coronavirus Cases in India",
            f"Total Cases: {list[0]}\nDeaths: {list[1]}\nRecovered: {list[2]}", app_icon='favicon.ico')
        time.sleep(3600)