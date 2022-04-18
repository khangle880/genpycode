# open text file
text_file = open("./data.txt", "w")

# action
s = '''\
This is a {length} example.
Here is a {ordinal} line.\
'''

name = 'z'

parameters = {'length': 'multi-line', 'ordinal': 'second'}
globals()[name] = s.format(**parameters)

# write string to file
n = text_file.write(globals()[name])

# close file
text_file.close()

print(n)
