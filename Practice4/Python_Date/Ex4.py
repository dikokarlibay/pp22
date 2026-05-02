from datetime import datetime

def date_difference_in_seconds(date1, date2):
    # Calculate the difference between the two dates
    difference = date2 - date1
    # Convert the difference to seconds
    difference_in_seconds = difference.total_seconds()
    return difference_in_seconds

date1 = datetime(2023, 6, 1, 12, 0, 0)  # First date
date2 = datetime(2023, 6, 2, 12, 0, 0)  # Second date

# Calculate the difference in seconds
difference_seconds = date_difference_in_seconds(date1, date2)

print("Difference between the two dates in seconds:", difference_seconds)