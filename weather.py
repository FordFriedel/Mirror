#WEBSITE DOMAIN FOR API DOCUMENTATION (2.5 day) https://openweathermap.org/current
cardinalDir = {1:"N",2:"NNE",3:"NE",4:"ENE",5:"E",6:"ESE",7:"SE",8:"SSE",9:"S",10:"SSW",11:"SW",12:"WSW",13:"W",14:"WNW",15:"NW",16:"NNW",17:"N"}

class CurrentWeather:
  def __init__(self, city, kTemp, kHigh, wind, windDir, hum):
    self.city = city
    self.cTemp = round(kTemp - 273.15)
    self.fTemp = round((cTemp * 5/9) + 32)
    self.cHigh = round(kHigh - 273.15)
    self.fHigh = round((cHigh * 5/9) + 32)
    #Note: Wind comes in at m/s,  round([NUM],[DIGITS])
    self.kmhWind = round(wind * 3.6, 1)
    self.mphWind = round(kmhWind * 0.621371, 1)
    self.windDir = cardinalDir[int(windDir)]
    self.hum = hum

  def weathPrint():
    str = "Weather for " + city + "\n" + 
    "- Temperature:" + self.fTemp + "°F  (" + cTemp + "°C)" + "\n" + 
    "- Day High:" + self.fTemp + "°F  (" + cTemp + "°C)" + "\n" + 
    
