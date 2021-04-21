import pyperclip
import re

# copy text for extraction to clipboard by CTRL-A and CTRL-C
'''
Sample text to copy:
It is a long established fact that a reader will be distracted by the readable 
30/08/2022 content of a page when looking at its layout. The point of 31-10-2001 
using Lorem Ipsum is that it has 31.00.2011 a more-or-less normal distribution of 
letters, as opposed to using 'Content here, 23/10/2085 content here', making it look 
like readable English.  29/02/1976 Many desktop publishing 29/23/1973 packages and web 
page editors 31-09-2021 now use Lorem Ipsum as their default 31/11/1973 model text, 
and a search for 'lorem ipsum' will 31/01/2020 uncover many web sites still in their 
infancy. Various versions have evolved over the years, sometimes by accident, 
sometimes on purpose (injected humour and the like 03/06/2010 vestibulum ac 12.06.2019 
suscipit. Phasellus In d;lfkv abitasse vestibulum
'''

text = pyperclip.paste()

'''
Types of dates:
DD/MM/YYYY
YYYY/MM/DD
DD-MM-YYYY
YYYY-MM-DD
DD.MM.YYYY
YYYY.MM.DD
'''

def leap_year(year):
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): return True
	return False

# regex to check dates
regex = re.compile(r'''(
	((0[1-9]{1}|(1|2)[0-9]{1}|3[0-1]{1})(\.|/|-)
	(0[1-9]{1}|1[0-2]{1})(\.|/|-)
	([1-2]{1}[0-9]{3}))|(([1-2]{1}[0-9]{3})
	(\.|/|-)(0[1-9]{1}|1[0-2]{1})
	(\.|/|-)(0[1-9]{1}|(1|2)[0-9]{1}|30|31)
	)
	)''', re.VERBOSE)

# find matches in clipboard text
matches = []
for groups in regex.findall(text):
	group = re.split('[/.-]', groups[0])
	year = date = month = 0
	if len(group[-1]) == 4:
		year = int(group[-1])
		date = int(group[0])
	else:
		year = int(group[0])
		date = int(group[-1])
	month = int(group[1])
	# checking for days in feb
	if month == 2 and ((leap_year(year) and date > 29) or (not leap_year(year) and date > 28)): continue
	elif (month not in [1,3,5,7,8,10,12]) and date == 31: continue
	else: matches.append("-".join(list((str(date).rjust(2, '0'), str(month).rjust(2, '0'), str(year)))))

if matches:
	print("Copied to clipboard:")
	print("\n".join(matches))
	pyperclip.copy("\n".join(matches))
else:
	print("No year found!")
