import discord
import os
from datetime import date
from replit import db

import initialization as ini

with open('initialization.py', 'a') as f:
    f.write('print("hello")\n')

print(ini.a)
# Um den Bot zum Laufen zu bekommen habe ich den API Wrapper gewechselt.
# Mit dem Befehl "python3 -m pip install -U py-cord" habe ich pyCord installiert.
# Dadurch können wir jetzt auch Slash Befehle nutzen.


bot = discord.Bot()



@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

### old stuff ###
    #@bot.event
    #async def on_message(message):
    #    if message.author == bot.user:
    #        return
    
    #    if message.content.startswith('hello'):
    #        await message.channel.send('Hi Fuckface :) ')
    
    #@bot.command(name='hello')
    #async def foo(ctx, arg):
    #  print(arg)
    #  await ctx.send(arg)
    
    #@bot.command()
    #async def test(ctx):
    #    await ctx.send("hello world")
#################

# guild id ist unsere Server id. Wenn keine Id eingetragen ist, funktioniert das auch auf anderen Servern,   aber das kann beim deployen sehr lange dauern.
# description ist die Beschreibung, die in Discord angezeigt wird (schreib ein Slash und du siehst alle slash Befehle die du auf dem Server ausführen kannst)
# name ist der name des Befehls den man in Discord eintippen muss (natürlich nach einem Slash)
@bot.slash_command(guild_ids=[505846117427052566], description="Test", name="test")
async def hello(ctx):
    today = date.today()
    print(db["entry1"])
    await ctx.respond("Hello! Today's date is: {}".format(today))

@bot.event
async def on_message(message):
  if message.author == bot.user:
      return
  else:
    await message.channel.send('Hello!')

bot.run(os.environ['TOKEN'])
