def add_time(start, duration, dow=None):
    hours = get_hours(start,duration)
    minutes = get_mins(start,duration)
    total_hours, total_minutes = add_times(hours, minutes)
    days_passed = get_days_passed(total_hours)
    new_time = format_time(total_hours, total_minutes, dow)
    return new_time


def get_hours(start, duration):
    suffix = get_suffix(start)
    inputs = [start, duration]
    hours = []
    for i in inputs:
        hour, minute = i.split(':')
        if len(hours) == 0 and suffix == 'PM':
            hour = int(hour)
            hour += 12
        hours.append(hour)
    return hours


def get_mins(start, duration):
    inputs = [start, duration]
    minutes = []
    for i in inputs:
        hour, minute = i.split(':')
        if len(minute) > 2:
            minute, suffix = minute.split(' ')
        minutes.append(minute)
    return minutes


def get_suffix(start):
    suffix = start.split(' ')[1]
    return suffix


def add_times(hours, minutes):
    hours = sum(list(map(int, hours)))
    minutes = sum(list(map(int, minutes)))
    if minutes >= 60:
        hours += 1
        minutes -=60
    return hours, minutes


def format_time(hours, minutes, dow=None):
    days_passed, string = get_days_passed(hours)
    if dow != None:
        new_dow = get_dow(dow, days_passed)
        new_dow = ","+" "+new_dow.capitalize()
    else:
        new_dow = ''
    current_hour = hours % 24
    if current_hour > 12:
        current_hour -=12
        suffix = 'PM'
    elif current_hour == 12:
        suffix = 'PM'
    elif current_hour == 0:
        current_hour = 12
        suffix = 'AM'
    else:
        suffix = 'AM'
    if minutes < 10:
        minutes = f'0{minutes}'
    return f'{current_hour}:{minutes} {suffix}{new_dow}{string}'

    
def get_days_passed(hours):
    days_passed = hours // 24
    if days_passed == 0:
        string = ''
    elif days_passed == 1:
        string = ' (next day)'
    else:
        string = f' ({days_passed} days later)'
    return days_passed, string


def get_dow(dow, days_passed):
    dow = dow.lower()
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    index = (days.index(dow) + days_passed)%7
    day = days[index]
    return day


print(add_time('3:30 PM', '2:12', 'Monday'))


