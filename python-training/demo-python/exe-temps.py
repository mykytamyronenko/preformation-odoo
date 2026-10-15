time_in_sec = 4561
sec_in_one_day = 86400
sec_in_one_hour = 3600
sec_in_one_minute = 60

day = time_in_sec // sec_in_one_day
rest = time_in_sec % sec_in_one_day

hour = rest // sec_in_one_hour
rest = rest % sec_in_one_hour

minute = rest // sec_in_one_minute
rest = rest % sec_in_one_minute

second = rest


print("There are ",day," days ", hour," hours ", minute," minutes ",second," seconds in ",time_in_sec,".")

# V2 (test), could be cleaner
TIME_IN_SEC = 4561
SEC_IN_ONE_DAY = 86400
SEC_IN_ONE_HOUR = 3600
SEC_IN_ONE_MINUTE = 60

second = TIME_IN_SEC % SEC_IN_ONE_MINUTE

minute = (TIME_IN_SEC - second) // SEC_IN_ONE_MINUTE
minute %= SEC_IN_ONE_MINUTE

hour = (TIME_IN_SEC - second - minute * SEC_IN_ONE_MINUTE) // SEC_IN_ONE_HOUR
hour %= SEC_IN_ONE_HOUR

day = (TIME_IN_SEC - second - minute * SEC_IN_ONE_MINUTE - hour * SEC_IN_ONE_HOUR) // SEC_IN_ONE_DAY
day %= SEC_IN_ONE_DAY

print("There are ",day," days ", hour," hours ", minute," minutes ",second," seconds in ",TIME_IN_SEC,".")
print(f"{TIME_IN_SEC} seconds is : {day} day(s), {hour} hour(s), {minute} minutes and {second} seconds.")