"""
Description:
To be done


Prerequisites:
- Change of API Wrapper needed: 
  At first time use, use "python3 -m pip install -U py-cord" to install pyCord
- Find out your Discord Server ID/Guild ID, needed as constant for the script

"""
#################### Import libraries/scripts ######################################################
import discord
import os

import basic_functions

#################### Static parameter list #########################################################
tc_server_id=505846117427052566
#################### Main ##########################################################################
bot = discord.Bot()
basic_functions.start_listeners(bot,tc_server_id)


bot.run(os.environ['TOKEN'])


####################################################################################################


































# Example function notation
"""Calculate the number of occurences of a character in a string.

    If reasonable, a more elaborate description of the function follows (not
    needed here).

    Args:
        char (str): A string of length 1.
            Some further description of the parameter char is indented.
        string (str): A string.

    Returns:
        int or None: int if ``char`` is a string of length 1; None otherwise.

    Notes:
        Python has no own type for characters. If we had introduced exceptions
        in the lecture, we would throw some on non-legal inputs. Instead we are
        returning ``None`` in this case.

    Examples:

        >>> charcount("s", "spamam")
        1
        >>> charcount("a", "spamam")
        2
        >>> charcount("x", "spamam")
        0
        >>> x = charcount("am", "spamam")
        >>> x is None
        True

"""










""" OLD STUFF
with open('initialization.py', 'a') as f:
    f.write('print("hello")\n')

print(ini.a)

"""