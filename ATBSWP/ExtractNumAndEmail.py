# python program to extract emails and phone numbers from text
import pyperclip
import re

# copy text for extraction to clipboard by CTRL-A and CTRL-C

text = pyperclip.paste()

# regex to check phone numbers
phone_regex = re.compile(r'''(
	((\+\d{2,3}) | \(\+\d{2,3}\))?
	((\s) | -)?
	(\d{10})
	)''', re.VERBOSE)

# regex to check emails
email_regex = re.compile(r'''(
	[a-zA-Z0-9+._-]+
	@
	[a-zA-Z0-9.-]+
	(\.[A-Za-z]{2,4})
	)''', re.VERBOSE)

# find matches in clipboard text
matches = []
for groups in phone_regex.findall(text):
	matches.append(groups[0])

for groups in email_regex.findall(text):
	matches.append(groups[0])

if len(matches) > 0:
	print("Copied to clipboard:")
	print("\n".join(matches))
	pyperclip.copy("\n".join(matches))
else:
	print("No email or number found in text!")
