from Adafruit_IO import Client
import os
api_key = os.getenv('api_key')
aio = Client('Yuva_2001',api_key)

from telegram.ext import Updater, MessageHandler,Filters

def demo1(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://image.shutterstock.com/image-vector/ok-hand-lettering-handmade-calligraphy-260nw-669965602.jpg'
  bot.message.reply_text('I am fine')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def demo2(bot,update):
  bot.message.reply_text("My name is abc-bot")

def lightOn(bot,update):
  chat_id = bot.message.chat_id
  aio.send('light', 1)
  path = 'https://static.scientificamerican.com/sciam/cache/file/2B38DE31-C1D3-4339-8808D61972976EE4.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("light is turned on")

def lightOff(bot,update):
  chat_id = bot.message.chat_id
  aio.send('light', 0)
  path = 'https://i.pinimg.com/474x/77/6a/30/776a3077389d21a1669a02a15acaa777.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("light is turned off")

def fanOn(bot,update):
  chat_id = bot.message.chat_id
  aio.send('fan', 1)
  path = 'https://www.thespruce.com/thmb/tyVxBz0q2ToJOLZCGKUHj6vwId0=/1883x1412/smart/filters:no_upscale()/GettyImages-182436453-5c79e51cc9e77c0001e98e6c.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("fan is turned on")

def fanOff(bot,update):
  chat_id = bot.message.chat_id
  aio.send('fan', 0)
  path = 'https://5.imimg.com/data5/DI/UR/MY-9970142/orient-ceiling-fan-500x500.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("fan is turned off")

def main(bot,update):
  a = bot.message.text.lower()
  print(a)

  if a == "how are you?":
    demo1(bot,update)
  elif a =="what is your name?" or a=="name please":
    demo2(bot,update)
  elif a =="turn on the light" or a =="light on":
    lightOn(bot,update)
  elif a =="turn off the light" or a =="light off":
    lightOff(bot,update)
  elif a =="turn on the fan" or a =="fan on":
    fanOn(bot,update)
  elif a =="turn off the fan" or a =="fan off":
    fanOff(bot,update)
  else:
    bot.message.reply_text('Invalid Text')

BOT_TOKEN = os.getenv('BOT_TOKEN')
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
