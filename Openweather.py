import pyowm

owm = pyowm.OWM('5e6c36ae009623fb229b622824742c4d')

def getWeatherString():

    weatherObject = getCurrentWeather();

    windSpeed     = int(round(weatherObject['wind'][u'speed']))
    windDirection = int(round(weatherObject['wind'][u'deg']))
    humidity      = int(round(weatherObject['humidity']))
    maxTemp       = int(round(weatherObject['temperature']['temp_max']))
    currentTemp   = int(round(weatherObject['temperature']['temp']))
    minTemp       = int(round(weatherObject['temperature']['temp_min']))
    sunny         = getWeatherForecast();

    return "Today is going to be a wicked day with the current temperature at {} degrees, humidity at {} percent and windspeed at {} meters per second.".format(currentTemp, humidity, windSpeed)


location = "Espoo, fi"

def getWeatherForecast():
    #weatherObject = {}

    #forecast = owm.daily_forecast("Espoo,fi")

    #tomorrow = pyowm.timeutils.tomorrow()

    #print('daily forecast:')

    #print(forecast)

    # return forecast.will_be_sunny_at(tomorrow)

    return True


def getCurrentWeather():
    weatherObject = {}
    # Search for current weather in London (UKs)
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    print(w)                     # <Weather - reference time=2013-12-18 09:20,
                                # status=Clouds>
    weatherObject['wind']        = w.get_wind()
    weatherObject['humidity']    = w.get_humidity()
    weatherObject['temperature'] = w.get_temperature('celsius')
    weatherObject['status']      = w.get_temperature('celsius')

    return weatherObject


# Will it be sunny tomorrow at this time in Milan (Italy) ?
# forecast = owm.daily_forecast("Milan,it")
# tomorrow = pyowm.timeutils.tomorrow()
# forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)


# Weather details
#w.get_wind()                  # {'speed': 4.6, 'deg': 330}
#w.get_humidity()              # 87
#w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)
