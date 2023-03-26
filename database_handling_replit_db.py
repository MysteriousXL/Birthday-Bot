import uuid
from datetime import datetime
from replit import db


debug_print = False


def create_db_structure():
  db["years"] = dict()
  db["months"] = dict()
  db["days"] = dict()
  db["birthdays"] = dict()


def input_birthday_into_database(year, month, day, first_name, last_name):
    # check if there is no entry for the year in the years dictionary
    if year not in db["years"].keys():
        # add year to years dictionary
        db["years"][year] = []
    # check if there is no entry for the month in the months dictionary
    if month not in db["months"].keys():
        # add month to months dictionary
        db["months"][month] = []
    # check if there is no entry for the day in the days dictionary
    if day not in db["days"].keys():
        # add day to days dictionary
        db["days"][day] = []
    # get all ids that are in the list of the year, the month and the day
    common_ids = list(set(set(db["years"].get(year)).intersection(db["months"].get(month))).intersection(db["days"].get(day)))
    for birthday in common_ids:
        # check if the firstname and lastname are the same as one of the entries for the same birthdate
        if db["birthdays"][birthday]["first_name"] == first_name and db["birthdays"][birthday]["last_name"] == last_name:
            # return false to signal that no new entry is added to the database
            return False
    # create a unique id that refers to one specific birthdate + name combination
    unique_id = str(uuid.uuid1())
    # add the birthday to the birthdays in the database
    db["birthdays"][unique_id] = {"year": year, "month": month, "day": day, "first_name": first_name,
                                  "last_name": last_name}
    # set a reference to the birthday through the unique id in the years dictionary
    db["years"][year].append(unique_id)
    # set a reference to the birthday through the unique id in the months dictionary
    db["months"][month].append(unique_id)
    # set a reference to the birthday through the unique id in the days dictionary
    db["days"][day].append(unique_id)
    # signal a successful new entry to the database
    return True


def get_next_birthday():
    # get the current date and split it into a list of three strings [YYYY, MM, DD]
    current_date = datetime.today().strftime('%Y-%m-%d').split("-")
    # current_date = ["2023", "12", "31"]
    # set the month variable to the current month
    month = current_date[1]
    # set the day variable to the current day
    day = current_date[2]
    # create a list for upcoming birthdays
    next_birthday = []
    # initialise the variable for the next birthday and set it higher than legitimatly possible
    next_birthday_day = 32
    # iterate untli there is at least one entry in the list for the next birthday
    while len(next_birthday) == 0:
        # check if the month is in the month dictionary
        if month in db["months"].keys():
            # iterate over all unique ids in the month dictionary
            for birthday_id in db["months"][month]:
                # check if the entry from the month dictionary is on a later day than the day variable and earlier or equal to the former next birthday day
                if int(day) < int(db["birthdays"][birthday_id]["day"]) <= int(next_birthday_day):
                    # check if the day from the month dictionary is NOT equal to the former next birthday day
                    if next_birthday_day != db["birthdays"][birthday_id]["day"]:
                        # change the variable for the next birthday
                        next_birthday_day = db["birthdays"][birthday_id]["day"]
                        # empty the list of people that have their birthday at the next date
                        next_birthday = []
                    birthday_dict = db["birthdays"][birthday_id]
                    new_birthday_entry_as_list = []
                    new_birthday_entry_as_list.append(birthday_dict.get("first_name"))
                    new_birthday_entry_as_list.append(birthday_dict.get("last_name"))
                    new_birthday_entry_as_list.append(birthday_dict.get("day"))
                    new_birthday_entry_as_list.append(birthday_dict.get("month"))
                    new_birthday_entry_as_list.append(birthday_dict.get("year"))
                    # add the birthday entry to the list of next birthdays
                    next_birthday.append(new_birthday_entry_as_list)
        # increase the month by one
        month = str(int(month) + 1)
        # check if the month is greater than 12
        if int(month) > 12:
            # change the month to 01
            month = "01"
        # check if the month string consists of only one char
        if len(month) == 1:
            # add a leading zero to the month
            month = "0" + month
        # check if the month of the month varaible is the same as the current month and the day is set to zero
        # The zero of the day indicates, that this is not the first iteration.
        if int(month) == int(current_date[1]) and day == 0:
            # return false to signal that no next birthday was found
            return False
        # set day to zero, because the day is only relevant in the current month
        day = 0
    # return the list of birthdays
    return next_birthday


def reset_database():
    for key in db.keys():
        del db[key]

# check if database structure is set up
if "birthdays" not in db.keys():
  create_db_structure()

  
############################  Testing ##################################
"""
print("Birthdays Dictionary")
for key in db["birthdays"].keys():
  print(key)
  for k1 in db["birthdays"][key].keys():
    print("\t"+k1 +": "+ db["birthdays"][key][k1])
print("Days Dictionary")
for day in db["days"].keys():
  print(day)
  for value in db["days"][day]:
    print("\t"+value)
print("Months Dictionary")
for month in db["months"].keys():
  print(month)
  for value in db["months"][month]:
    print("\t"+value)
print("Years Dictionary")
for year in db["years"].keys():
  print(year)
  for value in db["years"][year]:
    print("\t"+value)
"""

def input_test_data():
  test_data = ["V;N;01;01;2002","V2;N2;10;02;1989","V3;N3;08;05;1900","V3.5;N3.5;08;05;1900","V4;N4;08;03;2010","V10;N10;08;05;2010",
               "V5;N5;08;03;2010","V6;N6;09;03;1989","V5;N5;08;03;2010","V3;N3;19;01;1990","V3;N3;19;01;1990",
               "V3;N3;19;01;1990"]
  for test_entry in test_data:
    test_entry = test_entry.split(";")
    input_birthday_into_database(test_entry[4], test_entry[3], test_entry[2], test_entry[0], test_entry[1])


if debug_print:
  input_test_data()
  list_of_birthdays = get_next_birthday()
  print(list_of_birthdays)
