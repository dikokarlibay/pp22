from datetime import datetime

current_datetime = datetime.now()

current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Datetime without microseconds:", current_datetime_without_microseconds)