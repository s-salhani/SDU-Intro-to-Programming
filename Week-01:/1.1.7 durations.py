# converts seconds into hours, minutes, and seconds.

# Input
total_seconds = 10000


# Calculate hours
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

# calculate minutes
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60



 # Output
print(hours)
print(minutes)
print(seconds)
