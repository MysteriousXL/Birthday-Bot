"""
Description:
To be done


"""
#################### Import libraries/scripts ######################################################
from datetime import date
#from replit import db
import random

import database_handling_csv as database_handling
#import database_handling_replit_db as database_handling
####################################################################################################


def start_listeners(bot, tc_server_id):
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
    #print(db["entry1"])
    await ctx.respond("Hello! Todays date is: {}".format(today))

  #---------------------------------------------------------------------------------------------------
  @bot.event
  async def on_message(message):
    """If anyone (except for the bot itself) writes a message, the bot answers with the defined string when a random number is correct
      Args:
          message (string): any kind of message any user has written in any channel
  
      Returns:
  
      Notes:
  
      Examples:
          >>> Write Discord message in an arbitrary channel
          Bot answers: Hello!
  
    """
    rand_int=random.randint(1, 10)
    if message.author == bot.user:
      return
    elif rand_int==1:
      await message.channel.send('Can I help you?')
    else:
      return

  #---------------------------------------------------------------------------------------------------
  @bot.slash_command(guild_ids=[tc_server_id],
                     description="This deletes all entries of the database",
                     name="delete_database")
  async def delete_database(ctx):
    """The whole database will be deleted when this command is called.
  
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
    database_handling.reset_database()
    await ctx.respond("All database entries deleted")

  #---------------------------------------------------------------------------------------------------
  @bot.slash_command(
    guild_ids=[tc_server_id],
    description="Enter birthday as: Vorname Nachname DD.MM.YYYY",
    name="add_new_birthday")
  async def input_birthday_into_database(ctx, s_input):
    """The whole database will be deleted when this command is called.
  
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
    input_successful = database_handling.input_birthday_into_database(s_input)
    #Define answer message
    if input_successful == True:
      s_answer = "You have entered: " + s_input + ", it was successful."
    else:
      s_answer = "You have entered: " + s_input + ", it was already in the database."

    await ctx.respond(s_answer)

  #---------------------------------------------------------------------------------------------------
  @bot.slash_command(guild_ids=[tc_server_id],
                     description="This shows the next birthday in the channel",
                     name="get_next_birthday")
  async def get_next_birthday(ctx):
    """In the chat window the next birthday will be printed.
  
      guild_id (list of integers): 
        ID of the Discord servers, on which the function is running.
      description (string): 
        Description of the slash command that can be seen on the Discord server.
      name (string): 
        Name of the command to be called on the Discord server.
  
      Args:
          ctx (Context): The context of the slash command.
              The context contains, among other things, the author and the channel in which the command was written. 
              The context is automatically provided by the discord api.
              see also: https://docs.pycord.dev/en/stable/ext/commands/api.html#discord.ext.commands.Context
  
      Returns:
          
      Notes:
  
      Examples:
          >>> 
  
    """
    list_of_birthdays = database_handling.get_next_birthday()

    todays_date = date.today().strftime('%Y-%m-%d').split("-")

    #calculate days until next birthday
    birthday_date = date(1900, int(list_of_birthdays[0][3]),int(list_of_birthdays[0][2]))
    todays_date_reformatted = date(1900, int(todays_date[1]), int(todays_date[2]))
    days_until_birthday = birthday_date - todays_date_reformatted
    days_until_birthday = days_until_birthday.days

    if len(list_of_birthdays) < 1:
      #ERROR    
      pass
    elif len(list_of_birthdays) == 1:
      age = int(todays_date[0])-int(list_of_birthdays[0][4])
      output_string = f"Am {list_of_birthdays[0][2]}.{list_of_birthdays[0][3]} hat {list_of_birthdays[0][0]} {list_of_birthdays[0][1]} Geburtstag. {list_of_birthdays[0][0]} {list_of_birthdays[0][1]} wird {age} Jahre alt. Bis dahin sind es noch {days_until_birthday} Tage."
    else:
      names_string = ""
      age_string = ""
      counter = 0
      for birthday_entry in list_of_birthdays:
        names_string += birthday_entry[0] + " " + birthday_entry[1]
        if counter == len(list_of_birthdays) - 2:
          names_string += " und "
        elif counter == len(list_of_birthdays) - 1:
          names_string += " "
        else:
          names_string += ", "
        counter += 1
        age = int(todays_date[0])-int(birthday_entry[4])
        age_string += f" {birthday_entry[0]} {birthday_entry[1]} wird {age} Jahre alt."
      output_string = f"Am {list_of_birthdays[0][2]}.{list_of_birthdays[0][3]} haben {names_string} Geburtstag.{age_string} Bis dahin sind es noch {days_until_birthday} Tage."
    
    await ctx.respond(output_string)

  ###########################################DBG######################################################
  #---------------------------------------------------------------------------------------------------
  @bot.slash_command(guild_ids=[tc_server_id],
                     description="input test",
                     name="input_test")
  async def input_test(ctx, s_input):
    """The whole database will be deleted when this command is called.
  
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
    returnValue = database_handling.inputTest(s_input)
    await ctx.respond(returnValue)