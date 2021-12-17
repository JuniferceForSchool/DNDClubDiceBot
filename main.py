import discord
import os
import shelve
TOKEN = os.getenv("TOKEN")
PREFIX = "!"

Client = discord.Client()
save = shelve.open("savedata")

PrivacyMessages = []
NumberMessages = []
RollMessages = []

def SaveAll():
  save["PrivacyMessages"] = PrivacyMessages
  save["NumberMessages"] = PrivacyMessages
  save["RollMessages"] = PrivacyMessages

def CheckExists(name):
  save = shelve.open("savedata")
  try: 
    return save[name]
  except Exception:
    save[name] = []
    return save[name]
  save.close()

def LoadAll():
  PrivacyMessges = CheckExists("PrivacyMessages")
  NumberMessges = CheckExists("NumberMessages")
  RollMessges = CheckExists("RollMessages")

@Client.event
async def on_ready():
  print(f'{Client.user.name} has connected to Discord!')
  LoadAll()

@Client.event
async def on_message(message):
  if list(message.content)[0] == PREFIX:
    Params = (message.content.split(PREFIX,1)[0]).split(" ")
    print(Params[0])

#Client.run(TOKEN)