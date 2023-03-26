"""


"""
#################### Import libraries/scripts ######################################################
from replit import db
from datetime import datetime
####################################################################################################

##############  DBG  #############################
"""for year in db.keys():
    print("year: " + year)
    for month in db[year]:
        print("month: " + month)
        for day in db[year][month]:
            print("day: " + day)
            for name in db[year][month][day]:
                print(name)"""
##############  DBG end  #########################


def input_birthday_into_database(s_input):
  """Deletes all entries in the database when called.
      Args:     Input string in the format "Vorname Nachname DD.MM.YYYY"
      Returns:  True/False - succesful input to the database
      Notes:    
          Database structure example
          db={
          YYYY1: 
            {
             MM1: {DD1: [Vorname1 Nachname1]},
             MM2: {DD2: [Vorname2 Nachname2]}
            },
          YYYY2: 
            {
            MM1: ...
            }
          }
        db[1989] = {"02": {"28": [Vorname1 Nachname1]}}
      Examples:  

    {"birthdays": [{"year": 2000, "month": 1, "day": 1, 
                    "vorname": "Vorname", "nachname": Nachname},...]}


  CSV 
  Vorname Nachname DD MM YYYY
  seb     bec   10   09   1989
  M       M     01   02   1910
  M2       M2     03   05   1980


  gettime = 01011900
  getmonth= 01 getday=01

  CSV splitMonth()
  [MM
  09
  02]
Column MM : search (x>=01)
[n.a
0
1]
with open('readme.txt', 'w') as f:
    f.write('readme')
    
  """
    #input string will be splitted in a format similar to ['Vorname','Nachname','DD.MM.YYYY']
    s_birthday_entry = s_input.split()
    #take the input date and split it into ['DD','MM','YYYY']
    s_date = s_birthday_entry[-1].split(".")
    del s_birthday_entry[-1]

  # creates database structure according to the notes above
  if s_date[2] not in db:
      db[str(s_date[2])] = {}
  if s_date[1] not in db[str(s_date[2])]:
      db[str(s_date[2])][str(s_date[1])] = {}
  if s_date[0] not in db[str(s_date[2])][str(s_date[1])]:
      db[str(s_date[2])][str(s_date[1])][str(s_date[0])] = []
  if (s_birthday_entry[0] + " " + s_birthday_entry[1]) not in db[str(
          s_date[2])][str(s_date[1])][str(s_date[0])]:
      db[str(s_date[2])][str(s_date[1])][str(
          s_date[0])].append(s_birthday_entry[0] + " " + s_birthday_entry[1])
      return True
  return False

#---------------------------------------------------------------------------------------------------
def get_next_birthday():
    """Deletes all entries in the database when called.
      Args:     None
      Returns:  None
      Notes:    All data will be lost 
      Examples:  
  """
    # example ['2023','02','28']
    todays_date = datetime.today().strftime('%Y-%m-%d').split("-")

    #[x for x in db.keys() if todays_date[1] in x.keys()]

    ############### DBG MM ####################################
    #---------
    # This code is not commented for security purposes!
    # Security through obscurity
    """
    month = todays_date[1]
    day = todays_date[2]
    next_birthdays = []
    while len(next_birthdays) <= 0:
        birthdays_in_month = [db[x][month] for x in db.keys() if month in db[x].keys()]   
        next_birthdays = [x for x in birthdays_in_month for y in x.keys() if y >= day]
        if len(next_birthdays) <= 0:
            month = str(int(month) + 1) if (int(month) + 1) <= 12 else "01"
            month = "0" + month if len(month) == 1 else month
            if day == "0" and month == todays_date[1]:
                break
            else:
                day = "0"
    print(next_birthdays)
    
    for birthday_entry in next_birthdays:
        for day in birthday_entry.keys():
            print(month + " " + day + " " + str(birthday_entry[day][0]))
    
    01.01.2000


    20230302

    19890201
    20000302

    db[01.01.2000] = [..]
    
    """
    #-----------
  
    print(int(datetime.today().timestamp() * 1000))
    month = todays_date[1]
    day = todays_date[2]
    next_birthdays = []
    while len(next_birthdays) <= 0:
        birthdays_in_month = []
        for year in db.keys(): 
          print("Here Ia am")
          for month in db[year].keys():
            
            if month in db[year].keys():
              print("month: " + month)
            #birthdays_in_month.append([db[x][month], x])
            for day in db[year][month]:
              birthdays_in_month.append([year, month, day, db[year][month][day].value])
          else:         
            month = str(int(month) + 1) if (int(month) + 1) <= 12 else "01"
        """next_birthdays = [x for x in birthdays_in_month for y in x.keys() if y >= day]
        if len(next_birthdays) <= 0:
            month = str(int(month) + 1) if (int(month) + 1) <= 12 else "01"
            month = "0" + month if len(month) == 1 else month
            if day == "0" and month == todays_date[1]:
                break
            else:
                day = "0"
    print(next_birthdays)"""
    
    
    for birthday_entry in next_birthdays:
        for day in birthday_entry.keys():
            print(month + " " + day + " " + str(birthday_entry[day][0]))
"""
    #define empty array with next birthday
    next_birthday = []
    #define loop break variable
    birthday_found = False

    for year in db.keys():
        print("I am in years")
        for month in db[year].keys():
            print("I am in month" + str(month))
            for day in db[year][month].keys():
                print("I am in the days")
                if month == todays_date[1] and day >= todays_date[
                        2] and birthday_found == False:
                    #if month the same as current month, only check days greater todays date
                    #get the first input later than or same as the actual date

                    #Add list [Vorname Nachname, YYYY,MM,DD]  Formatting okay???
                    buffer = [db[year][month][day].value, year, month, day]
                    next_birthday.append(buffer)
                    print(next_birthday)
                    birthday_found = True
                    del buffer
                if month > todays_date[
                        1] and birthday_found == False:  #if month later than current month, search all days
                    #get the first input later than or same as the actual date
                    buffer = [
                        db[year][month][day].value, year, month, day
                    ]  #Add list [Vorname Nachname, YYYY,MM,DD]  Formatting okay???
                    next_birthday.append(buffer)
                    print(next_birthday)
                    birthday_found = True
                    del buffer

"""
############### DBG end ################################
"""

"""

#birthdays_this_month =
get_next_birthday()

#---------------------------------------------------------------------------------------------------
def reset_database():
    """Deletes all entries in the database when called.
      Args:     None
      Returns:  None
      Notes:    All data will be lost 
      Examples:  
  """
    for key in db.keys():
        del db[key]
#---------------------------------------------------------------------------------------------------
###########################################DBG######################################################
def inputTest(s_input):
    output = s_input + "Ausgabewert"
    return output
