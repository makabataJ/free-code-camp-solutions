def add_time(start, duration, start_day=None):
  """
  args: start (str): 12 hour clock of the formart 3:00 PM --> reqiured
      : duration(str): time delta of the formart Hours:Minutes --> requied
      : start_day(str):  starting day of the week
  """
  if start_day:
    start_day = start_day.upper()
  meridians = ["AM", "PM"]
  weekdays = [
    "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY",
    "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"
  ]
  legal_hours = list(range(1, 13))
  start_meridian = start.split(" ")[1]
  if start_meridian != meridians[0]:
    meridians.reverse()
  minutes_counter = 0
  hours_counter = 0
  # get minutes inouts
  initial_minutes = int(start.split(":")[1].split(" ")[0])
  additional_minues = int(duration.split(":")[1])
  # get hours inputs
  initial_hours = int(start.split(":")[0])
  additional_hours = int(duration.split(":")[0])

  # Get the total number of hours and minutes
  if additional_minues > 59:
    hours_to_add = additional_minues//60
    remaining_minutes = additional_minues%60
    minutes_counter = initial_minutes + remaining_minutes
    hours_counter = initial_hours + hours_to_add + additional_hours
  else:
    minutes_counter = initial_minutes + additional_minues
    hours_counter = initial_hours + additional_hours

  if minutes_counter > 59:
    hours_to_add = minutes_counter//60
    total_minutes = minutes_counter%60
    total_hours = hours_to_add + hours_counter
  else:
    total_minutes = minutes_counter
    total_hours = hours_counter
  total_minutes = str(total_minutes)
  if len(total_minutes) == 1:
    total_minutes = f"0{total_minutes}"
  # get days passed
  days_passed = total_hours//24
  day_passed_message = ''
  if start_meridian == "PM":
    if 12<= total_hours <24 and initial_hours < 12:
      day_passed_message = 'next day'
    elif total_hours < 12:
      day_passed_message = ''
    else:
      day_passed_message = f'{days_passed + 1} days later' 
  elif not days_passed:
    pass
  elif days_passed == 1:
    day_passed_message = 'next day'
  else:
    day_passed_message = f'{days_passed} days later'
  # Get the number of hours difference from the start to the new hours
  # hours_diff = total_hours - initial_hours
  if start_day and days_passed:
    new_weekdays = weekdays*days_passed
    index_start_date = weekdays.index(start_day)
    if start_meridian == "PM":
      days_passed = int(day_passed_message.split(' ')[0])
      print(new_weekdays)
      weekday = new_weekdays[index_start_date+days_passed]
      weekday = weekday[0] + weekday[1:].lower()
    else:
      weekday = new_weekdays[index_start_date+days_passed]
      weekday = weekday[0] + weekday[1:].lower()   
  elif not start_day:
    pass
  else:
    weekday = start_day
    weekday = weekday[0] + weekday[1:].lower()

  
    
  # get the new hours_diff
  new_hours = legal_hours*(total_hours//12 +1)
  new_hour = new_hours[total_hours-1]
  
  new_meridian = ''
  meridians_passed = total_hours//12
  if meridians_passed%2 == 0:
    new_meridian = start_meridian
  else:
    new_meridian = meridians[1]
  if start_day and day_passed_message:
    new_time = f"{new_hour}:{total_minutes} {new_meridian}, {weekday} ({day_passed_message})"
  elif day_passed_message:
    new_time = f"{new_hour}:{total_minutes} {new_meridian} ({day_passed_message})"
  elif start_day:
    new_time = f"{new_hour}:{total_minutes} {new_meridian}, {weekday}"
  else:
    new_time = f"{new_hour}:{total_minutes} {new_meridian}"
    
  return new_time
