import os
filename = "./nlu/intent.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)

# open text file
text_file = open(filename, "w")

examples = [
    'this is a',
    'this is a',
    'this is a',
    'this is a',
    'this is a',
    'this is a',
]

# gen code
for val in examples:
    text_file.write("\t- {val}\n".format(val=val))

# close file
text_file.close()
