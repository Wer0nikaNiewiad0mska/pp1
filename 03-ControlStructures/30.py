military_time = input('Enter time (24-hour format): ')
military_time.split(":")

if len(military_time) == 3:
        hours = military_time[0]
        minutes = military_time[2]
        if hours < 0:
            print("Hours can't be less than 0.")
elif len(military_time) == 4:
        if military_time[0:2] >= 10:
            hours = military_time[0:2]
            minutes = military_time[3]
            if minutes < 0:
                print("Minutes can't be less than 0.")
            if minutes < 10:
                minutes = 0 + minutes
        else:
            hours = military_time[0]
            minutes = military_time[2:]
            if minutes >= 60:
                print("Too big of a number for minutes.")
else:
    hours = military_time[0:2]
    minutes = military_time[3:]
    setting = 'AM'
if hours > 12:
    setting = 'PM'
    hours -= 12
    print(hours + ":" + minutes + setting)
