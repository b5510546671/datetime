import datetime

UTC_OFFSET = 7
result_utc_datetime = datetime.datetime.utcnow() + datetime.timedelta(hours=UTC_OFFSET)

result_utc_datetime.strftime("%Y-%m-%d %H:%M:%S")

print(result_utc_datetime.strftime("%Y-%m-%d"))

result_utc_datetime.strftime("%H:%M:%S")
print(result_utc_datetime.strftime("%H:%M:%S"))

print(result_utc_datetime.strftime("%x : %X"))