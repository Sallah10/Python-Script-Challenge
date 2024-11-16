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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A: Find all area codes and prefixes called by people in Bangalore
codes = set()  # To store unique codes
total_calls_from_080 = 0
calls_to_080 = 0

for call in calls:
    caller = call[0]
    receiver = call[1]

    # Check if the call originated from Bangalore (starts with (080))
    if caller.startswith("(080)"):
        total_calls_from_080 += 1

        # Fixed line numbers: Extract area code inside parentheses
        if receiver.startswith("("):
            end_idx = receiver.find(")")
            area_code = receiver[1:end_idx]  # Extract code excluding parentheses
            codes.add(area_code)

            # Count if the receiver is also from Bangalore
            if area_code == "080":
                calls_to_080 += 1

        # Mobile numbers: Start with 7, 8, or 9 and contain a space
        elif " " in receiver and receiver[0] in "789":
            mobile_prefix = receiver[:4]  # First 4 digits as prefix
            codes.add(mobile_prefix)

        # Telemarketers: Start with 140
        elif receiver.startswith("140"):
            codes.add("140")

# Part A Output
sorted_codes = sorted(codes)  # Lexicographic order
print("The numbers called by people in Bangalore have codes:")
for code in sorted_codes:
    print(code)

# Part B: Calculate percentage of calls to fixed lines in Bangalore
percentage = (calls_to_080 / total_calls_from_080) * 100
print(f"{percentage:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
