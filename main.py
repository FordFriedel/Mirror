import discord
import os
import requests
import json
import random
from stock import Stock
from replit import db

client = discord.Client()

def get_news():
  response = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2021-08-16&sortBy=publishedAt&apiKey=c2b7cbb78dec4c198b36d900f2781571")
  print(response)
  print(type(response))
  json_data = json.loads(response.text)
  print(type(json_data))
  news = json_data["articles"][0]["url"]
  return(news)

def get_stock(ticker):
  response = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_0ab160a41e1641fbbb84a02baa280e3d&period=annual")
  json_data = json.loads(response.text)
  stockinfo = Stock(ticker, json_data["companyName"],json_data["avgTotalVolume"],json_data["change"], json_data["changePercent"])
  return(stockinfo.tickprint())

def get_weather(city):
  response = response.get("api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=a56ec5cb22d8e8355965d00b4a3a8cfc")
  json_data = json.loads(response.text)
  weathinfo = 


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("$news"):
    article = get_news()
    await message.channel.send(article)

  if msg.startswith("$s"):
    stock = get_stock(msg[3:])
    await message.channel.send(stock)
  
client.run(os.getenv('TOKEN'))