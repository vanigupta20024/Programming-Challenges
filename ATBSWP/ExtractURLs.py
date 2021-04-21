# python program to check for valid URLs
import pyperclip
import re

# copy text for extraction to clipboard by CTRL-A and CTRL-C

text = pyperclip.paste()

# regex to check URLs
url_regex = re.compile(r'''(
	https?://
	((w{3} | W{3})\.)?
	[a-zA-Z0-9_-]+
	\.
	[a-zA-Z]+
	)''', re.VERBOSE)

# find matches in clipboard text
matches = []
for groups in url_regex.findall(text):
	matches.append(groups[0])

if matches:
	print("Copied to clipboard:")
	print("\n".join(matches))
	pyperclip.copy("\n".join(matches))
else:
	print("No email or number found in text!")
