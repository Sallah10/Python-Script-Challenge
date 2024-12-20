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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
# Creating sets for outgoing calls, incoming calls, texts sent, and texts received
outgoing_calls = set()
incoming_calls = set()
texts_sent = set()
texts_received = set()

for call in calls:
    outgoing_calls.add(call[0])  
    incoming_calls.add(call[1])  

for text in texts:
    texts_sent.add(text[0])      
    texts_received.add(text[1])  

# Identifying telemarketers
# Telemarketers make calls but are not in any of the other sets so we Remove the other sets.
telemarketers = outgoing_calls - incoming_calls - texts_sent - texts_received

# Sorting in lexicographic order and printing the results
print("These numbers could be telemarketers: ")
for number in sorted(telemarketers):  # Lexicographic order
    print(number)
