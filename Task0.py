"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
first_text = texts[0]
incoming_text = first_text[0]
answering_text = first_text[1]
text_time = first_text[2]

last_call = calls[-1]
incoming_call = last_call[0]
answering_call = last_call[1]
call_time = last_call[2]
duration = last_call[3]

print(f"First record of texts, {incoming_text} texts {answering_text} at time {text_time}")
print(f"Last record of calls, {incoming_call} calls {answering_call} at time {call_time}, lasting {duration} seconds"
)