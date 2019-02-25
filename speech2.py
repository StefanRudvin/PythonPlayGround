from gtts import gTTS
import os
import weather, news, datetime, currency, googleCalendar

def main():
    message = createMessage()

    tts = gTTS(text=message, lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

def createMessage():
    weatherString  = weather.getWeatherString()
    newsString     = news.getNewsString()
    calendarString = googleCalendar.getCalendarString()
    currencyString = currency.getCurrencyString()

    welcomeString = welcome()

    message = "{} How are you doing ma boy? {} {} {} . That is all for today. Berry out".format(welcomeString, weatherString, newsString, currency, calendarString)

    print(message)

    return message


def welcome():
    currentHour = datetime.datetime.now().hour
    print(currentHour)
    if (currentHour > 12):
        return "Good day Stefan."
    elif (currentHour > 18):
        return "Good evening Stefan."
    else:
        return "Good morning Stefan."


if __name__ == "__main__":
    main()
