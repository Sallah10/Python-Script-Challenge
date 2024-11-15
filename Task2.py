"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# # Dictionary to store total time spent by each telephone number
# call_durations = {}

# # Process each call record
# for call in calls:
#     incoming_number = call[0]
#     answering_number = call[1]
#     call_time = int(call[3])  # Duration in seconds

#     # Add duration to the incoming number
#     call_durations[incoming_number] = call_durations.get(incoming_number, 0) + call_time

#     # Add duration to the answering number
#     call_durations[answering_number] = call_durations.get(answering_number, 0) + call_time

# # Find the number with the longest total time
# longest_time_number = max(call_durations, key=call_durations.get)
# longest_time = call_durations[longest_time_number]

# # Print the result
# print(f"{longest_time_number} spent the longest time, {longest_time} seconds, on the phone during September 2016.")

call_durations = {}

for call in calls:
    incoming_call = call[0]
    answering_call = call[1]
    time = int(call[3])

call_durations[incoming_call] = call_durations.get(incoming_call, 0) + time

call_durations[answering_call] = call_durations.get(answering_call, 0) + time

longest_time_number = max(call_durations, key=call_durations.get)
longest_time = call_durations[longest_time_number]

print(f"{longest_time_number} spent the longest time, {longest_time} seconds, on the phone during September 2016.")