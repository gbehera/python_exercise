import pyperclip
text = pyperclip.paste()

"""# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)"""

#------------------------------------------------------------------

"""# To convert things to UPPERCASE
hello= text.upper()"""

#------------------------------------------------------------------

pyperclip.copy(hello)

