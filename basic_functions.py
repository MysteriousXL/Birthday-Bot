"""
Description:
To be done

Prerequisites:

"""
#################### Import libraries/scripts ######################################################
from datetime import date
from replit import db
####################################################################################################

def start_listeners(bot,tc_server_id):
  ####################################################################################################
  #################### Function definition ###########################################################
  @bot.event
  async def on_ready():
    """Gives feedback in the console when the script is loaded.
    
      Args: 
  
      Returns: 
  
      Notes: 
  
      Examples: 
  
    """
    print('We have logged in as {0.user}'.format(bot))
  #---------------------------------------------------------------------------------------------------
  @bot.slash_command(guild_ids=[tc_server_id], description="Test", name="test")
  async def hello(ctx):
    """A reply to the slash command test is written to the Discord channel.
  
      guild_id (list of integers): 
        ID of the Discord servers, on which the function is running.
      description (string): 
        Description of the slash command that can be seen on the Discord server.
      name (string): 
        Name of the command to be called on the Discord server.
  
      Args:
          ctx (Context): The context of the slah command.
              The context contains, among other things, the author and the channel in which the command was written. 
              The context is automatically provided by the discord api.
              see also: https://docs.pycord.dev/en/stable/ext/commands/api.html#discord.ext.commands.Context
  
      Returns:
          
      Notes:
  
      Examples:
          >>> Write Discord message in an arbitrary channel: /test
          Bot answers: Hello! Todays date is: yyyymmdd
  
    """
    today = date.today()
    print(db["entry1"])
    await ctx.respond("Hello! Todays date is: {}".format(today))
  #---------------------------------------------------------------------------------------------------
  @bot.event
  async def on_message(message):
    """If anyone (except for the bot itself) writes a message, the bot answers with the defined string
      Args:
          message (string): any kind of message any user has written in any channel
  
      Returns:
  
      Notes:
  
      Examples:
          >>> Write Discord message in an arbitrary channel
          Bot answers: Hello!
  
    """
    if message.author == bot.user:
        return
    else:
      await message.channel.send('Hello!')
