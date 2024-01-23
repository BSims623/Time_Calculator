def add_time(start, duration, day=False):
  start_hour = start.split(':')[0]
  start_min = start.split(':')[1][0:2]
  start_am_pm = start[len(start) - 2:len(start)]
  duration_hour = duration.split(':')[0]
  duration_min = duration.split(':')[1]
  result_hour = int(start_hour) + int(duration_hour)
  result_min = int(start_min) + int(duration_min)
  result_am_pm = start_am_pm
  # handle result time
  result_hour = result_hour + int(result_min / 60)
  # handle am_pm
  if (int(result_hour / 12) % 2) == 1:
    result_am_pm = am_pm(result_am_pm)
  # handle days passed
  if start_am_pm == 'AM':
    days_passed = int(result_hour / 24)
  else:
    if result_hour < 12:
      days_passed = 0
    else:
      days_passed = int((result_hour - 12) / 24) + 1
  # handle new day    
  if day:
    new_day = return_day(day,days_passed)
  if days_passed == 1:
    days_passed = '(next day)'
  elif days_passed > 1:
    days_passed = f'({days_passed} days later)'
  # format final result time
  result_hour = result_hour % 12
  if result_hour == 0:
    result_hour = '12'
  else:
    result_hour = str(result_hour)
  result_min = format_min(result_min % 60)  

  if day and days_passed != 0:
    return f'{result_hour}:{result_min} {result_am_pm}, {new_day} {days_passed}'
  elif day:
    return f'{result_hour}:{result_min} {result_am_pm}, {new_day}'
  elif days_passed != 0:
    return f'{result_hour}:{result_min} {result_am_pm} {days_passed}'
  else:  
    return f'{result_hour}:{result_min} {result_am_pm}'

def am_pm(current):
  if current == 'AM':
    return 'PM'
  else:
    return 'AM'

def format_min(time):
  if time == 0:
    return '00'
  elif time < 10:
    return f'0{time}'
  else:
    return str(time)

def return_day(day,days_passed):
  days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
  new_day = days.index(day.lower())
  new_day_index = (new_day + days_passed) % 7
  return days[new_day_index].capitalize()