
import os
filename = "./action/abc.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)

# open text file
text_file = open(filename, "w")

actions = [
    {
        "index": "1",
        "intentId": "625a7d31021ef3afcf37a94c",
        "actionId": "625a74f674f1fb9f9a4b6291",
        "inputs": ["abc_slot"],
        "outputMapNames": {
            "xyz": "cleared_slot"
        },
    }, {
        "index": "2",
        "intentId": "625a7d31021ef3afcf37a94c",
        "actionId": "625a74f674f1fb9f9a4b6291",
        "inputs": ["abc_slot"],
        "outputMapNames": {
        }
    }
]

clear = '''
def my_function({val1}):
    {val1} = ''
'''

# gen code
for val in actions:
    val1 = "globals()['{name}']".format(name=val['inputs'][0])
    function = clear.format(val1=val1)
    xyz = val['outputMapNames'].get('xyz')
    text_file.write("globals()['{xyz}'] = {function}\n".format(
        xyz=xyz if xyz else 'xyz', function=function))

# close file
text_file.close()
