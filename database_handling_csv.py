#################### Import libraries/scripts ######################################################
from datetime import datetime

import pandas as pd

####################################################################################################


def reset_database():
  """Deletes all entries in the csv when called.
      Args:     None
      Returns:  None
      Notes:    All data will be lost 
      Examples:  
  """
  #re-write csv file
  with open('database_data.txt', 'w') as f:
    f.write('Vorname;Nachname;Tag;Monat;Jahr\n')
    f.close()


#---------------------------------------------------------------------------------------------------
def input_birthday_into_database(s_input):
  """
  ToDo: Write it for the csv
  
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
  print(s_birthday_entry)
  #take the input date and split it into ['DD','MM','YYYY']
  s_date = s_birthday_entry[-1].split(".")
  del s_birthday_entry[-1]

  s_csv_input = s_birthday_entry[0] + ';' + s_birthday_entry[1] + ';' + s_date[
    0] + ';' + s_date[1] + ';' + s_date[2]

  # ToDo: Check for double entries???

  #append csv with the new data
  with open('database_data.txt', 'a') as f:
    f.write(s_csv_input + '\n')
    f.close()
    return True

  #if no entry
  #return False


def get_next_birthday():
  """Get the next birthday or the next birthdays if multiple people have birthday on the same day.
    Args:     debug_print
              0 or 1 to print debug values
    Returns:  output list of the next birthday(s)
              #example: [[V1, N1, 01, 04, 1990],[V2, N2, 05, 12, 1989]]
    Notes:    All data will be lost 
    Examples: 

    Example test data for database_handling_csv.py
    Vorname;Nachname;Tag;Monat;Jahr
    V;N;01;01;2002
    V2;N2;10;02;1989
    V3;N3;08;05;1900
    V4;N4;08;03;2010
    V10;N10;08;05;2010
    V5;N5;08;03;2010
    V6;N6;09;03;1989
    V5;N5;08;03;2010
    V3;N3;19;01;1990
    V3;N3;19;01;1990
    V3;N3;19;01;1990

    
    
  """
  #debug variable to enable print commands locally
  debug_print=0
  # get todays date example ['2023','02','28']
  todays_date = datetime.today().strftime('%Y-%m-%d').split("-")
  if debug_print == 1:
    print("Todays date: ")
    print(todays_date)
  #-------------------------
  #read txt data in a table
  #ToDo: You can also only read the next two lines, compare and then read again the next line. No need to read in everything at the same time
  birthday_data = pd.read_csv('database_data.txt', sep=";", header=0)
  #define header row/column names
  #birthday_data.columns = ['Vorname', 'Nachname', 'Tag', 'Monat', 'Jahr']
  if debug_print == 1:
    print(birthday_data)
  #-------------------------
  #set next birthday to first row --> type list needed in case there are birthdays at the same date
  next_birthday_row_idx = [0]
  #initialize an arbitrary high value of days until next birthday
  days_to_birthday_min = 999
  #for-loop to go through the whole table one by one: always compare the current entry with the next, as well as with todays date
  for i in range(1, len(birthday_data['Monat'])):
    #Trick: set year to the same value, so you can compare DD.MM.1900
    date_today = datetime(1900, int(todays_date[1]), int(todays_date[2]))
    date_old = datetime(1900, birthday_data['Monat'].values[i - 1],
                        birthday_data['Tag'].values[i - 1])
    date_new = datetime(1900, birthday_data['Monat'].values[i],
                        birthday_data['Tag'].values[i])
    #--------------------------------------------------------------------------------------
    #calculate days to birthday, can be negative (in the past) or positive (in the future)
    days_to_birthday_old = date_old - date_today
    days_to_birthday_old = days_to_birthday_old.days
    if days_to_birthday_old < 0:
      #rincrease the year by one. Birthday is in the past month, so we use this trick and set the year to 1 year later
      date_old = datetime(1901, birthday_data['Monat'].values[i - 1],
                          birthday_data['Tag'].values[i - 1])
      days_to_birthday_old = date_old - date_today
      days_to_birthday_old = days_to_birthday_old.days

    days_to_birthday_new = date_new - date_today
    days_to_birthday_new = days_to_birthday_new.days
    if days_to_birthday_new < 0:
      #same idea as above
      date_new = datetime(1901, birthday_data['Monat'].values[i],
                          birthday_data['Tag'].values[i])
      days_to_birthday_new = date_new - date_today
      days_to_birthday_new = days_to_birthday_new.days
    #--------------------------------------------------------------------------------------
    if debug_print == 1:
      print("------")
      print("loop iteration: " + str(i))
      print("days to birthday old: " + str(days_to_birthday_old))
      print("days to birthday new: " + str(days_to_birthday_new))
      print("days to birthday: " + str(days_to_birthday_min))
      print("Found row indices for the same birthday: ")
      print(next_birthday_row_idx)

    #Hope I got all cases in this statement
    if days_to_birthday_new == days_to_birthday_min:
      next_birthday_row_idx.append(i)
      days_to_birthday_min = days_to_birthday_new
    elif days_to_birthday_old < days_to_birthday_new and days_to_birthday_old < days_to_birthday_min:
      #both birthdays in the future, but old is earlier than new and previous min value --> keep old value
      next_birthday_row_idx = [i - 1]
      days_to_birthday_min = days_to_birthday_old
    elif days_to_birthday_old > days_to_birthday_new and days_to_birthday_new < days_to_birthday_min:
      #both birthdays in the future, but new is earlier than old and previous min value --> keep new value
      next_birthday_row_idx = [i]
      days_to_birthday_min = days_to_birthday_new
    elif days_to_birthday_old == days_to_birthday_new and days_to_birthday_old == days_to_birthday_min:
      #if both distances are the same, append the index only if it matches the previous found distance to the next birthday
      next_birthday_row_idx.append(i)
      days_to_birthday_min = days_to_birthday_old
    else:
      if debug_print == 1:
        print(
          "The compared two lines do not yield another next birthday. No change."
        )

  #result can be a list of rows with the same DD.MM! Need to handle that for output
  if debug_print == 1:
    print("--Final result----")
    print("loop iteration: " + str(i))
    print("days to birthday old: " + str(days_to_birthday_old))
    print("days to birthday new: " + str(days_to_birthday_new))
    print("days to birthday: " + str(days_to_birthday_min))
    print("Found row indices for the same birthday: ")
    print(next_birthday_row_idx)
    #print results
    #for i in next_birthday_row_idx:
    #  print(birthday_data.iloc[i,:])
  #-----------------------------------output definition----------------
  #define output table --> smaller version of initial table
  #re-read csv all as string to get a proper output --> ToDo second time to read the csv, not very optimized
  birthday_data = pd.read_csv('database_data.txt', sep=";", header=0,dtype=str)
  
  next_birthdays_output = birthday_data.iloc[next_birthday_row_idx, :]
  #define the output list and a buffer list
  #with the nested for loop define the output structure
  next_birthdays_output_list = []
  buffer = []
  for i in range(len(next_birthdays_output)):
    for j in range(len(next_birthdays_output.columns)):
      buffer.append(next_birthdays_output.iloc[i].iat[j])
    next_birthdays_output_list.append(buffer)
    buffer = []
  #DBG print
  if debug_print == 1:
    print(next_birthdays_output_list)

  return next_birthdays_output_list




###########################################DBG######################################################
def inputTest(s_input):
  output = s_input + "Ausgabewert"
  return output
